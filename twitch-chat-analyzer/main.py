from twitch.bot import Bot
from db.db_manager import initialize_db

if __name__ == '__main__':
    initialize_db()  # Initialize the database
    bot = Bot()
    bot.run()
