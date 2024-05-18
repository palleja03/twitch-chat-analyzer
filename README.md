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
├── twitch_chat_analyzer/
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

- Python 3.x
- Twitch account and API credentials
- [Twitch Token Generator](https://twitchtokengenerator.com/) (optional, for generating refresh tokens)

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/twitch-chat-analyzer.git
    cd twitch-chat-analyzer
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

### Usage

1. **Initialize the database**:

    The database is automatically initialized when you run the `main.py` script.

2. **Run the bot**:

    ```sh
    python -m twitch_chat_analyzer.main
    ```

### Scripts

- `main.py`: Entry point of the application. Initializes the database and starts the bot.
- `db_manager.py`: Contains functions to initialize the database and save messages.
- `auth_url.py`: Generates the authorization URL for Twitch API.
- `get_refresh_token.py`: Script to obtain a refresh token using an authorization code.
- `token_manager.py`: Contains functions to refresh and validate the access token.
- `bot.py`: Defines the Twitch bot, its events, and commands.

### Example .env File

```ini
CLIENT_ID=exampleclientid123
CLIENT_SECRET=examplesecretkey123
REFRESH_TOKEN=examplerefreshtoken123
INITIAL_CHANNELS=channel1,channel2,channel3
NICK=example_nick
