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

## Events

Capturing events

Use the @client.ee.on() decorator

Types:

* 'message', emitted when a new message is sent
* 'ready', emitted when the client has connected
* 'bad_request', emitted when there was a server side error processing the request
* 'presence_change', emitted when someone goes online or offline
* 'message_delete', emitted when a message is deleted
* 'member_join', emitted when a member is added or removed (I think, I haven't had the chance to test yet)
