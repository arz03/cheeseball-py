import discord
import os
import requests
import json

import glob
from PIL import Image, ImageDraw, ImageFont
import codecs

from utils import permissions
from discord.ext.commands import AutoShardedBot, DefaultHelpCommand


import urllib.parse
import base64
import sys 
import requests

import praw

import typing 
import random 

import string

from utils import http

import editdistance
import re
import asyncio
import aiohttp
import traceback
import random
import datetime
import time
import subprocess

import dotenv

from prsaw import RandomStuff 

from weather import *

from tinydb import TinyDB, Query
from discord.ext.commands import Bot

from discord.ext import commands
from keep_alive import keep_alive
from discord import DMChannel

intents = discord.Intents.default()
owner = "396706408881455104"
owner = 396706408881455104
client = commands.Bot(command_prefix=".", command_attrs=dict(hidden=True), 
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False),
    intents=discord.Intents(  # kwargs found at https://discordpy.readthedocs.io/en/latest/api.html?highlight=intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True, presences=True
    ))
bot = commands.Bot(command_prefix=".", command_attrs=dict(hidden=True), 
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False),
    intents=discord.Intents(  # kwargs found at https://discordpy.readthedocs.io/en/latest/api.html?highlight=intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True, presences=True
    ))
cogs = ["events.on_message"]
rs = RandomStuff(async_mode = True)

api_key = 'b1fa9ec1fda91ac3cac6e56730b2321b'
command_prefix = '.w '

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n - " + json_data[0]['a']
    return (quote)



status_type = {"idle": discord.Status.idle}






@client.event
async def on_ready():
    print("Bot is ready!")

    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)
    await asyncio.sleep(3)
    print('---------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(discord.utils.oauth_url(client.user.id))
    await client.change_presence(status="idle",
      activity=discord.Activity(
        type=discord.ActivityType.watching, name="𝙮𝙤𝙪 𝙦𝙪𝙩𝙞𝙚 𝙐𝙬𝙐"))


    







@client.command(helpinfo='For when plain text just is not enough')
async def emojify(ctx, *, text: str):
    '''
    Converts the alphabet and spaces into emoji
    '''
    author = ctx.message.author
    emojified = ''
    formatted = re.sub(r'[^A-Za-z ]+', "", text).lower()
    if text == '':
        await ctx.send('Remember to say what you want to convert!')
    else:
        for i in formatted:
            if i == ' ':
                emojified += '     '
            else:
                emojified += ':regional_indicator_{}: '.format(i)
        if len(emojified) + 2 >= 2000:
            await ctx.send('Your message in emojis exceeds 2000 characters!')
        if len(emojified) <= 25:
            await ctx.send('Your message could not be converted!')
        else:
            await ctx.send(''+emojified+'')







@client.command(helpinfo='Clone your words - like echo')
async def clone(ctx, *, message):
    '''
    Creates a webhook, that says what you say. Like echo.
    '''
    pfp = requests.get(ctx.author.avatar_url_as(format='png', size=256)).content
    hook = await ctx.channel.create_webhook(name=ctx.author.display_name,
                                            avatar=pfp)
    
    await hook.send(message)
    await hook.delete()
    await ctx.message.delete()



@client.command()
async def act(ctx, member: discord.Member, *, message=None):
        if message == None:
                await ctx.send(f'Please provide a message with that!')
                return

        webhook = await ctx.channel.create_webhook(name=member.name)
        await webhook.send(
            str(message), username=member.name, avatar_url=member.avatar_url)

        await webhook.delete()
        await ctx.message.delete()




@client.command(name='eval')
async def my_command(ctx, *, arg):
    result = eval(arg)
    await ctx.send(arg)
    await ctx.send(result)






























player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver
    if gameOver:
        global board
        board = [
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:"
        ]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            myEmbed = discord.Embed(title="GAME IN PROGRESS",
                                    description="IT IS <@" + str(player1.id) +
                                    ">'s TURN.",
                                    color=0xe74c3c)
            await ctx.send(embed=myEmbed)
        elif num == 2:
            turn = player2
            myEmbed = discord.Embed(title="GAME IN PROGRESS",
                                    description="IT IS <@" + str(player2.id) +
                                    ">'s TURN.",
                                    color=0xe74c3c)
            await ctx.send(embed=myEmbed)
    else:
        myEmbed = discord.Embed(
            title="GAME IN PROGRESS",
            description=
            "A GAME IS STILL IN PROGRESS. FINISH IT BEFORE STARTING A NEW ONE",
            color=0xe74c3c)
        await ctx.send(embed=myEmbed)


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    myEmbed = discord.Embed(title="WINNER!",
                                            description=mark + " :crown: ",
                                            color=0xf1c40f)
                    await ctx.send(embed=myEmbed)
                elif count >= 9:
                    gameOver = True
                    myEmbed = discord.Embed(
                        title="TIE",
                        description="IT'S A TIE :handshake:",
                        color=0xf1c40f)
                    await ctx.send(embed=myEmbed)

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                myEmbed = discord.Embed(
                    title="PLACE ERROR!",
                    description=
                    "BE SURE TO CHOOSE AN INTEGER BETWEEN 1 AND 9 (INCLUSIVE) AND AN UNMARKED TILE. ",
                    color=0xe74c3c)
                await ctx.send(embed=myEmbed)
        else:
            myEmbed = discord.Embed(title="TURN ERROR!",
                                    description="IT'S NOT YOUR TURN",
                                    color=0xe74c3c)
            await ctx.send(embed=myEmbed)
    else:
        myEmbed = discord.Embed(
            title="START GAME",
            description="TO START A NEW GAME, USE -tictactoe COMMAND",
            color=0x2ecc71)
        await ctx.send(embed=myEmbed)


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[
                condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        myEmbed = discord.Embed(title="MENTION ERROR!",
                                description="PLEASE MENTION 2 USERS",
                                color=0xe74c3c)
        await ctx.send(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = discord.Embed(
            title="ERROR!",
            description=
            "PLEASE MAKE SURE TO MENTION/PING PLAYERS (ie. <@688534433879556134>)",
            color=0xe74c3c)
        await ctx.send(embed=myEmbed)


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        myEmbed = discord.Embed(title="NO POSITION",
                                description="PLEASE ENTER A POSITION TO MARK",
                                color=0xe74c3c)
        await ctx.send(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = discord.Embed(title="INTEGER ERROR!",
                                description="PLEASE MAKE SURE IT'S AN INTEGER",
                                color=0xe74c3c)
        await ctx.send(embed=myEmbed)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return


    if message.content == ('quote'):
        quote = get_quote()
        await message.reply(quote)
    await client.process_commands(message)

    if message.content == ('.help'):
        await message.channel.send(
            '**Commands**\n`quote` - get a random quote\n`.tictactoe <@user1> <@user2>` - play tictactoe\n`.hug <@user>`- give a hug <3\n`.hi <@user>`- say hi to your friend!\n`.echo <text>`- echos your text\n`.kiss <@user>`- kiss your ammmm... FRIEND?\n`.av <@user>`- Get a users avatar.\n`.ping`- pong\n`!ev`-¯\_(ツ)_/¯\n`.kill`-kills💀 (restricted)\n`!spam <text>`-spaayyyymmmm (restricted)\n`.clean <limit>` - purge messages (admin only)\n`---------------\n*;help* - .js commands'
        )

    if message.content == ('quote daily'):
        await message.channel.send(
            'Daily quotes are currently under development. When they\'re done, you\'ll be able to pick a channel the the frequency for the quotes to be posted in.'
        )

    if message.content == ('.contact'):
        await message.channel.send('@aarz#0003')

    if message.content == ('ping'):
        await message.channel.send('Pong! :ping_pong:')

    if message.content == ('quote upvote'):
        await message.channel.send('unavailable.')

    if message.content == ('morning'):
        await message.channel.send(
            'mooowwwrrrninnngg qttt       ̷       (̷ ̷ ̷ ̷ⓛ̷ ̷ ̷ ̷ﻌ̷ ̷ ̷ ̷ⓛ̷ ̷ ̷ ̷*̷ ̷)̷', delete_after=7
        )

    if message.content == ('gm'):
        await message.channel.send('mooowwwrrrninnngg qttt <3', delete_after=7)
    if message.content == ('Gm'):
        await message.channel.send('mooowwwrrrninnngg qttt <3', delete_after=7)

    #if message.content == ('heylo'):
    #    await message.channel.send('hello ji ~(=^‥^)/', delete_after=7)

    #if message.content == ('hi'):
    #   await message.channel.send('hennloo (⁎˃ᆺ˂)', delete_after=7)
    #if message.content == ('Hi'):
    #    await message.channel.send('hennloo (⁎˃ᆺ˂)', delete_after=7)
    #if message.content == ('sex'):
    #    await message.channel.send('sex👍')
    #    await message.add_reaction('😳')

    #if message.content == ('Sex'):
    #    await message.channel.send('sex👍')
    #    await message.add_reaction('😳')



    #if message.content == ('ok'):
    #    await message.channel.send('*:･ﾟ✧(=✪ ᆺ ✪=)*:･ﾟ✧', delete_after=7)

    if message.content == ('.invite'):
        await message.channel.send(
            'https://discord.com/oauth2/authorize?client_id=815457074406359061&permissions=8&scope=bot'
        )


    if message.content.startswith('accha'):
       await message.channel.send(' ‌ ‌‌ ‌‌ ‌‌    ‍\n ‌ ‌‌ ‌‌ ‌‌    ‍\n ‌ ‌‌ ‌‌ ‌‌    ‍\n ‌ ‌‌ ‌‌ ‌‌    ‍\n ‌ ‌‌ ‌‌ ‌‌    ‍\n ‌ ‌‌ ‌‌ ‌‌    ‍\n', delete_after=1)
         
    if message.content.startswith('poll'):
         await message.add_reaction('👍')
         await message.add_reaction('👎')
         await message.add_reaction('🤷‍♂️')

    if message.content.startswith('+poll'):
         await message.add_reaction('👍')
         await message.add_reaction('👎')
         await message.add_reaction('🤷‍♂️')

    if message.content.startswith('?poll'):
         await message.add_reaction('👍')
         await message.add_reaction('👎')
         await message.add_reaction('🤷‍♂️')

    if message.content.startswith('.poll'):
         await message.add_reaction('👍')
         await message.add_reaction('👎')
         await message.add_reaction('🤷‍♂️')

    if message.content.startswith('.kiss'):
        await message.channel.send(
            'https://tenor.com/view/milk-and-mocha-bear-couple-kisses-kiss-love-gif-12498627'
        )

    if message.content.startswith('.hug'):
        await message.channel.send(
            'https://tenor.com/view/milk-and-mocha-hug-love-heart-couple-gif-17258498'
        )

    if message.content.startswith('.hi'):
        await message.channel.send(
            'https://thumbs.gfycat.com/RecklessEagerGraysquirrel-max-1mb.gif')

    if message.content.startswith('!echo'):
        await message.channel.send('please use  👉 .echo 👈 චᆽච')

    if message.content.startswith('.av'):
        await message.channel.send

    #if message.content.startswith('gn'):
    #    await message.channel.send('*yawns*... gn <3', delete_after=7)

    #if message.content == ('?'):
    #    await message.channel.send('?')

    if message.content == ('op'):
        await message.channel.send('op bhay op')
    #if message.content == ('hehe'):
    #    await message.channel.send('huhu', delete_after=7)

    if message.content.startswith('group hug'):
        await message.reply(
            'https://cdn.discordapp.com/attachments/722103516558131306/808419532636028978/unknown.png'
        )

    
    if message.content == ('.nuke'):
        await message.channel.send('***Are you sure you want to nuke?***\n reply with ```y for yes``` or ```n for no```')

    if message.content.startswith(".echo"):
        await message.channel.send(message.content[5:].format(message))
        await client.delete_message(context.message)

    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
        else:
            await message.channel.send('nuu👎👎👎 spam=bad')

    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))
    if message.content.startswith("!spam"):
        if str(message.author.id) == '396706408881455104':
            await message.channel.send(message.content[5:].format(message))

  
    if message.author != client.user and message.content.startswith(command_prefix):
        if len(message.content.replace(command_prefix, '')) >= 1:
            location = message.content.replace(command_prefix, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data = parse_data(json.loads(requests.get(url).content)['main'])
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))




    
    
    if message.channel.id == 824857068103663657:
      response = await rs.get_ai_response(message.content)
      await message.reply(response)



format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@client.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)




  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)



  icon = str(ctx.guild.icon_url)



  text_channels = len(ctx.guild.text_channels)
  voice_channels = len(ctx.guild.voice_channels)
  categories = len(ctx.guild.categories)
  channels = text_channels + voice_channels
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=0x5CFF9D
    )
  embed.set_thumbnail(url=icon)
  
  embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}")

  await ctx.send(embed=embed)




@client.command()
@commands.cooldown(rate=1, per=2.0,type=commands.BucketType.user)
async def urban(ctx, *, search:commands.clean_content):
    """ Find the 'best' definition to your words """
    async with ctx.channel.typing():
        try:
            url = await http.get(f'https://api.urbandictionary.com/v0/define?term={search}', res_method="json")
        except Exception:
            return await ctx.send("Urban API returned invalid data... might be down atm.")
        if not url:
            return await ctx.send("I think the API broke...")
        if not len(url['list']):
            return await ctx.send("Couldn't find your search in the dictionary...")
        result = sorted(url['list'], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]
        definition = result['definition']
        if len(definition) >= 1000:
            definition = definition[:1000]
            definition = definition.rsplit(' ', 1)[0]
            definition += '...'
        await ctx.send(f"📚 Definitions for **{result['word']}**```fix\n{definition}```")



@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    await ctx.send('Messages Purged by {}'.format(ctx.author.mention), delete_after=3)
    await ctx.message.delete()



@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("You cant do that!", delete_after=3)


@client.command()
async def kiss(ctx, *, member: discord.Member = None):
    await ctx.reply(f"awww 😍 {member.mention}")


@client.command()
async def hug(ctx, *, member: discord.Member = None):
    await ctx.reply(f"hey cutie! you got a hug {member.mention}")


@client.command()
async def hi(ctx, *, member: discord.Member = None):
    await ctx.reply(f"hellooowwwww {member.mention}")


@client.command(pass_context=True, no_pm=True)
async def av(ctx, member: discord.Member):
    """User Avatar"""

    await ctx.reply("{}".format(member.avatar_url))
    await ctx.channel.send("{}".format(member.mention))




reddit = praw.Reddit(client_id='jFqQOyp7CqFeTQ',
                     client_secret='p0UNZPjr0GsIRslJ2l7OQSfFuTCDVQ',
                     username='aarz03',
                     password=os.environ['rpass']
,
                     user_agent='cheeseball')


@client.command()
async def meme(ctx,subred = "SaimanSays"):
   subreddit = reddit.subreddit(subred)
   all_subs = []

   top = subreddit.top(limit = 100)

   for submission in top:
     all_subs.append(submission)

   random_sub = random.choice(all_subs)

   name = random_sub.title
   url = random_sub.url

   em = discord.Embed(title = name)

   em.set_image(url = url)

   await ctx.reply(embed=em)







@client.command()
async def hello(ctx):
    await ctx.channel.send(f"Hello! {ctx.author.mention}")
    await ctx.message.delete()

@client.command()
async def ping(ctx):
    await ctx.reply(f"Pong! :ping_pong: {round(client.latency*1000)}ms")

@client.command()
async def poll(ctx, *, message):
    emb = discord.Embed(title=" POLL", description=f"{message}")
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('🤷‍♂️')

  
@client.event
async def on_guild_join(Guild):
    await Guild.system_channel.send('Hello! use .help 7 ;help to get list of commands👍'
                                    )


@client.command()
async def kill(ctx):
    id = str(ctx.author.id)
    if id == '396706408881455104':
        await ctx.send('AARZ SACRIFISED ME!!!! AAAAAAAA😭😭😭😭')
        await ctx.bot.logout()
    else:
        await ctx.send(
            "You dont have sufficient permmisions to perform this action!")



@client.command(aliases=["fancy"])
async def fancify(ctx, *, text):
    """Makes text fancy!"""
    try:
        def strip_non_ascii(string):
            """Returns the string without non ASCII characters."""
            stripped = (c for c in string if 0 < ord(c) < 127)
            return ''.join(stripped)

        text = strip_non_ascii(text)
        if len(text.strip()) < 1:
            return await self.ctx.send(":x: ASCII characters only please!")
        output = ""
        for letter in text:
            if 65 <= ord(letter) <= 90:
                output += chr(ord(letter) + 119951)
            elif 97 <= ord(letter) <= 122:
                output += chr(ord(letter) + 119919)
            elif letter == " ":
                output += " "
        await ctx.send(output)
    except:
        await ctx.send(config.err_mesg_generic)



@client.command()
async def timer(ctx, seconds):
  try:
    secondint = int(seconds)
    if secondint < 0 or secondint == 0:
                await ctx.send("I dont think im allowed to do negatives")
                raise BaseException
    
    message = await ctx.send(f"Timer: {seconds}")

    while True:
     secondint -= 1
     if secondint == 0:
       await message.edit(content="Ended")
       break
     
     await message.edit(content=f"Timer: {secondint}")
     await asyncio.sleep(1)

    await ctx.send(f"{ctx.author.mention}, Your countdown ans been ended")
 
  except ValueError:
   await ctx.send('You must enter a number!')



@client.command()
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' sent to: " + target.name)

        except:
            await ctx.channel.send("Couldn't dm the given user.")
        

    else:
        await ctx.channel.send("You didn't provide a user's id and/or a message.")



snipe_message_author = {}
snipe_message_content = {}

editsnipe_message_author = {}
editsnipe_message_content = {}

@client.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    await asyncio.sleep(60)
    # del snipe_message_author[message.channel.id]
    # del snipe_message_content[message.channel.id]

@client.event
async def on_message_edit(message_before, message_after):
    editsnipe_message_author[message_before.channel.id] = message_before.author
    editsnipe_message_content[message_before.channel.id] = message_before.content
    await asyncio.sleep(60)
    del editsnipe_message_author[message_before.channel.id]
    del editsnipe_message_content[message_before.channel.id]


@client.command(name='snipe')
async def snipe(ctx):
    channel = ctx.channel
    try:
        em = discord.Embed(name=f"Last deleted message in #{channel.name}",
                           description=snipe_message_content[channel.id], color=0x5CFF9D)
        em.set_footer(
            text=f"This message was sent by {snipe_message_author[channel.id]}"
        )
        await ctx.send(embed=em)
    except:
        await ctx.send(
            f"There are no recently deleted messages in #{channel.name}")

@client.command(name='editsnipe')
async def editsnipe(ctx):
    channel = ctx.channel
    try:
        em = discord.Embed(name=f"Last edited message in #{channel.name}",
                           description=editsnipe_message_content[channel.id], color=0x5CFF9D)
        em.set_footer(
            text=f"This message was sent by {editsnipe_message_author[channel.id]}"
        )
        await ctx.send(embed=em)
    except:
        await ctx.send(
            f"There are no recently edited messages in #{channel.name}")




@client.command(pass_context=True)
async def role(ctx, user: discord.Member, *, role: discord.Role):
    if str(ctx.author.id) == '396706408881455104':
        if role in user.roles:
           await user.remove_roles(role) #removes the role if user already has
           roleremove = discord.Embed(title=f":boot: Removed *{role}* from *{user.name}*!", description=f"By: *{ctx.author.mention}*")
           await ctx.send(f"{user.mention}",embed=roleremove)
        else:
           await user.add_roles(role) #adds role if not already has it
           roleadd = discord.Embed(title=f":boot: Added *{role}* to *{user.name}*!", description=f"By: *{ctx.author.mention}*")
           await ctx.send(f"{user.mention}",embed=roleadd)
    else:
      await ctx.reply("<:dno:793122178961899541>")
























@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
    if str(ctx.author.id) == '396706408881455104':
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked *{user.name}*!", description=f"Reason: *{reason}*\nBy: *{ctx.author.mention}*")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

#The below code bans player.
@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    if str(ctx.author.id) == '396706408881455104':
       await member.ban(reason = reason)
       ban = discord.Embed(title=f":boot: Banned *{member.name}*!", description=f"Reason: *{reason}*\nBy: *{ctx.author.mention}*")
       await ctx.channel.send(embed=kick)
       await member.send(embed=ban)

#The below code unbans player.
@client.command()
async def unban(ctx, *, member):
    if str(ctx.author.id) == '396706408881455104':
       banned_users = await ctx.guild.bans()
       member_name, member_discriminator = member.split     ("#")

       for ban_entry in banned_users:
           user = ban_entry.user



          

           if (user.name, user.discriminator) == (member_name, member_discriminator):
             
               await ctx.guild.unban(user)
               unban = discord.Embed(title=f":boot: Banned *{member.name}*!", description=f"By: *{ctx.author.mention}*")

               await ctx.send(embed=unban)
              


@client.command()
async def moverole(ctx, role: discord.Role, pos: int):
    if str(ctx.author.id) == '396706408881455104': 
        await ctx.message.delete()   
        try:
            await role.edit(position=pos)
            await ctx.send("Role moved.", delete_after=1)
        except discord.Forbidden:
            await ctx.send("You do not have permission to do that!")
        except discord.HTTPException:
            await ctx.send("Failed to move role")
        except discord.InvalidArgument:
            await ctx.send("Invalid argument")




keep_alive()
client.run(os.getenv('TOKEN'))
