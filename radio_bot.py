import discord
from discord.ext import commands
import os

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
    # fallback robust, în caz că ctx.voice_client e None
    voice_client = ctx.guild.voice_client or discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice_client and voice_client.is_connected():
        radio_url = "https://asculta.radiomanele.ro:8000/"
        voice_client.stop()
        voice_client.play(discord.FFmpegPCMAudio(radio_url), after=lambda e: print('🎵 Redarea s-a încheiat.'))
        await ctx.send("▶️ Redau Radio Manele LIVE! 🔊💥")
    else:
        await ctx.send("❌ Costel nu e conectat în voice. Scrie `!haiCostele` mai întâi.")


@bot.command(name="taciCostele")
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⏹️ Costel a ieșit din voice. Gata cu petrecerea.")
    else:
        await ctx.send("Nu sunt conectat.")
        
bot.run(os.getenv("TOKEN"))
