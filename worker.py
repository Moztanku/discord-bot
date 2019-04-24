import discord
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print("Gotowy do pracy 6")
@client.event
async def on_message(message):
    if 'nigger' in message.content.lower() or 'nigga' in message.content.lower():
        if "569979207292157984" not in [role.id for role in message.author.roles]:
            await message.delete()
            await message.channel.send( message.author.mention+" nie masz N-Word Passa, proszę nie używać słowa \"ni\*\*er\".")
    if 'spermiarz' in message.content.lower():
        if "569979214858551298" not in [role.id for role in message.author.roles]:
            await message.delete()
            await message.channel.send( message.author.mention+" nie masz S-Word Passa, proszę nie używać słowa \"sp\*\*\*\*\*rz\".")
client.run("NTAzNTY0ODMzMzU1MjAyNTcz.Dq4YRA.9MLbFuNBjL6ZjnNHJXvWwPH9Ffw")
