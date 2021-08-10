import discord
from discord.ext import commands

class Games(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.addList =[]
    self.lobby = []
    self.spots = 5

  # Command to ping the server to ask if anyone wants
  # to play Valorant, and also create a lobby so if
  # anyone wants to play they can see who else is
  # playing
  @commands.command(pass_context = True)
  async def valorant(self, ctx, member2:discord.Member=None, member3:discord.Member=None,
  member4:discord.Member=None):
    await ctx.send("@here")
    self.spots = 5
    self.lobby.clear()
    self.lobby.append(ctx.author)
    self.spots -= 1
    if member2 is not None and member2 not in self.lobby:
      self.lobby.append(member2)
      self.spots -= 1
    if member3 is not None and member3 not in self.lobby:
      self.lobby.append(member3)
      self.spots -= 1
    if member4 is not None and member4 not in self.lobby:
      self.lobby.append(member4)
      self.spots -= 1
    self.ctx = ctx

    description=f"{self.ctx.author.mention} wants to play Valorant\n"
    index = 5 - self.spots
    for i in range(0,index):
      description+=f"\n{i+1} - {self.lobby[i].mention}"
    for i in range(index, 5):
      description+=f"\n{i+1} - "
    description+=f"""\n\n\t\t*{self.spots} spots left*
    React with ✅ to join the lobby
    React with ❌ to leave the lobby"""
    embed = discord.Embed(title="VALORANT, COME BROS",description = description, color=discord.Color.from_rgb(250, 68, 84))
    file=discord.File("valorant.png")
    embed.set_thumbnail(url="attachment://valorant.png")
    self.message = await ctx.send(embed=embed, file=file)
    await self.message.add_reaction("✅")
    await self.message.add_reaction("❌")

  # Function that edits message to add players
  # to the lobby
  async def valo_lobby_add(self):
    description=f"{self.ctx.author.mention} wants to play Valorant\n"
    for user in self.addList:
      if user not in self.lobby and self.spots>0:
        self.lobby.append(user)
        self.spots -= 1
        for user in self.lobby:
            index = 5 - self.spots
        for i in range(0,index):
          description+=f"\n{i+1} - {self.lobby[i].mention}"
        for i in range(index, 5):
          description+=f"\n{i+1} - "
        description+=f"""\n\n\t\t*{self.spots} spots left*
        React with ✅ to join the lobby
        React with ❌ to leave the lobby"""
        embed = discord.Embed(title="VALORANT, COME BROS", description = description, color=discord.Color.from_rgb(250, 68, 84))
        embed.set_thumbnail(url="attachment://valorant.png")
        await self.message.edit(embed=embed)

  # Function that edits message to remove players
  # from the lobby
  async def valo_lobby_remove(self):
    description=f"{self.ctx.author.mention} wants to play Valorant\n"
    index = 5 -self.spots
    for i in range(0,index):
      description+=f"\n{i+1} - {self.lobby[i].mention}"
    for i in range(index, 5):
      description+=f"\n{i+1} - "
    description+=f"""\n\n\t\t*{self.spots} spots left*
    React with ✅ to join the lobby
    React with ❌ to leave the lobby"""
    embed = discord.Embed(title="VALORANT, COME BROS",description = description, color=discord.Color.from_rgb(250, 68, 84))
    embed.set_thumbnail(url="attachment://valorant.png")
    await self.message.edit(embed=embed)

  @commands.Cog.listener()
  async def on_reaction_add(self, reaction, user):
    if user!=self.client.user:
      if reaction.message==self.message and str(reaction.emoji) == "✅":
        if self.spots <= 0:
          await self.ctx.send("Sorry, it's a full stack")
        self.addList = await reaction.users().flatten()
        self.addList.remove(self.client.user)
        await self.valo_lobby_add()   
      elif reaction.message==self.message and str(reaction.emoji) == "❌":
        self.removeList = await reaction.users().flatten()
        for users in self.removeList:
          if users in self.lobby and users != self.ctx.author:
            self.lobby.remove(users)
            self.spots += 1
          await self.valo_lobby_remove()

def setup(client):
  client.add_cog(Games(client))