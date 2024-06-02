import os

def get_auth_url(client_id):
    redirect_uri = "http://localhost"
    return f"https://id.twitch.tv/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=chat:read"

if __name__ == '__main__':
    CLIENT_ID = os.getenv('CLIENT_ID')
    print("Authorization URL:", get_auth_url(CLIENT_ID))