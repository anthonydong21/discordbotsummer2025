import os
import random
import discord
from dotenv import load_dotenv

#connecting the bot
from discord.ext import commands
#loading the token and guild
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True  
intents.members = True

#removes default !help
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)



@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord yay!')  

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hiii {member.name}, welcome to my server!!!!!!!!!!!!!!'
    )




#silly quotes, references from toontown, 
#https://www.mmocentralforums.com/forums/showthread.php?t=234847

@bot.command(name='joke')
async def joke(ctx):
    sillyquote = [
        "What travels around the world but stays in a corner? ||A stamp.||",
        "Why was the math book unhappy? ||It had too many problems.||",
        "What did the doctor say to the sick orange? ||Are you peeling well?||",
        "What did the peanut say to the elephant? ||Nothing peanuts can't talk||",
        "Why do mummies make excellent spies? ||Because they're good at keeping things under wraps||",
        "What do you call a blind dinosaur? ||An I-Dont-Think-He-Saurus!||",
        "What kind of mistakes do spooks make? ||Boo boos||",
        "What do you call a chicken at the north pole? ||Lost||",
        "What did the cashier say to the register? ||Im counting on you.||"


    ]
    response = random.choice(sillyquote)
    await ctx.send(response)
    await ctx.message.add_reaction('✅')
#help
@bot.command(name='help')
async def helpme(ctx):
    help_text = "Here are my current commands:\n!joke: tells a joke!"
    await ctx.send(help_text)
#raise exception for errors
@bot.command(name='raise-exception')
async def raise_exception(ctx):
    raise discord.DiscordException


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


bot.run(TOKEN)