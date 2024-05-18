import requests
from config import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, TOKEN_URL, VALIDATION_URL

def refresh_access_token(client_id, client_secret, refresh_token):
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(TOKEN_URL, params=params)
    response.raise_for_status()
    token_info = response.json()
    return token_info['access_token'], token_info['refresh_token']

def validate_token(access_token):
    headers = {
        'Authorization': f'OAuth {access_token}'
    }
    response = requests.get(VALIDATION_URL, headers=headers)
    response.raise_for_status()
    return response.json()
