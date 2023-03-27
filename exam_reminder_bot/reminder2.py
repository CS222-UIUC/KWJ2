#MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8
import discord, asyncio, os 
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime, timedelta
import random
import re

TOKEN = 'MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8'

intents = discord.Intents.all()
game = discord.Game("Let's help")

bot = commands.Bot(command_prefix='?', status=discord.Status.online, activity=game, intents=intents)

exam_list = {}

@bot.command()
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}, I am a exam reminder bot')

@bot.command()
async def bye(ctx):
    await ctx.send(f'{ctx.author.mention}, See you again')

#store the exam into exam list
@bot.command()
@bot.listen('on_message')
async def examsave(ctx):
    if ctx.content.startswith("?exam"):
        parts = ctx.content.split('/', maxsplit=2)
        #print(parts[0].split(' ', maxsplit=1)[1])
        exam = parts[0].split(' ', maxsplit=1)[1]
        due = parts[1].strip() if len(parts) > 1 else ""
        place = parts[2].strip() if len(parts) > 2 else ""
        print(exam)
        print(due)
        print(place)
        if not re.match(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}", due):
            await ctx.channel.send('Wrong format. Type in !exam Exam/`YYYY-MM-DD HH:MM`/place.')
            return
        #exam_list[exam] = datetime.strptime(due, '%Y-%m-%d %H:%M')
        exam_list[exam] = {'due_date': datetime.strptime(due, '%Y-%m-%d %H:%M'), 'place': place}
        # print(datetime.strptime(due, '%Y-%m-%d %H:%M'))
        # print(exam_list.keys())
        # print(exam_list.values())
        await ctx.channel.send(f"You have {exam} exam on {place} at {due}")
        now=datetime.datetime.now()
        then=datetime.strptime(due, '%Y-%m-%d %H:%M')
        oneh_before=then.hour()-timedelta(hour=1)
        then.replace(hour=oneh_before)
        wait_time=(then-now).total_seconds()
        await asyncio.sleep(wait_time)
        
        await ctx.send(f'One hour left before your {exam} exam on {place}!')
        
#print the exam list
@bot.command()
async def myexams(ctx):
    await ctx.send(exam_list)
#list become empty again when the bot become offline
#start again when the bot is online

#testing if this logic works
@bot.command()
async def schedule_message(ctx):
    now=datetime.datetime.now()
    then=now.replace(hour=22, minute=53)
    wait_time=(then-now).total_seconds()
    await asyncio.sleep(wait_time)

    await ctx.send("Good morning!!")


bot.run(TOKEN)