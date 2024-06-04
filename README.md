# Twitch Chat Analyzer

Twitch Chat Analyzer is a Python project that connects to the Twitch API, pulls chat logs, and saves them into a database. The project is designed to analyze user engagement in chat and can be extended with additional functionalities like sentiment analysis, A/B testing, and so.

## Features

- Connects to Twitch API
- Pulls chat logs and saves them to a SQLite database
- Basic bot commands
- Modular and extensible structure

## Project Structure

```plaintext
twitch-chat-analyzer/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── db_manager.py
│   │   └── chat_messages.db  # Database file
│   ├── twitch/
│   │   ├── __init__.py
│   │   ├── auth_url.py
│   │   ├── bot.py
│   │   ├── get_refresh_token.py
│   │   └── token_manager.py
├── venv/
├── .env
├── setup.py
├── README.md
└── requirements.txt
```


## Getting Started

### Prerequisites

- Python 3.9.x
- Twitch account and API credentials
- [Twitch Token Generator](https://twitchtokengenerator.com/) (optional, for generating refresh tokens)
- AWS account with DynamoDB

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/twitch-chat-analyzer.git
    ```

2. **Set up a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Create and configure the `.env` file**:

    Create a `.env` file in the root directory with the following content:

    ```ini
    CLIENT_ID=[Twitch Client ID]
    CLIENT_SECRET=[Twitch API secret key]
    REFRESH_TOKEN=[generated via get_refresh_token.py / can also be obtained with https://twitchtokengenerator.com/]
    INITIAL_CHANNELS=[channels you want to join, separated by comma]
    NICK=[your twitch nick]
    ```

5. **Create and configure the `initial_channels.txt` file**:

    Create a `initial_channels.txt` file in the root directory, or copy the provided `initial_channels.example.txt` and fill in your desired channels:

    ```sh
    cp initial_channels.example.txt initial_channels.txt
    ```

    Then edit the `initial_channels.txt` file with the channels you want to join, one per line:

    ```plaintext
    channel_1
    channel_2
    channel_3
    ```

6. **Set up AWS DynamoDB**:

    Ensure you have an AWS account and set up DynamoDB. You will need to configure AWS credentials which can be stored in environment variables or use AWS IAM roles if deploying on AWS services.

    If using environment variables, ensure the following are set:

    ```sh
    AWS_ACCESS_KEY_ID=[Your AWS Access Key ID]
    AWS_SECRET_ACCESS_KEY=[Your AWS Secret Access Key]
    AWS_REGION=[Your AWS Region]
    ```

    Alternatively, configure your AWS credentials using the AWS CLI:

    ```sh
    aws configure
    ```

6. **Run the application**:

    Start the main application:

    ```sh
    python main.py
    ```

### Scripts

- `main.py`: Entry point of the application. Starts the bot.
- `db_manager.py`: Contains DBManager class to connect to AWS DynamoDB and save messages.
- `auth_url.py`: Generates the authorization URL for Twitch API.
- `get_refresh_token.py`: Script to obtain a refresh token using an authorization code.
- `token_manager.py`: Contains functions to refresh and validate the access token.
- `bot.py`: Defines the Twitch bot, its events, and commands.


### Summary of Changes

- Removed references to the local SQLite database.
- Added instructions for setting up `initial_channels.txt` and `.env`.
- Updated the need for AWS DynamoDB and appropriate credentials.
- Simplified the setup instructions by leveraging example configuration files.
