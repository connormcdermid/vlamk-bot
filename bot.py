#!/usr/bin/env python3

# A simple Python Discord bot
import os
import re  # regexes
import discord  # discord.py API wrapper
from dotenv import load_dotenv  # Allows confidentiality of discord token

load_dotenv()

_TOKEN = os.getenv('DISCORD_TOKEN')  # Confidential -- DO NOT MAKE PUBLIC AND DO NOT FUCK WITH

client = discord.Client()

valm_regex = re.compile(r'valm[ie]*k', re.I)
@client.event
async def on_ready():
    print(f'{client.user} has established a connection to Discord')
    print(f'{client.user} has established a connection to the following guilds: ')
    for guild in client.guilds:
        print(f'{guild.name}(id: {guild.id})')
        for channel in guild.channels:
            print(f'{channel.name}')


@client.event
async def on_message(message):
    if 'vlamk' in message.content or 'valmik' in message.content or valm_regex.match(message.content):
        print(f'Reference to Valmik found in message {message.id}')
        try:
            await message.channel.send("***I sense that a great name of power has been invoked. The name of...***")
        except discord.Forbidden:
            print(f'Failed to send reply to message {message.id} -- incorrect permissions')
        except discord.NotFound:
            print(f'Message {message.id} not found -- perhaps it was deleted?')
        except discord.HTTPException:
            print(f'Client failed to reach Discord.')
        finally:
            print(f'Message {message.id} replied to.')
            await message.channel.send("***VALMEEEEEEEEEK***")




client.run(_TOKEN)
