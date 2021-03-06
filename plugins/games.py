import discord
import asyncio
import os, datetime, time, base64
from random import randint, SystemRandom
from bot_command import *

async def coinflip(message, args, author, client) :
    if SystemRandom().randint(0, 1) == 1 :
        await message.channel.send('Heads!')
    else :
        await message.channel.send('Tails!')

async def roulette(message, args, author, client) :
    
    if message.author.voice != None :
        uChannel = message.author.voice.channel
        if SystemRandom().randint(0, 5) == 5 :
            await message.author.move_to(None)
            await message.channel.send(':boom:')
        else :
            await message.channel.send('Click')
    else :
        await message.channel.send('You must be in a voice channel to play')

async def leaderboard(message, args, author, client) :
    # print full leaderboard
    point_dict = client.settings.get_data_val('user_points')
    if point_dict == None :
        await message.channel.send('No one has any updoots yet! Get updoots by being smart! :thinking:')
        return
    points = sorted(point_dict.items(), key = lambda kv:(kv[1], kv[0]))[::-1]
    print(points)
    # 32 is magic number because why not?
    lines = [message.guild.get_member(points[n][0]).display_name.ljust(32) + str(points[n][1]).rjust(10) for n in range(0, len(points))]
    to_send = '```\n' + '\n'.join(lines) + '\n```'
    await message.channel.send(to_send)

async def points(message, args, author, client) :
    points = client.settings.get_data_val('user_points')
    if points == None or not author.id in points.keys() :
        #hardcoded instructions /shrug
        await message.channel.send("You have no updoots! Get updoots by being smart! :thinking:")
        return
    await message.channel.send(author.display_name + ', you have ' + str(points[author.id]) + ' updoot' + ('s!' if points[author.id] != 1 else '!' ))




game_cmds = [
	bot_cmd("flip", coinflip, 1, 'Flip a coin with cryptographically secure randomness!'),
    bot_cmd("roulette", roulette, 1, 'Test your luck!'),
    bot_cmd("leaderboard", leaderboard, 1, 'See who\'s winning'),
    bot_cmd("updoots", points, 1, 'Check your updoots'),
]
