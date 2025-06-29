import discord
from discord.ext import commands
import os
import random  # adaugă și importul random

RADIO_STREAMS = [
    "https://live.myradioonline.ro:8443/radio1manele.mp3",
    "https://live.myradioonline.ro:8443/fmradiomanele.mp3",
    "https://live.myradioonline.ro:8443/manelev.mp3",
    "https://live.myradioonline.ro:8443/radiopromanele.mp3"
]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Botul e conectat ca {bot.user}")

@bot.command(name="haiCostele")
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("🎧 M-am conectat în voice, frățioare.")
    else:
        await ctx.send("Trebuie să fii într-un voice channel.")

@bot.command(name="cantaCostele")
async def play(ctx):
    voice_client = ctx.guild.voice_client or discord.utils.get(bot.voice_clients, guild=ctx.guild)
    
    try:
        radio_url = "https://asculta.radiomanele.ro:8000/"
        voice_client.stop()
        voice_client.play(discord.FFmpegPCMAudio(radio_url), after=lambda e: print('🎵 Redarea s-a încheiat.'))
        await ctx.send("▶️ Redau Radio Manele LIVE! 🔊💥")
    except Exception as e:
        print(f"Eroare la redare: {e}")
        await ctx.send("❌ Costel nu poate cânta acum. Încearcă `!haiCostele` din nou.")


@bot.command(name="taciCostele")
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⏹️ Costel a ieșit din voice. Gata cu petrecerea.")
    else:
        await ctx.send("Nu sunt conectat.")
        
@bot.command(name="skipCostele")
async def skip(ctx):
    voice_client = ctx.guild.voice_client or discord.utils.get(bot.voice_clients, guild=ctx.guild)
    
    try:
        radio_url = random.choice(RADIO_STREAMS)
        voice_client.stop()
        voice_client.play(discord.FFmpegPCMAudio(radio_url), after=lambda e: print('🔁 Skip terminat'))
        await ctx.send(f"🔁 Costel a schimbat melodia! Acum ascultăm: `{radio_url}`")
    except Exception as e:
        print(f"Eroare la skip: {e}")
        await ctx.send("❌ Costel nu poate sări acum. Verifică dacă e în voice (`!haiCostele`).")
        
        
bot.run(os.getenv("TOKEN"))
