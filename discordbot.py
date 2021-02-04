from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
    
@bot.command()
async def molcar(ctx):
    await ctx.send('pui pui')
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#random_content=[magnam, magnam, magnam, "ふわふわ"]

bot.run(token)
