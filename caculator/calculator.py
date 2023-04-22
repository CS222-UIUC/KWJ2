# @client.command() 
# async def add(ctx, *nums):
#     operation = " + ".join(nums)
#     await ctx.send(f'{operation} = {eval(operation)}')

# @client.command() 
# async def sub(ctx, *nums): 
#     operation = " - ".join(nums)
#     await ctx.send(f'{operation} = {eval(operation)}')

# @client.command() 
# async def multiply(ctx, *nums): 
#     operation = " * ".join(nums)
#     await ctx.send(f'{operation} = {eval(operation)}')

# @client.command() 
# async def divide(ctx, *nums): 
#     operation = " / ".join(nums)
#     await ctx.send(f'{operation} = {eval(operation)}')

# @client.command()
# async def calculate(ctx, operation, *nums):
#     if operation not in ['+', '-', '*', '/']
#         await ctx.send('Please type a valid operation type.')
#     var = f' {operation} '.join(nums)
#     await ctx.send(f'{var} = {eval(var)}')

# @client.command()
# async def calc(ctx, operation:str):
#   await ctx.send(eval(operation))

#MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8
import discord, asyncio, os 
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime, timedelta
import random
import re
import math
#git check
TOKEN = 'MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8'

intents = discord.Intents.all()
game = discord.Game("Let's help")

bot = commands.Bot(command_prefix='?', status=discord.Status.online, activity=game, intents=intents)

@bot.listen('on_message')
async def calculator(message):
    #channel = ctx.channel
    if message.content.startswith("math"):
        parts = message.content.split()
        print(parts)
        first = parts[1].strip() if len(parts) > 1 else ""
        operator = parts[2].strip() if len(parts) > 2 else ""
        second = parts[3].strip() if len(parts) > 3 else ""

        first=int(first)
        second=int(second)

        if operator=='+':
            await message.channel.send(first+second)
        elif operator=='-':
            await message.channel.send(first-second)
        elif operator=='*':
            await message.channel.send(first*second)
        elif operator=='/':
            await message.channel.send(first/second)
        elif operator=='^' or operator=='**':
            await message.channel.send(first**second)
        elif operator=='%':
            await message.channel.send(first%second)
        else:
            await message.channel.send("You can only use +,-,*,/,^,%. Please try again with format math 1 + 2")

    elif message.content.startswith("trig"):
        parts = message.content.split()
        print(parts)
        operator = parts[1].strip() if len(parts) > 1 else ""
        num = parts[2].strip() if len(parts) > 2 else ""
        num=float(num)
        if operator=='sin':
            await message.channel.send(math.sin(num))
        elif operator=='cos':
            await message.channel.send(math.cos(num))
        elif operator=='tan':
            await message.channel.send(math.tan(num))
        else:
            await message.channel.send("You can only use cos, sin, tan. Please try again with format trig cos 3.14")

bot.run(TOKEN)