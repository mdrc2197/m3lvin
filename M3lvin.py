Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "?")


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    if message.content == "Hi M3lvin":
        await client.send_message(message.channel, "Hi!")

client.run("NDc1OTA4NDgwOTQzNzgzOTM2.Dkpr4A.bVOYlNhOvBEsNXCLQSERrBCOVnc")
