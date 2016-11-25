import discord
import logging


# Setup Logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# Bot Class
class Bot(discord.Client):
    def __start_bot(self):
        super().run(self.tk)

    def __init__(self, token):
        super().__init__()
        self.tk = token
        self.pf = "?!"

    async def on_message(self, msg):
        pass
