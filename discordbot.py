from discord.ext import commands
import os
import traceback

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

random_content=[magnam, magnam, magnam, "ふわふわ"]
    
@client.event
async def on_message(message):
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    # メッセージの本文が 鳴いて だった場合
    if message.content == "gacha":
        # 送信するメッセージをランダムで決める
        content = random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)
    elif message.content == "おはよう":
        await message.channel.send("おはよう！！")


bot.run(token)
