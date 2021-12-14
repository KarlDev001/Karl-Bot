import os
import json
import discord
from discord.ext import commands

with open('config.json') as json_file:
    data = json.load(json_file)

prefix = data["prefix"]
bot_token = data["token"]

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print(f'{client.user} is online.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(bot_token)
