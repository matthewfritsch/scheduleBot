from discord.ext import commands
from scripts.eventmanager import add_event, allEvents

client = commands.Bot(command_prefix='!sch ')
client.remove_command('help')
commandList = ['add', 'events', 'help']


@client.event
async def on_ready():
    print('Bot is started.')


@client.command()
async def add(ctx, *, message):
    await ctx.send(add_event(message))


# @client.event
# async def on_command(ctx):
#    await ctx.send('<@' + str(ctx.author.id) + '>')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Some arguments missing. Please try again!')
    else:
        await ctx.send("We're getting an unknown error. Consult Mac.")
        await ctx.send('> ' + str(error))


@client.command()
async def help(ctx, *, message):
    if message is None or message is '':
        await ctx.send('Type !sch <command> [OPTIONS], or !sch help <command> to see correct syntax!')
        cmdPrint = 'Commands include:'
        for cmd in commandList:
            cmdPrint += '\n- ' + cmd
        await ctx.send(cmdPrint)
    if message == "add":
        await ctx.send('!sch add <eventName> [OPTIONS]\nOptions:\n -d <date>\n -t <time>\n -s <summary>\n -r <role>')
        await ctx.send('> !sch add Essay -d 5-22 -t 11PM -r @essayTeam')
        return
    if message == "events":
        await ctx.send('!sch events\nThis command sends the list of all events stored by @scheduleBot')
        return


@client.command()
async def events(ctx):
    for e in allEvents:
        await ctx.send(e)
    if len(allEvents) is 0:
        await ctx.send('No events currently!')


client.run('')  # replace empty str with bot key
