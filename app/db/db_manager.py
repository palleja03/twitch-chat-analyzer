import boto3
import json
from queue import Queue
from datetime import datetime, timezone
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, DYNAMODB_TABLE_NAME


def calculate_item_size(item):
    return len(json.dumps(item).encode('utf-8'))

def estimate_wc_usage(items):
    total_size = sum(calculate_item_size(item) for item in items)
    return (total_size + 1023) // 1024  # Round up to the nearest KB



class DBManager:
    def __init__(self, buffer_size=25):
        self._table_name = DYNAMODB_TABLE_NAME

        # Initialize DynamoDB resource
        self._dynamodb = boto3.resource(
            'dynamodb',
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        self._table = self._dynamodb.Table(self._table_name)

        # Buffer settings
        self.latest_buffer = datetime.now(timezone.utc).isoformat()[:16]
        self.buffer = []
        self.buffer_size = buffer_size  


    def buffer_message(self, channel_id, user_id, message, timestamp):
        partition_key = f"{channel_id}::{user_id}"
        sort_key = timestamp[:16]
        new_message = {'message': message, 'timestamp': timestamp}

        # Check for existing items in the buffer
        for buffered_item in self.buffer:
            if buffered_item['channel_user'] == partition_key and buffered_item['ts_min'] == sort_key:
                buffered_item['messages'].append(new_message)
                break
        else:
            item = {
                'channel_user': partition_key,
                'ts_min': sort_key,
                'messages': [new_message]
            }
            self.buffer.append(item)

        flush_mask = datetime.now(timezone.utc).isoformat()[:16]
        if flush_mask > self.latest_buffer and len(self.buffer) >= self.buffer_size:
            self.flush_buffer(flush_mask)

    def flush_buffer(self, flush_mask):
        if not self.buffer:
            return
        try:
            flush_items = [item for item in self.buffer if item['ts_min'] != flush_mask]
            flush_len = len(flush_items)

            # Split flush_items into smaller lists of size buffer_size
            for i in range((flush_len // self.buffer_size)+1):
                l,r = i*self.buffer_size, min((i+1)*self.buffer_size, flush_len)
                batch_items = flush_items[l:r]
                if len(batch_items) == 0:
                    break
                with self._table.batch_writer() as batch:
                    for item in batch_items:
                        batch.put_item(Item=item)

            self.buffer = [item for item in self.buffer if not (item in flush_items)]
            self.latest_buffer = flush_mask
        except (NoCredentialsError, PartialCredentialsError) as e:
            print(f"Credentials not available: {e}")
        except Exception as e:
            print(f"Error writing to DynamoDB: {e}")

    def close(self):
        # Ensure any remaining messages are flushed when closing
        if self.buffer:
            flush_mask = datetime.now(timezone.utc).isoformat()[:16]
            self.flush_buffer(flush_mask)