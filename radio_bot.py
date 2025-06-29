import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Botul e conectat ca {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("🎧 M-am conectat în voice.")
    else:
        await ctx.send("Trebuie să fii într-un voice channel.")

@bot.command()
async def play(ctx):
    if ctx.voice_client:
        radio_url = "https://asculta.radiomanele.ro:8000/"
        ctx.voice_client.stop()
        ctx.voice_client.play(discord.FFmpegPCMAudio(radio_url), after=lambda e: print('🎵 Redarea s-a încheiat.'))
        await ctx.send("▶️ Redau Radio Manele LIVE!")
    else:
        await ctx.send("Nu sunt într-un voice channel. Scrie `!join` mai întâi.")

@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⏹️ M-am deconectat.")
    else:
        await ctx.send("Nu sunt conectat.")

bot.run("MTM4ODkxMTkwMjEwODY4NDQzOQ.GBktmt.DLi2Aked_9fQ4H8yCllnrp6D7ZFzVe4AITZfUw")
