# from src.shovel_class import shovel
# import discord
# from discord.ext import commands
# import asyncio
# from itertools import cycle


TOKEN = ''

# intents = discord.Intents.default()
# client = commands.Bot(command_prefix='.', intents=intents)
# class_codes = [123, 456, 678]
# async def check_class_status():
#     await client.wait_until_ready()

#     while not client.is_closed:

#         for i in class_codes:
#             print(i)

#         await asyncio.sleep(3)

# @client.event
# async def on_ready():
#     print('Bot is ready.')

# async def main():
#     async with client:
#         client.loop.create_task(check_class_status())
#         await client.start(TOKEN)

# if __name__ == "__main__":
#     asyncio.run(main())

# # 1088998577986097257
# # 1088998577986097257


import asyncio
import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.typing = True
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

async def background_task():
    while True:
        # do some background task here
        print("cooll")
        await asyncio.sleep(10) # wait for 60 seconds before running again

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(background_task())

@client.command()
async def hello(ctx):
    print("excuted")
    await ctx.send('Hello, world')

@client.listen()
async def on_message(message):
        print(f"{message.author}: {message.content}")
# Add your bot token here
client.run(TOKEN)
