# union.py

A python library for Kromatic's Union chatservice

## Requirements

* websockets
* json
* base64
* asyncio
* pyee

## Example

```python
import union

client = union.Client(username='Test', password = 'Test')

@client.ee.on('ready')
async def ready():
  print('Union client loaded')
  
 @client.ee.on('message')
 async def on_message(msg):
  if msg.content.lower() == '!hi':
    await msg.reply('Oh hi there {}'.format(msg.author))
    
client.start()
```
