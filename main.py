#Discord-bot-by-yourself...

import discord

Token = "MTMxMjYzNDkyMDQwOTEwNDQ3NQ.Gw8rth.3thEAnqN7vkQkdc6z07f7hcov0i5PQ00lJNkFQ"
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} でログインしました。')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(Token)