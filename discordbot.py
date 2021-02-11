from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(self, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await self.send(error_msg)
    
@bot.event
async def on_message(self, message):
    s = message.content.split(' ')
    author = message.author
    try:
        if not s[0] in self.forbidden_commands_per_phase[self.phase]:
            gen = self.commands[s[0]](s[1:], author)
            if gen is not None:
                for mem, mes in gen:
                    await self.send_message(self.createDest(mem), mes)
    except KeyError:
        pass

@bot.command()
async def neko(self):
    await self.send('にゃーん')

@bot.command()
async def Neko(self, *args):
    for arg in args:
        argnya = arg + 'にゃーん'
        await self.send(argnya)

@bot.command()
async def molcar(self):
    await self.send('pui pui')

@bot.command()
async def ping(self):
    random_contents = ['magnam', 'magnam', 'magnam', 'magnam', 'ふわふわ', 'pong', 'pong']
    content = random.choice(random_contents)
    await self.send(content)

bot.run(token)
