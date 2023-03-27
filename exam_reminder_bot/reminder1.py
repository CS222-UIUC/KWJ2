import discord
from discord.ext import commands
from asyncio import sleep as s

client = commands.AutoShardedBot(commands.when_mentioned_or('!'), help_command=None)

@client.commnds()
async def reminder(ctx, time: int, *, msg):
    while True:
        await s(time)
        await ctx.send(f'{msg}, {ctx.author.mention}')
