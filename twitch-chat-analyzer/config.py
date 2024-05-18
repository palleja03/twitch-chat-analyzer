import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
TOKEN_URL = 'https://id.twitch.tv/oauth2/token'
VALIDATION_URL = 'https://id.twitch.tv/oauth2/validate'
INITIAL_CHANNELS = os.getenv('INITIAL_CHANNELS').replace(' ','').split(',')
NICK = os.getenv('NICK')
