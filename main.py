import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

# DIFFERENT TYPE
#client = discord.Client()
client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
  print('Logged {0.user}'.format(client))

# FROM DIFFERENT TYPE
#@client.event
#async def on_message(message):
  #if message.author == client:
  #  return
  #if message.content.startswith('$Hello'):
  #  await message.channel.send('Hi')

@client.command()
async def play(ctx, url : str):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  await voiceChannel.connect()


keep_alive()
client.run(os.getenv('TOKEN'))