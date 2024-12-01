#Discord-bot-by-yourself...

import discord
import configparser

#load config.ini file
config_ini = configparser.ConfigParser()
config_ini.read('config.ini')
#get config_data
Token = config_ini['General']['Token']

#initialize discord_client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#event on ready
@client.event
async def on_ready():
    print(f'{client.user} でログインしました。')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
#run client
client.run(Token)