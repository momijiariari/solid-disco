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

@bot.event
async def on_message(message):
    if message.content == "あ":
        await message.channel.send("ああ")

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.command()
async def Neko(ctx, *args):
    for arg in args:
        argnya = arg + 'にゃーん'
        await ctx.send(argnya)

@bot.command()
async def molcar(ctx):
    await ctx.send('pui pui')

@bot.command()
async def ping(ctx):
    random_contents = ['magnam', 'magnam', 'magnam', 'magnam', 'ふわふわ', 'pong', 'pong']
    content = random.choice(random_contents)
    await ctx.send(content)

bot.run(token)
