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

client.run('NzA5OTQ5OTQ0MjMxODg2ODg4.XrxOHA.HormCLTjB_V5X681IG_GupYM0oA')