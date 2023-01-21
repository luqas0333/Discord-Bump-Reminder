import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='bump')
async def bump(ctx):
    await ctx.send('Bump message will be sent in 2 hours')

     #Using asyncio.sleep to wait for 2 hours
    await asyncio.sleep(2*60*60)

    embed = discord.Embed(title="Bump", description="Vergesse nicht den Server zu bumpen!", color=0x333333)
    await ctx.send(embed=embed)

bot.run('#')
