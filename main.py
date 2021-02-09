import discord
import os
import requests
import json

client = discord.Client()



@client.event
async def on_ready():
  print('Logged {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client:
    return
  
  if message.content.startswith('$Hello'):
    await message.channel.send('Hi')

client.run(os.getenv('TOKEN'))