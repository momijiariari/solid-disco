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
    if message.content == "!人狼": #ゲーム開始および役職設定のメッセージ
        if situation_number == 0:
            await message.channel.send("使用したい役職の絵文字を使用したい数リアクションしてください。\n役職およびその数を決定したら\n!役職決定\nとコマンドを送ってください。")
        situation_number+=1  #ゲームの進行度は1

        if situation_number >= 1: #進行度が１異常だったら!人狼を受け付けない
            await message.channel.send("そのコマンドは既に実行しています")

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
