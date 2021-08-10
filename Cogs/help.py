import discord
from discord.ext import commands

bot_prefix = '>'

class Help(commands.Cog):
  def __init__(self, client):
    self.client = client

    # Removing help command to make a custom help command
    self.client.remove_command('help') 

  # Custom help command
  @commands.group(invoke_without_command = True)
  async def help(self, ctx):
    help_embed = discord.Embed(title='Help',description=f'Use {bot_prefix}help <command> for extended information', color=discord.Color.lighter_gray())

    help_embed.add_field(name='Useful Commands', value='mute, unmute, valorant', inline=False)
    help_embed.add_field(name='\nFun Commands', value='hello, hbd, pogchamp, element, sad', inline=False)
    help_embed.add_field(name='\nImage Commands', value='putin, bflook, drake', inline=False)
    await ctx.send(embed = help_embed)

  @help.command()
  async def hello(self, ctx):
    embed = discord.Embed(title='hello', description='Greets the user', color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}hello')
    await ctx.send(embed = embed)

  @help.command()
  async def hbd(self, ctx):
    embed = discord.Embed(title='hbd', description='Wish someone a happy birthday', color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}hbd <ping member>')
    await ctx.send(embed = embed)

  @help.command()
  async def mute(self, ctx):
    embed = discord.Embed(title='mute', description='Mute a user for x seconds.\n*Can only be called by admins*', color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}mute <ping member><seconds to be muted>')
    await ctx.send(embed = embed)

  @help.command()
  async def unmute(self, ctx):
    embed = discord.Embed(title='unmute', description='Unmute a muted user.\n*Can only be called by admins*', color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}mute <ping member>')
    await ctx.send(embed = embed)

  @help.command()
  async def pogchamp(self, ctx):
    embed = discord.Embed(title='pogchamp', description='You have a 1/1000 chance of being given the role \'POGCHAMP\'\n*Pls don\'t spam*',color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}pogchamp')
    await ctx.send(embed = embed)

  @help.command()
  async def element(self, ctx):
    embed = discord.Embed(title='element', description='Take quick personality quiz and get one of the elements from Avatar: The Last Airbender',color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}element')
    await ctx.send(embed = embed)

  @help.command()
  async def putin(self, ctx):
    embed = discord.Embed(title='putin', description='Put your pfp or someone else\'s on Putin\'s face', color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}putin <optional ping someone>')
    await ctx.send(embed=embed)
  
  @help.command()
  async def bflook(self, ctx):
    embed = discord.Embed(title='bflook', description='Put your pfp or someone else\'s on the famous peeping boyfriend meme', color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}putin <optional ping someone> <optional ping someone> <optional ping someone>')
    await ctx.send(embed=embed)

  @help.command()
  async def drake(self, ctx):
    embed = discord.Embed(title='drake', description='Put your pfp or someone else\'s on the drake hotline bling meme', color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}drake <optional ping someone>')
    await ctx.send(embed=embed)

  @help.command()
  async def valorant(self, ctx):
    embed = discord.Embed(title='valorant', description='Ping the server to ask if anyone wants to play Valorant, and also create a lobby so if anyone wants to play they can see who else is playing', color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}valorant <optional ping someone><optional ping someone><optional ping someone>')
    await ctx.send(embed=embed)

  @help.command()
  async def sad(self, ctx):
    embed = discord.Embed(title='sad', description='Reminds the user not to be sad and that Mario loves them very much', color=discord.Color.lighter_gray())
    embed.add_field(name='Syntax', value=f'{bot_prefix}sad <optional ping someone>')
    await ctx.send(embed = embed)

def setup(client):
  client.add_cog(Help(client))