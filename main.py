from webserver import keep_alive
import os
from random import choice
import discord
import discord.utils
from discord.ext import commands
from random import randint
import asyncio

# Creating bot that uses '>' as its prefix for commands
client = commands.Bot(command_prefix = '>', case_insensitive = True)

# Loads all the cogs in the Cogs Folder
for filename in os.listdir('./Cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'Cogs.{filename[:-3]}')

# Bot command that makes the bot greet the user
@client.command()
async def hello(ctx):
    hello_embed = discord.Embed(title="HELLO!",description=f"Hello {ctx.author.mention}", color=discord.Color.lighter_gray())
    # List containing URLs of GIFs saying 'Hello'
    url_list = ["https://media.tenor.com/images/85e426c13870d42c18ad4b3b8644a105/tenor.gif", "https://media.tenor.com/images/acc4116372dcc4b342cb1a00ae657151/tenor.gif","https://media1.tenor.com/images/9969d2bc836ee216a3319d0c15d8ad35/tenor.gif","https://media1.tenor.com/images/0ed8b6e0b69defc406010a69a33492fe/tenor.gif?itemid=14129058"]
    # Embeds a gif from the URL list chosen randomly
    hello_embed.set_image(url=choice(url_list))
    await ctx.send(embed = hello_embed)

# Bot command that sends an embedded message wishing
# someone a happy birthday and adds reaction for
# members to react to
@client.command()
async def hbd(ctx, member : discord.Member):
  hbd_embed = discord.Embed(title='HAPPY BIRTHDAY!', description = f'Happy Birthday {member.mention}!! \nEveryone react to wish them a happy birthday!!', color = discord.Color.random())
  hbd_message = await ctx.send(embed = hbd_embed)
  await hbd_message.add_reaction('🎂')

# Command that reminds you that Mario loves you very
# much if your message includes any of the above words
@client.command()
async def sad(ctx, member:discord.Member=None):
  if member == None:
    member = ctx.author
  file=discord.File("Mario.jpg")
  await ctx.send(f"{member.mention}, don't-a be sad\nMario loves you very much", file=file)

# Command to send the 'Kal Sunday Hai' video 
# ***Not mentioned in help is this is strictly an 
#           inside joke with my friends***
@client.command()
async def sunday(ctx):
  await ctx.send(file=discord.File("Kal Sunday Hai.mp4"))

# Command that adds the role "Muted" to the mentioned
# member. The role makes it so that the mentioned member
# can't send messages to the server for the mentioned
# time in seconds
# *Can only be called by administrators of the server*
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member, mute_time = 0):
  role = discord.utils.get(ctx.guild.roles, name='Muted')
  await member.add_roles(role)
  await ctx.send(f"{member.mention} has been muted for {mute_time} seconds")
  await asyncio.sleep(mute_time)
  await ctx.send(f"{member.mention} is now unmuted")
  await member.remove_roles(role)
  
# Command that removes the role "Muted" from 
# mentioned member.
# *Can only be called by administrators of the server*
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name='Muted')
  if role not in member.roles:
    await ctx.send(f'{member.mention} isn\'t muted to begin with')
  else:
    await member.remove_roles(role)
    await ctx.send(f'{member.mention} has been unmuted')

# Command where the user has a 1/1000 chance of
# being given the role 'POGCHAMP'
@client.command()
async def pogchamp(ctx):
  role = discord.utils.get(ctx.guild.roles, name='POGCHAMP')
  if role in ctx.author.roles:
    await ctx.send(f'{ctx.author.mention}, you are already a POGCHAMP')
    return
  number = randint(1, 1000)
  if number == randint(1, 1000):
    await ctx.send(f'{ctx.author.mention}, you are a POGCHAMP')
    await ctx.author.add_roles(role)
  else:
    await ctx.send(f'{ctx.author.mention}, you are not very poggers')
    
# Sends a message if a user that is not an
# administrator tries to use the mute command
@mute.error
async def mute_error(ctx, error):
  if isinstance(error):
    error_message = "Sorry, you don't have the permissions to use that command"
    await ctx.send(message = error_message)

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)