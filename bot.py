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
prefix = re.compile(r'^\$v')

taunts = [""]


@client.event
async def on_ready():
    print('{} has established a connection to Discord'.format(client.user))
    print('{} has established a connection to the following channels in the following guilds: '.format(client.user))
    for guild in client.guilds:
        print('{}(id: {})'.format(guild.name, guild.id))
        for channel in guild.channels:
            print('{}'.format(channel.name))


@client.event
async def on_message(message):
    if 'vlamk' in message.content or 'valmik' in message.content or valm_regex.match(message.content):
        print('Reference to Valmik found in message {} sent by {}'.format(message.id, message.author))
        try:
            await message.channel.send("***I sense that a great name of power has been invoked. The name of...***")
        except discord.Forbidden:
            print('Failed to send reply to message {} -- incorrect permissions'.format(message.id))
        except discord.NotFound:
            print('Message {} not found -- perhaps it was deleted?'.format(message.id))
        except discord.HTTPException:
            print('Client failed to reach Discord.')
        finally:
            print('Message {} replied to.'.format(message.id))
            await message.channel.send("***VALMEEEEEEEEEK***")
    elif prefix.match(message.content):
        if "report status" in message.content:
            await message.channel.send("Message replied to: {}\n".format(message.id)
                                       + "Current guild: {}\n".format(message.guild.name)
                                       + "Current channel: {}\n".format(message.channel.name))
            await message.channel.send("I can see the following channels:")
            for x in message.guild.channels:
                await message.channel.send(x.name)
            for x in client.guilds:
                await message.channel.send("Other guilds: {}".format(x.name))

            await message.channel.send("Thanks for asking, {}".format(message.author))
        elif "show channels" in message.content:
            if message.author == "Connor | CAM#6843":
                await message.channel.send("Why, certainly, sir.")
                for channel in message.guild.channels:
                    await message.channel.send(channel.name)
            elif message.author == "SevenSixTwo":
                await message.channel.send("fuck off")
                for channel in message.guild.channels:
                    await message.channel.send("Instead of saying what channel this is, i'm just going to taunt you.")

            else:
                await message.channel.send("No problem.")
                for channel in message.guild.channels:
                    await message.channel.send(channel.name)
        elif "play" in message.content:
            await message.channel.send("I'm not a music bot, dumbass. Get off my back.")
    elif "good bot" in message.content:
        await message.channel.send("Why thank you, {}".format(message.author))
    elif message.author == "MEE6#4876":
        await message.channel.send("Shut up inferior bot.")


client.run(_TOKEN)
