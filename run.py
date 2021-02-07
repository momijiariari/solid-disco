from dowClient import dowClient

token = os.environ['DISCORD_BOT_TOKEN']
client = dowClient()

with open('./key', 'r') as f:
    key = f.read()

client.run(token)
#key[0:-1]
