import discord
import random, os
from discord.ext import commands
from project import gen_pass,sampah_organic,sampah_anorganic

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def password(ctx):
    await ctx.send("Ini pasword untuk mu:")
    await ctx.send(gen_pass())
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
@bot.command()
async def eightballs(ctx):
    balan= ["Iya", "Enggak", "Gak mungkin", "Udah pasti iya", "Kayaknya enggak ", "Iya kayaknya", "Mustahil", "100% bener"]
    balran= random.choice(balan)
    await ctx.send(balran)

@bot.command()
async def meme(ctx):

    gambar = random.choice (os.listdir('images'))

    with open(f'images/{gambar}', "rb") as f:
        pic= discord.File(f)

    await ctx.send(file=pic) 

@bot.command()
async def organic(ctx):
    sampah=""
    for i in sampah_organic:
        i = i+'\n'
        sampah += i
    await ctx.send('daftar sampah organic')
    await ctx.send(sampah)

@bot.command()
async def anorganic(ctx):
    sampah=""
    for i in sampah_anorganic:
        i = i+'\n'
        sampah += i
    await ctx.send('daftar sampah anorganic')
    await ctx.send(sampah)

bot.run("")
