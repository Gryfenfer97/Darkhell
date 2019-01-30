#!Python-3.6.8/python

import discord
import asyncio
import random
import crypter

client = discord.Client()


def rps(choice):
    message = " {0} {1}"
    paper_emo = ":page_facing_up:"
    rock_emo = ":moyai:"
    scissor_emo = ":scissors:"
    if choice == "rock"  or choice == "scissors" or choice == "paper":
        r = random.randrange(0,3)
        if r == 0: #rock
            if choice == "rock":
                return message.format(rock_emo,"we're square")
            elif choice == "paper":
                return message.format(rock_emo,"you win")
            else:
                return message.format(rock_emo,"you lost")
        elif r == 1: #paper
            if choice == "rock":
                return message.format(paper_emo,"you lost")
            elif choice == "paper":
                return message.format(paper_emo,"we're square")
            else:
                return message.format(paper_emo,"you win")
        if r == 2: #scissors
            if choice == "rock":
                return message.format(scissor_emo,"you win")
            elif choice == "paper":
                return message.format(scissor_emo,"you lost")
            else:
                return message.format(scissor_emo,"we're square")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!rps'):
        await client.send_message(message.channel, message.author.mention + rps(message.content.split(' ')[1]))

    elif message.content.startswith('!encrypt'):
        command_splitted = message.content.split(' ')
        if command_splitted[1] == 'cesar':
            await client.send_message(message_channel,crypter.caesar(True,message.content.split("```")[1],command_splitted[2]))

client.run("NDUyODkyNzM3NzA0ODIwNzM2.DyK26g._0ro1jfWgL5tt1-24tFFhJxwQbk")