# A simple Python Discord bot
import os

import discord
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')  # Confidential -- DO NOT MAKE PUBLIC

client = discord.Client()

@client.event
async def on_ready():
    print("Client has established connection to Discord.")
