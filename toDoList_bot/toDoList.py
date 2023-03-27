#MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8
import discord, asyncio, os 
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime, timedelta
import random
import re
import emoji
#git check
TOKEN = 'MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8'

intents = discord.Intents.all()
game = discord.Game("Let's help")

bot = commands.Bot(command_prefix='?', status=discord.Status.online, activity=game, intents=intents)
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
bot.run(TOKEN)