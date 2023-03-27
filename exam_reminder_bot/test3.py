#new bot
import discord
from discord.ext import commands
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
# @bot.command()
# async def hihello(message):
#     await message.channel.send('Hi!')
@client.event


async def on_message(message):
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))

# 봇이 "테스트"라는 유저의 메세지를 감지하면 Hello라고 답합니다.
 
bot.run('MTA4MTA3OTYzMDYzMjU4NzMwNA.Gwp6Gf.8SoIBCbFhc8CawzxyHhowxD5cIExuKJhJsb5L8')