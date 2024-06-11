import mysql.connector
from mysql.connector import Error
from config import RDS_HOST, RDS_DATABASE, RDS_USER, RDS_PASSWORD

class DBManager:
    def __init__(self):
        self.connection = None
        self.connect_to_rds()

    def connect_to_rds(self):
        """Establishes connection to the MySQL database on RDS."""
        try:
            self.connection = mysql.connector.connect(
                host=RDS_HOST,
                database=RDS_DATABASE,
                user=RDS_USER,
                password=RDS_PASSWORD
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")
            self.connection = None

    def reconnect(self):
        """Reconnect to the database if the connection was lost."""
        if self.connection is None or not self.connection.is_connected():
            print("Reconnecting to the database...")
            self.connect_to_rds()

    def write_chat_log(self, channel_id, user_id, message, timestamp):
        """Writes a chat log to the database."""
        self.reconnect()  # Ensure we are connected before performing any operation
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()
                insert_query = '''
                INSERT INTO twitch_logs (channel_id, user_id, message, timestamp)
                VALUES (%s, %s, %s, %s)
                '''
                cursor.execute(insert_query, (channel_id, user_id, message, timestamp))
                self.connection.commit()
                # print(f"Chat log inserted: {channel_id}, {user_id}, {message}")
            except Error as e:
                print(f"Error inserting chat log: {e}")
            finally:
                cursor.close()

    def close_connection(self):
        """Close the database connection."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

