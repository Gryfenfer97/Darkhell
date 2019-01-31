#!Python-3.6.8/python

import discord
import asyncio
import random
import crypter
import json
from discord.ext import commands
import games
from miscellaneous import *


def _prefix_callable(bot, message):
    base = [f'<@!{bot.user.id}> ', f'<@{bot.user.id}> ', bot.config['prefix']]
    return base

description = ""


class Darkhell(commands.Bot):
    def __init__(self, config):
        super().__init__(command_prefix=_prefix_callable)
        self.config = config

    
    async def on_ready(self):
        print('Logged in as {}'.format(self.user.name))
        #print(self.user.id)
        print('------')
        await self.change_presence(game=discord.Game(name=self.config['informations']['status']))


    async def on_message(self,message):
        if message.content.startswith('!test'):
            counter = 0
            tmp = await self.send_message(message.channel, 'Calculating messages...')
            async for log in self.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await self.edit_message(tmp, 'You have {} messages.'.format(counter))
        elif message.content.startswith('!sleep'):
            await asyncio.sleep(5)
            await self.send_message(message.channel, 'Done sleeping')

        elif message.content.startswith('!rps'):
            await self.send_message(message.channel, message.author.mention + games.rps(message.content.split(' ')[1]))

        elif message.content.startswith('!year_progress'):
            await self.send_message(message.channel, year_progress())

        elif message.content.startswith('!encrypt'):
            command_splitted = message.content.split(' ')
            if command_splitted[1] == 'cesar':
                await self.send_message(message.channel,crypter.caesar(True,message.content.split("```")[1],command_splitted[2]))

        elif message.content.startswith('!decrypt'):
            command_splitted = message.content.split(' ')
            if command_splitted[1] == 'cesar':
                await self.send_message(message.channel,crypter.caesar(False,message.content.split("```")[1],command_splitted[2]))

    def run(self, token):
        super().run(token, reconnect=True)


#client.run("NDUyODkyNzM3NzA0ODIwNzM2.DyK26g._0ro1jfWgL5tt1-24tFFhJxwQbk")