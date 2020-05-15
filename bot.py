import discord
from discord.ext import commands

client=commands.Bot(command_prefix='!sch ')

@client.event
async def on_ready():
    print('Bot is started.')

#await ctx.send("> " + message) this line will just quote the user
@client.command()
async def add(ctx, *, message):
    print(ctx, message)
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Some arguments missing. Please try again!")

client.run('') #replace empty str with bot key
