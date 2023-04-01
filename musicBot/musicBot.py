import asyncio
from discord.ext import commands

TOKEN = 'MTA4MTA3OTYzMDYzMjU4NzMwNA.GXY-RO.1TE3a_pqwexb3qjK0VwIh-GDp98dLMW8fMXNL8'

client = commands.Bot(command_prefix='?')
songs = asyncio.Queue()
play_next_song = asyncio.Event()


async def audio_player():
    while True:
        play_next_song.clear()
        current = await songs.get()
        current.start()
        await play_next_song.wait()


def toggle():
    client.loop.call_soon_threadsafe(play_next_song.set)


@client.command(pass_context=True)
async def play(ctx, url):
    if not client.is_voice_connected(ctx.message.server):
        voice = await client.join_voice_channel(ctx.message.author.voice_channel)
    else:
        voice = client.voice_client_in(ctx.message.server)

    player = await voice.create_ytdl_player(url, after=toggle)
    await songs.put(player)

client.loop.create_task(audio_player())

client.run('token')