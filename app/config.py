# import os
# from dotenv import load_dotenv

# load_dotenv()

# CLIENT_ID = os.getenv('CLIENT_ID')
# CLIENT_SECRET = os.getenv('CLIENT_SECRET')
# REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
# TOKEN_URL = 'https://id.twitch.tv/oauth2/token'
# VALIDATION_URL = 'https://id.twitch.tv/oauth2/validate'
# INITIAL_CHANNELS = os.getenv('INITIAL_CHANNELS').replace(' ','').split(',')
# NICK = os.getenv('NICK')

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Amazon Variables ---------------------------------------

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
DYNAMODB_TABLE_NAME = os.getenv('DYNAMODB_TABLE_NAME')


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