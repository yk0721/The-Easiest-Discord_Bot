#Discord-bot-by-yourself...
import discord
import configparser
from discord.ext import commands
from messages.return_messages import *

#load config.ini file
config_ini = configparser.ConfigParser()
config_ini.read('config.ini')
#get config_data
Token = config_ini['General']['Token']

#initialize discord_client
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='%', intents=intents)

#event on ready
@bot.event
async def on_ready():
    print(readyMsg(bot.user))

@bot.command()
async def hihi(cfx):
    await cfx.send("Hello")

#run client
bot.run(Token)