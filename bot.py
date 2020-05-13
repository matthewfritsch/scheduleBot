import discord
from discord.ext import commands

client=commands.Bot(command_prefix='!sch ')

@client.event
async def on_ready():
    print('Bot is started.')

@client.command()
async def add(ctx, *, message):
    print()
    #await ctx.send("> " + message) this line will just quote the user

client.run('') #replace empty str with bot key
