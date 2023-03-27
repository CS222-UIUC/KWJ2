# import discord
# from discord.ext import commands
# intents = discord.Intents.default()
# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_ready():
#     print("Start the bot.")

# @bot.command()
# async def hi(ctx):
#     await ctx.send('Hello')

# bot.run('MTA3OTk0MTY0ODEwMTkzNzI1NA.GlOUeC.y0nKhtfVa2a_Mq6RdGBZNbe4Y20E2SLrEu7oCA')
#-------------------------------------------------------------------------
# import discord, asyncio, os
# from discord.ext import commands

# game = discord.Game("Primary Bot")
# bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity=game)

# bot.run('MTA3OTk0MTY0ODEwMTkzNzI1NA.GlOUeC.y0nKhtfVa2a_Mq6RdGBZNbe4Y20E2SLrEu7oCA')
#-------------------------------------------------------------------------
# import discord
# from discord.ext.commands import Bot

# TOKEN = 'MTA3OTk0MTY0ODEwMTkzNzI1NA.GlOUeC.y0nKhtfVa2a_Mq6RdGBZNbe4Y20E2SLrEu7oCA'

# intents = discord.Intents.default()

# # ! means command
# bot = Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_ready():
#   print(f'logged in as {bot.user}')

# # !hello 
# @bot.command()
# async def hello(ctx):
#   await ctx.reply('Hi, there!')

# # !bye 
# @bot.command()
# async def bye(ctx):
#   await ctx.reply('See you later!')

# bot.run(TOKEN)

#-------------------------------------------------------------------------
# import discord
# from discord.ext import tasks

# TOKEN = 'MTA3OTk0MTY0ODEwMTkzNzI1NA.GlOUeC.y0nKhtfVa2a_Mq6RdGBZNbe4Y20E2SLrEu7oCA'
# CHANNEL_ID = '내 채널 ID'

# client = discord.Client()

# @client.event
# async def on_ready():
#     send_msg.start()

#     print("Hi, logged in as")
#     print(client.user.name)
#     print()

# @tasks.loop(minutes = 5)
# async def send_msg():
#     channel = client.get_channel(CHANNEL_ID)
#     await channel.send('Hello')

# client.run(TOKEN)

#-------------------------------------------------------------------------
import discord
from discord.ext.commands import Bot

TOKEN = 'MTA3OTk0MTY0ODEwMTkzNzI1NA.GlOUeC.y0nKhtfVa2a_Mq6RdGBZNbe4Y20E2SLrEu7oCA'

intents = discord.Intents.default()

# ! means command
bot = Bot(command_prefix='!', intents=intents)

bot.run(TOKEN)