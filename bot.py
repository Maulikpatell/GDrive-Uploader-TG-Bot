from pyrogram import Client
from config import Config


plugins = dict(root="plugins")


app = Client('GDrive-Bot',
        bot_token = Config.5098914599:AAGSBT8sJvL8AFQN9i1VWReGrJnkLkIbueQ,
        api_id = Config.16602377,
        api_hash = Config.6766d1e1d9fdddf7e06171829958bfad,
        plugins = plugins
      )


app.run()
