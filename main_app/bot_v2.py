import dotenv, os , asyncio, discord
from main_app.Bot_custom import Bot_with_javis
from utils import debug_log
from discord.ext import commands
from pathlib import Path
dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN_DISCORD")

DEBUG = os.getenv("RUN") # in debug mode, bot will delay at 5 minuts = 300 in diem danh
debug_log.info(DEBUG)


# MY_GUILD = discord.Object(id=os.getenv(str(DEBUG)+"_guild")) 

# if DEBUG == "tuan":
#     CHANNEL_ID = 902626872725217305
# elif DEBUG == "ttcd":
#     MY_GUILD = discord.Object(id=868410572369174539) # Trung tâm Chí Dũng guild
#     CHANNEL_ID = os.getenv("STARTUP_ROLE_VIEW_CHANNEL_ID")
#     print(type(CHANNEL_ID))
# elif DEBUG == "bkt":
#     MY_GUILD = discord.Object(id=895928190772609035) # BKT guild

################################ GLOBAL VARIABLES #################################
intents = discord.Intents.all() # enable all gateway intents
# intents.members = True
# intents.message_content = True
stop_check_class = False # check status of continue diemdanh
if "ttcd" in DEBUG:# sài thật
    delay_time_at_diemdanh = 300 # 5 phut
    delete_after_at_diemdanh = 200
else: # đang code
    delay_time_at_diemdanh = 5 # 5 giay
    delete_after_at_diemdanh = 3


# Get the current working directory
current_directory = Path.cwd()
cogs_dir = current_directory.joinpath("cogs")
################################ CLIENT VARIABLES #################################
# client = MyClient(intents=intents, guild=MY_GUILD) # initialize the client bot

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['>?', 'lol ', '!?']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

client = Bot_with_javis(command_prefix=get_prefix, intents=intents)

# Loading cogs module

async def loading():
    if cogs_dir.is_dir():
        # List all .py files in the directory
        python_files = list(cogs_dir.glob('*.py'))

        # Print the names of the .py files
        for file in python_files:
            await client.load_extension(f'cogs.{file.name[:-3]}')  # Just print the file name
    else:
        print(f"The specified path {cogs_dir} is not a valid directory.")
    

async def main():
    # async with client:
    await loading()

asyncio.run(main())
client.run(TOKEN)