# Twitch Chat Analyzer

Twitch Chat Analyzer is a Python project that connects to the Twitch API, pulls chat logs, and saves them into a database. The project is designed to analyze user engagement in chat and can be extended with additional functionalities like sentiment analysis, A/B testing, and so.

## Features

- Connects to Twitch API
- Pulls chat logs and saves them to an AWS RDS MySQL database
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
- AWS account with RDS MySQL database

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
    RDS_HOST=[RDS Endpoint]
    RDS_DATABASE=[RDS Database Name]
    RDS_USER=[RDS Username]
    RDS_PASSWORD=[RDS Password]
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

6. **Set Up AWS RDS MySQL**:

    1. Go to the [AWS Management Console](https://aws.amazon.com/console/).
    2. Navigate to the RDS service and create a new MySQL instance.
    3. Ensure you make note of your RDS endpoint, database name, username, and password.
    4. Ensure the security group for your RDS instance allows inbound traffic on port `3306` from your local machine’s IP or the EC2 instance you will be using.

7. **Create the Database**:

    1. Connect to your RDS instance using a MySQL client:

    ```sh
    mysql -h your-rds-endpoint.amazonaws.com -u your-username -p
    ```

    2. Create the `twitch-log` database and the `twitch_chat` table:

    ```sql
    CREATE DATABASE `twitch-log`;
    USE `twitch-log`;
    CREATE TABLE IF NOT EXISTS twitch_chat (
        id INT AUTO_INCREMENT PRIMARY KEY,
        channel_id VARCHAR(255) NOT NULL,
        user_id VARCHAR(255) NOT NULL,
        message TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

8. **Run the application**:

    To start logging Twitch chat messages, follow these steps:

    1. Open your terminal or command prompt.
    2. Activate the virtual environment with the following command:

    ```sh
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    3. Ensure your `.env` file and `initial_channels.txt` are properly configured.
    4. Start the main application by running:

    ```sh
    python app/main.py
    ```

    This will start the bot and connect it to the Twitch API. It will begin logging chat messages from the specified channels into your RDS MySQL database.


### Scripts

- `main.py`: Entry point of the application. Starts the bot and initializes database connections.
- `db_manager.py`: CContains the DBManager class to connect to AWS RDS MySQL and save chat messages.
- `auth_url.py`: Generates the authorization URL for Twitch API.
- `get_refresh_token.py`: Script to obtain a refresh token using an authorization code.
- `token_manager.py`: Contains functions to refresh and validate the access token.
- `bot.py`: Defines the Twitch bot, its events, and commands.


### Summary of Changes

- Removed references to the local SQLite database.
- Added instructions for setting up `initial_channels.txt` and `.env`.
- Updated the need for AWS DynamoDB and appropriate credentials.
- Simplified the setup instructions by leveraging example configuration files.
