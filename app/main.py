from twitch.bot import Bot

if __name__ == '__main__':
    bot = Bot()
    try:
        bot.run()
    except KeyboardInterrupt:
        # If the bot is interrupted (e.g., by Ctrl+C), ensure it shuts down gracefully
        bot.close()
