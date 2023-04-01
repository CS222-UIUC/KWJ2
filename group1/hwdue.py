import discord, asyncio, os
from discord.ext import commands
import datetime
import re
from collections import OrderedDict
import time
import requests
import random


api_key = 'aac486d22a195ee88dc4698525927457'
lat =   40.116
lon =  -88.243

saved_h = {}
saved_hw = {}
game = discord.Game("Studying")
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',status = discord.Status.online, activity = game, intents = intents)
vocab = {}

@client.command()
async def hi(ctx):
    await ctx.send("Hello, I am HWdue bot")
@client.command()
async def bye(ctx):
    await ctx.send("See you")
@client.listen('on_message')
async def hw_save(message):
    if message.content.startswith("savehw"):
        parts = message.content.split('/', maxsplit=1)
        print(parts[0].split(' ', maxsplit=1)[1])
        hw = parts[0].split(' ', maxsplit=1)[1]
        due = parts[1].strip() if len(parts) > 1 else ""
        print(hw)
        if not re.match(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}", due):
            await message.channel.send('Wrong format. Type in !hw Homework/`YYYY-MM-DD HH:MM`.')
            return
        saved_hw[hw] = datetime.datetime.strptime(due, '%Y-%m-%d %H:%M')
        saved_hw_sorted = OrderedDict(sorted(saved_hw.items(), key=lambda x: x[1]))
        saved_hw.clear()
        saved_hw.update(saved_hw_sorted)
        print(datetime.datetime.strptime(due, '%Y-%m-%d %H:%M'))
        print(saved_hw.keys())
        print(saved_hw.values())
        await message.channel.send(f"You have {hw} until {due}")
        
@client.listen('on_message')
async def due_calc_1(message):
    if message.content.startswith("todayhw"):
        now = datetime.datetime.now()
        #check = now.replace(hour = 23, minute = 2)
        #then = now + datetime.timedelta(days=1)
        #wait = (check-now).total_seconds()
        #wait = (then - now).total_seconds()
        print("works")
        for hw1, due1 in saved_hw.items():
            if now.date() == due1.date():
                print("check!")
                await message.channel.send(f"You have {hw1} until {due1}")

@client.listen('on_message')
async def due_calc_2(message):
    if message.content.startswith("weeklyhw"):
        now = datetime.datetime.now()
        #check = now.replace(hour = 23, minute = 2)
        #then = now + datetime.timedelta(days=1)
        #wait = (check-now).total_seconds()
        #wait = (then - now).total_seconds()
        print("works")
        for hw1, due1 in saved_hw.items():
            delta = due1 - now
            if delta.days >= 0 and delta.days <= 7:
                print("check!")
                await message.channel.send(f"You have {hw1} due on {due1.strftime('%A, %B %d')}")

@client.listen('on_message')
async def on_message(message):
    if message.content.startswith('stopwatch'):
        start_time = time.time() # Record the starting time of the stopwatch
        await message.channel.send("Stopwatch started. Type `!stop` to stop.") # Send a message indicating that the stopwatch has started

        # Keep the stopwatch running until the user types "!stop"
        while True:
            try:
                msg = await client.wait_for('message', timeout=1.0) # Wait for a message from the user
                if msg.content == '!stop':
                    end_time = time.time() # Record the ending time of the stopwatch
                    elapsed_time = round(end_time - start_time, 2) # Calculate the elapsed time in seconds
                    await message.channel.send(f"Stopwatch stopped. Elapsed time: {elapsed_time} seconds.") # Send a message with the elapsed time
                    break # Exit the loop and stop the stopwatch
                else:
                    current_time = time.time() - start_time # Calculate the current elapsed time
                    current_time_formatted = time.strftime("%H:%M:%S", time.gmtime(current_time)) # Format the current time as hours, minutes, and seconds
                    await message.channel.send(f"Elapsed time: {current_time_formatted}") # Send a message with the current elapsed time
            except asyncio.TimeoutError: # If no message is received for 1 second, continue the loop
                continue

@client.listen('on_message')
async def quiz(message):
    if message.author == client.user:
        return
    if message.content.startswith("addword"):
        _, word, meaning = message.content.split()
        vocab[word] = meaning
        await message.channel.send(f"{word} added.")

    if message.content.startswith("deleteword"):
        _, word = message.content.split()
        if word in vocab:
            del vocab[word]
            await message.channel.send(f"{word} deleted.")
        else:
            await message.channel.send(f"{word} does not exist.")

    if message.content.startswith("resetword"):
        vocab.clear()
        await message.channel.send("Vocab Reseted.")
    if message.content.startswith("wordquiz"):
        if not vocab:
            await message.channel.send("Save your words to start quiz.")
            return
        words = list(vocab.keys())
        random.shuffle(words)
        for word in words:
            meaning = vocab[word]

            await message.channel.send(f"{meaning}?")

            def check(m):
                return m.author == message.author and m.channel == message.channel

            try:
                response = await client.wait_for("message", check=check, timeout=10.0)
            except asyncio.TimeoutError:
                await message.channel.send(f"Time up! Answer:{word}")
            else:
                if response.content.lower() == word.lower():
                    await message.channel.send("Bingo!")
                else:
                    await message.channel.send(f"Wrong! Answer:{word}")

@client.listen('on_message')
async def weather(message):
    # 3/31: this wather command did not function till Friday
    # We will ask the TA on how to fix this issue
    # We are currently struggling with implementing any API

    # Check if the message starts with the weather command
    if message.content.startswith('weather'):
        # Make a GET request to the OpenWeatherMap API
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
        print(response.json())
        # Extract the temperature from the JSON response
        #temperature = response.json()['main']['temp']

        # Send a message to the Discord channel with the temperature
        #await message.channel.send(f'The temperature in Chmapaign is {temperature} degrees Celsius.')

        # this is for testing purposes

# We are planning on adding other API after this weather functionality
# we are planning on improving the quiz function using an API and I am still searching for tools to impliment this



@client.event
async def on_ready():
    print("You can now use your bot")
#testtesttest
client.run('MTA4MDM0MDk3MTg5MzU3MTYyNg.GGLmpu.Egpyv3q5-ICjr9DU5eh8BFSKmw001IkDNxNwDY')