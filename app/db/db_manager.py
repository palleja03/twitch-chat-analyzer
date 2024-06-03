from datetime import datetime, timezone
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, DYNAMODB_TABLE_NAME
import os

class DBManager:
    def __init__(self):
        self._table_name = DYNAMODB_TABLE_NAME

        # Initialize DynamoDB resource
        self._dynamodb = boto3.resource(
            'dynamodb',
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        self._table = self._dynamodb.Table(self._table_name)

    def write_chat_log(self, channel_id, user_id, message, timestamp):
        try:
            partition_key = f"{channel_id}::{user_id}"
            sort_key = timestamp[:19]
            response = self._table.put_item(
                Item={
                    'channel_user': partition_key,
                    'timestamp': sort_key,
                    'message': message,
                }
            )
            return response
        except (NoCredentialsError, PartialCredentialsError) as e:
            print(f"Credentials not available: {e}")
            return None
        except Exception as e:
            print(f"Error writing to DynamoDB: {e}")
            return None

    # def query_chat_logs(self, channel_id, start_time, end_time):
    #     try:
    #         response = self._table.query(
    #             KeyConditionExpression=Key('channel_id').eq(channel_id) & 
    #                                    Key('timestamp_user').between(start_time, end_time)
    #         )
    #         return response['Items']
    #     except Exception as e:
    #         print(f"Error querying DynamoDB: {e}")
    #         return None

# # Example usage
# if __name__ == "__main__":
#     db_manager = DBManager()
#     current_timestamp = datetime.now(timezone.utc).isoformat()  # ISO 8601 format with timezone
#     db_manager.write_chat_log('channel_123', 'user_abc', 'Hello, World!', current_timestamp)

#     # Example query
#     start_time = '2024-06-02T00:00:00+00:00::'
#     end_time = '2024-06-02T23:59:59+00:00::'
#     logs = db_manager.query_chat_logs('channel_123', start_time, end_time)
    
#     if logs is not None:
#         for log in logs:
#             print(log)
#     else:
#         print("No logs found or an error occurred.")
