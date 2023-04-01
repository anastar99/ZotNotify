from src.shovel_class import shovel
import asyncio
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = 'MTA4ODk5Mzg0NTM0MzE3ODc3Mg.GZqfwq.gzjHP229u726Zl8sFWBfnnZElj118AmMj1Vi6U'

intents = discord.Intents.default()
intents.typing = True
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

monitoring_classes = [1234, 4567, 8904]

def discord_msg(code_status):
     """
     Sends a message to the server if the class is now available
     otherwise does nothing
     """
     if code_status == 'Waitlist' or 'Open':
          return "Class is not closed any more gogogo"
     return None
     

def code_check(code):
     """
     Checks the status of the code, calls the msg function
     """
     code_status = shovel(code).check_status()
     discord_msg(code_status)

async def background_task():
    while True:
        # do some background task here
        for code in monitoring_classes:
             code_check(code)
        await asyncio.sleep(10) # wait for 60 seconds before running again

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(background_task())

@client.command()
async def add(ctx):
    code = ctx.message.content[5::]
    monitoring_classes.append(code)
    await ctx.send(f'Monitoring Class: {code}')

@client.listen()
async def on_message(message):
        print(f"{message.author}: {message.content}")
# Add your bot token here
client.run(TOKEN)
