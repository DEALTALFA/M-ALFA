import os

import discord
TOKEN = 'NzQ1NTExMTA5NzIwNjcwMjY5.Xzy1Uw.c1O6tRZxtyi2wFJuAbvB17ayIGc'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event     
async def on_message(message):
    if message.author==client.user:
        return
    if 'happy birthday' in message.content.lower():
       await message.channel.send("happy bithday 🎉")
client.run(TOKEN)