import union
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

username = config['settings']['username']
password = config['settings']['password']
client = union.Client(username=username, password=password)


@client.ee.on('ready')
async def ready():
    print('{} logged in'.format(username))


@client.ee.on('message')
async def on_message(msg):
    if msg.content.lower() == '!hi':
        await msg.reply('Oh hi there {}'.format(msg.author))

client.start()
