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

## Events

Capturing events

Use the @client.event.on() decorator

Types:

* 'message', emitted when a new message is sent
* 'ready', emitted when the client has connected
* 'bad_request', emitted when there was a server side error processing the request
* 'presence_change', emitted when someone goes online or offline
* 'message_delete', emitted when a message is deleted
* 'member_join', emitted when a member is added or removed (I think, I haven't had the chance to test yet)

## Functions

```python
# Client methods
await create_message(server, content) # Makes a new message, returns Message object
get_message(id) # Get a message by ID
await delete_message(id) # Delete a message by ID, only works on your own messages
get_member_info(server, id) # Get a member by server and ID

# Message methods
await reply(content) # Replies to a message, return Message object, shorthand for create_message()
await delete() # Deletes message, only works on your own messages
await send(content) # Alias of reply

# Server methods
get_member(id) # Gets a member from a server


