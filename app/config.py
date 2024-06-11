import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Amazon Variables ---------------------------------------

RDS_HOST = os.getenv('RDS_HOST')
RDS_DATABASE = os.getenv('RDS_DATABASE')
RDS_USER = os.getenv('RDS_USER')
RDS_PASSWORD = os.getenv('RDS_PASSWORD')


# Twitch Variables ---------------------------------------

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
TOKEN_URL = 'https://id.twitch.tv/oauth2/token'
VALIDATION_URL = 'https://id.twitch.tv/oauth2/validate'
NICK = os.getenv('NICK')

# Load initial channels from a .txt file
def load_initial_channels(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    file_path = os.path.join(script_dir, filename)  # Construct the full file path
    with open(file_path, 'r') as file:
        channels = [line.strip() for line in file if line.strip()]
    return channels

INITIAL_CHANNELS = load_initial_channels('initial_channels.txt')



