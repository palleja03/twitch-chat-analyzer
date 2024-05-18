from twitchio.ext import commands
from random import randint
from db.db_manager import save_message_to_db
from twitch.token_manager import refresh_access_token, validate_token
from config import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, INITIAL_CHANNELS, NICK

access_token, new_refresh_token = refresh_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
token_info = validate_token(access_token)
print(f"Access Token Scopes: {token_info.get('scopes')}")

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=f'oauth:{access_token}',
            client_id=CLIENT_ID,
            nick=NICK,
            prefix='$$',
            initial_channels=INITIAL_CHANNELS
        )

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        for channel in self.connected_channels:
            print(f'Connected to channel: {channel.name}')

    async def event_message(self, message):
        print(f'{message.author.name} in {message.channel.name}: {message.content}')
        save_message_to_db(message.author.name, message.content, message.channel.name)
        await self.handle_commands(message)

    # Sample commands
    
    # @commands.command(name='testhello')
    # async def holapalleja(self, ctx):
    #     await ctx.send("Hello, I am a friendly bot")

    # @commands.command(name='testroulette')
    # async def roulette(self, ctx):
    #     dice = randint(1, 6)
    #     if dice == 6:
    #         user_to_timeout = ctx.author.name
    #         try:
    #             await ctx.channel.timeout(user_to_timeout, duration=60, reason="Roulette timeout")
    #             await ctx.send(f"{user_to_timeout}, you rolled a 6 and have been timed out for 1 minute!")
    #         except Exception as e:
    #             await ctx.send(f"Failed to timeout {user_to_timeout}: {str(e)}")
    #     else:
    #         await ctx.send(f"{ctx.author.name}, you're safe! You rolled a {dice}.")
