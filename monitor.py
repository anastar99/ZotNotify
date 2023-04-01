import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from src.shovel_class import shovel
from src.msg_embeds import *

TOKEN = 'MTA4ODk5Mzg0NTM0MzE3ODc3Mg.GZqfwq.gzjHP229u726Zl8sFWBfnnZElj118AmMj1Vi6U'
CHANNEL_ID = 1088998577986097257


intents = discord.Intents.default()
intents.typing = True
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

monitoring_classes = []

async def discord_msg(code_status):
     """
     Sends a message to the server if the class is now available
     otherwise does nothing
     """
     channel = client.get_channel(CHANNEL_ID)
     print(code_status)
     if code_status == 'Waitl' or code_status == 'OPEN':
          await channel.send(embed=start_monitoring(3456))
          return True
     return False
     

async def code_check(code):
     """
     Checks the status of the code, calls the msg function
     """
     code_status = shovel(code).check_status()
     await discord_msg(code_status)

async def background_task():
    while True:
        # do some background task here
        for code in monitoring_classes:
             await code_check(code)
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

# @client.listen()
# async def on_message(message):
#         print(f"{message.author}: {message.content}")
client.run(TOKEN)
