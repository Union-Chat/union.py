Reference
=========
This explains how to use unionchat

Client
^^^^^^


.. py:class:: unionchat.Client(username, password, **)
Instances a client to connect to Union.
You can pass some options to Client.

**Parameters**

* loop(Optional) - Pass an asyncio event loop
* cache_size(Optional[int]) - The maximum number of messages to store in the message cache. This defaults to 500. Anything lower than 100 will use the default value.

.. py:attribute:: user

Object[SelfUser] - Simple user that contains password and username

.. py:attribute:: ready

Bool: Indicates whether client has finished connecting or not.

.. py:attribute:: loop

The event loop for the websocket and HTTP requests

.. py:attribute:: servers

Dict[Server] - The servers that the client can see.

.. py:attribute:: api

An instance of aiohttp ClientSession

.. py:function:: start()

Blocking call that runs the event loop so you don't have to create it yourself.

This function must always be called last.

.. py:function:: coroutine create_message(server, content)

This function is a coroutine

Sends a message to a Union server

.. py:function:: coroutine send_message(server, content)

This function is a coroutine

This is an alias of create_message(server, content)

.. py:function:: coroutine delete_message(id)

Deletes a message

You cannot delete messages send by others

.. py:function:: get_message(id)

Returns a Message

.. py:function:: get_member_info(id)

Returns a Member

Union Objects
^^^^^^^^^^^^^

Member
******
.. py:class:: unionchat.Member()

Represents a Union member. You normally don't have to create one of these yourself.
Members don't have ID's, their names are used internally.

.. py:attribute:: avatar_url

str - Returns the avatar url of the member

.. py:attribute:: created_at

timestamp - Returns the creation data of the member

.. py:attribute:: status
bool - Indicates whether a member is online or offline

.. py:function:: str(member)

Returns the member's name

.. py:function:: mention()
str - Returns a preformatted mention

Message
*******
.. py:class:: unionchat.Message()

Represents a Union message. You normally don't have to create one of these yourself.

.. py:attribute:: client

The client used, you usually don't use this.

.. py:attribute:: server

int - The server the message originates from.

.. py:attribute:: author

Object[Member] - Returns a member of the message author.

.. py:attribute:: content

str - Returns the message content.

.. py:attribute:: id

str - Returns the message id

.. py:attribute:: created_at

int - Unix timestamp from when the message was created

.. py:attribute:: self

Object[Member] - Only available when the client sent the message

.. py:function:: str(Message)

str - Returns message content

.. py:function:: coroutine reply(content)

Replies to a message

Returns Message of the message that was sent

.. py:function:: coroutine send(content)

Alias of reply(content)

.. py:cofunction:: coroutine delete()

Deletes the message.

You cannot delete messages sent by others

Server
******
.. py:class:: unionchat.Server()
Represents a Union server

.. py:attribute:: name

str - Returns the server name

.. py:attribute:: id

int - Returns the server ID

.. py:attribute:: messages

list - Returns the messages in the server by id

.. py:attribute:: icon_url

str - Returns the server's icon url

.. py:attribute:: members

dict - Returns the members in the server

.. py:method:: get_member(id)

Get a member by ID

SelfUser
********
.. py:class:: unionchat.SelfUser()

Denotes the client user properties

.. py:attribute:: password

Returns the password used to login

**YOU SHOULD ALWAYS KEEP THIS PRIVATE**

.. py:attribute:: username

Returns the username used to login

Exceptions
^^^^^^^^^

.. py:exception:: CannotDeleteOtherMessages

Raised when you attempt to delete a message that was not send by you

.. py:exception:: UsernameMustExist

Raised when you do not include a username when creating a Client.

.. py:exception:: PasswordMustExist

Raised when you do not include a password when creating a Client.

.. py:exception:: NotReadyYet

Raised when the client has not connected yet








