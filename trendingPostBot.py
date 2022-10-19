import discord
import random
import os
import praw
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv("C:/Users/Dexter/Documents/Discord Bot/token.env")
token = os.getenv('token')
id = os.getenv('id')
secret = os.getenv('secret')
user = os.getenv('user')
passW = os.getenv('passW')

reddit = praw.Reddit(client_id = id,
                    client_secret =  secret,
                    username = user,
                    password = passW,
                    user_agent = "redditPraw", check_for_async=False)

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = "%", intents = intents, case_insensitive=True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def hotPost(ctx, subred = "memes"):
    subreddit = reddit.subreddit(subred)
    all_subs = []

    hot = subreddit.hot(limit = 50)
    for submission in hot:
        all_subs.append(submission)
    
    random_sub = random.choice(all_subs)
    name = random_sub.title
    urlBro = random_sub.url

    em = discord.Embed(title=name)
    em.set_image(url = urlBro)
    await ctx.send(embed = em)
    
@client.event
async def on_message(message):
    user_message = str(message.content)
    channel = str(message.channel.name)
    
    if message.author == client.user:
        return
    await client.process_commands(message)
    
client.run(token)