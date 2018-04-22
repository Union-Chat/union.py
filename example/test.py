import unionchat

client = unionchat.Client(username='Test', password='Test')


@client.event.on('ready')
async def ready():
    print('Union client loaded')


@client.event.on('message')
async def on_message(msg):
    if msg.content.lower() == '!hi':
        await msg.reply('Oh hi there {}'.format(msg.author))


client.start()