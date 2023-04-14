#MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8
import discord, asyncio, os 
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime, timedelta
import random
import re
import emoji
TOKEN = 'MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8'

intents = discord.Intents.all()
game = discord.Game("Let's help")

bot = commands.Bot(command_prefix='?', status=discord.Status.online, activity=game, intents=intents)

#examreminder
#////////////////////////////////////////////////////////////////////////////////////////////
exam_list = {}
#store the exam into exam list
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
        exam_list[exam] = {'due_date': datetime.strptime(due, '%Y-%m-%d %H:%M'), 'place': place}
        await ctx.channel.send(f"You have {exam} exam on {place} at {due}")
        now=datetime.now()
        then=datetime.strptime(due, '%Y-%m-%d %H:%M')
        oneh_before=int(then.hour-(timedelta(hours=1, minutes=0, seconds=0)/timedelta(hours=1)))
        newthen=then.replace(hour=oneh_before)
        wait_time=(newthen-now).total_seconds()
        print(newthen)
        print(now)
        print(oneh_before)
        print(wait_time)
        await asyncio.sleep(wait_time)
        
        await ctx.channel.send(f'One hour left before your {exam} exam on {place}!')
        
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
#////////////////////////////////////////////////////////////////////////////////////////////
#examreminder


#studyTimer
#////////////////////////////////////////////////////////////////////////////////////////////
@bot.listen('on_message')
async def studytimer(message):
    #channel = ctx.channel
    if message.content.startswith("studytimer"):
        #await message.channel.send('Please write how many minutes you want to set the timer. (In minutes!!)')
        #mins = message.content
        parts = message.content.split(':', maxsplit=1)
        mins = parts[0].split(' ', maxsplit=1)[1]
        secs = parts[1].strip() if len(parts) > 1 else ""

        await message.channel.send(f"Your timer is set to {mins}minutes {secs}seconds from now!")
        mins=int(mins)
        secs=int(secs)
        
        mins=mins*60
        await asyncio.sleep(mins+secs)

        await message.channel.send("Time is over!!!")
#////////////////////////////////////////////////////////////////////////////////////////////
#studyTimer

#toDoList
#////////////////////////////////////////////////////////////////////////////////////////////
todo_list={}
#save the name of task and due date into todo_list
#type: ?todo task/YYYY-MM-DD HH:MM
@bot.listen('on_message')
async def todosave(ctx):
    if ctx.content.startswith("todo"):
        parts = ctx.content.split('/', maxsplit=1)
        task = parts[0].split(' ', maxsplit=1)[1]
        due = parts[1].strip() if len(parts) > 1 else ""
        print(task)
        print(due)
        if not re.match(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}", due):
            await ctx.channel.send('Wrong format. Type in ?todo task/`YYYY-MM-DD HH:MM`')
            return
        todo_list[task] = due
        await ctx.channel.send(f"You have {task} due to {due}.")
             
#print the todo_list
# type: ?mylist
@bot.command()
async def mylist(ctx):
    list_print="Your list:\n"
    for key in todo_list:
        list_print+=key+" "
        list_print+=todo_list[key]+"\n"
    await ctx.send(list_print)

#add thumbs_up emoji in front of the task done
#type: check taskname
@bot.listen('on_message')
async def todoremove(ctx):
    if ctx.content.startswith("check"):
        parts = ctx.content.split('/', maxsplit=0)
        task = parts[0].split(' ', maxsplit=1)[1]
        list_print="Your list:\n"
        for key in todo_list:
            if key==task:
                list_print+=emoji.emojize(':thumbs_up:')+" "
            list_print+=key+" "
            list_print+=todo_list[key]+"\n"
        await ctx.channel.send(list_print)

#remove the task from the list
# type: remove taskname
@bot.listen('on_message')
async def todoremove(ctx):
    if ctx.content.startswith("remomve"):
        parts = ctx.content.split('/', maxsplit=0)
        task = parts[0].split(' ', maxsplit=1)[1]
        todo_list.pop(task, -1)
        list_print="Your list:\n"
        for key in todo_list:
            list_print+=key+" "
            list_print+=todo_list[key]+"\n"
        await ctx.channel.send(list_print)
#////////////////////////////////////////////////////////////////////////////////////////////
#toDoList

bot.run(TOKEN)