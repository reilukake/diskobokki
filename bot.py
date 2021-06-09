import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv()
token = getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.load_extension('commands_simple')
bot.load_extension('commands_intent')
bot.load_extension('commands_embed')

bot.run(token)