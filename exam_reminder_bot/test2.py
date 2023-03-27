import discord, asyncio, os 
from discord.ext import commands
game = discord.Game("Primary Bot")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', status=discord.Status.online, activity=game, intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}, Nice to meet you!')

bot.run('MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8')