# union.py

A python library for Kromatic's Union chatservice.
Current version: 0.0.7

## Installation

`pip3 install unionchat`

## Requirements

* websockets
* pyee
* aiohttp

## Example

```python
import unionchat

client = unionchat.Client(username='Test', password = 'Test')

@client.event.on('ready')
async def ready():
  print('Union client loaded')
  
 @client.event.on('message')
 async def on_message(msg):
  if msg.content.lower() == '!hi':
    await msg.reply('Oh hi there {}'.format(msg.author))
    
client.start()
```

## Documentation

Find it [here](http://unionchat.readthedocs.io/en/latest/reference.html)


