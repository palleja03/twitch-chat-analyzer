import requests
from config import CLIENT_ID, CLIENT_SECRET

def get_refresh_token(auth_code):
    redirect_uri = "http://localhost"
    url = 'https://id.twitch.tv/oauth2/token'
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': auth_code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    auth_code = input("Enter the authorization code: ")
    token_info = get_refresh_token(auth_code)
    print("Refresh Token:", token_info['refresh_token'])
