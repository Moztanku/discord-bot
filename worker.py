import discord
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print("Ready to work")
@client.event
async def on_message(message):
    if '/*YOUR WORD*/' in message.content.lower() or '/*YOUR OTHER WORD*/' in message.content.lower():
        if not discord.utils.get(message.author.roles, name="/*REQUIRED RANK NAME*/"):
            await message.delete()
            await message.channel.send( message.author.mention+" cant say the \**\ word.")
    if '/*YOUR WORD*/' in message.content.lower():
        if not discord.utils.get(message.author.roles, name="/*REQUIRED RANK*/"):
            await message.delete()
            await message.channel.send( message.author.mention+" doesn't have a necessary rank to use \**\ word.")
