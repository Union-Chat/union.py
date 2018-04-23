.. unionchat documentation master file, created by
   sphinx-quickstart on Mon Apr 23 01:42:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to unionchat's documentation!
=====================================


Contents
=======

.. toctree::
   :maxdepth: 2

   reference





Indices and tables
==================

* :ref:`search`

Example
=======
.. code-block:: python

   import union

   client = union.Client(username='Test', password = 'Test')

   @client.event.on('ready')
   async def ready():
     print('Union client loaded')

    @client.event.on('message')
    async def on_message(msg):
     if msg.content.lower() == '!hi':
       await msg.reply('Oh hi there {}'.format(msg.author))

   client.start()
