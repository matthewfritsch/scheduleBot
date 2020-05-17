from discord.ext import commands
from EventHandler import add_event

client = commands.Bot(command_prefix='!sch ')
client.remove_command('help')


@client.event
async def on_ready():
    print('Bot is started.')

# await ctx.send("> " + message) this line will just quote the user


@client.command()
async def add(ctx, *, message):
    print(ctx, message)
    add_event(message)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Some arguments missing. Please try again!')
    else:
        await ctx.send("We're getting an unknown error. Consult Mac.")
        await ctx.send('> ' + str(error))


@client.command()
async def help(ctx, message):
    await ctx.send('<@'+str(ctx.author.id)+'>')
    if message == "add":
        await ctx.send('!sch add <eventName> [OPTIONS]\nOptions:\n -d <date>\n -t <time>\n -s <summary>\n -r <role>')
        await ctx.send('> !sch add Essay -d 5-22 -t 11PM -r @essayTeam')
    if message == "events":
        await ctx.send('!sch events\nThis command sends the list of all events stored by @scheduleBot')


@client.command()
async def events(ctx):
    _myEvents = 0
    for e in _myEvents:
        await ctx.send(e)
    else:
        await ctx.send('No events currently!')

# for filename in os.listdir('./cogs'):
#    if filename.endswith('.py'):
#        client.load_extension("cogs."+filename[:-3])
#        print("Loaded ./cogs/" + filename)
# client.load_extension("cogs.EventHandler")
# print("Loaded ./cogs/EventHandler.py")

client.run('')  # replace empty str with bot key
