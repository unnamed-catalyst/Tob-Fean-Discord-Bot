import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import asyncio

class Images(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Command that sends an edited photo of the
  # user's pfp over a picture of Putin riding 
  # a bear
  @commands.command()
  async def putin(self, ctx, user:discord.Member=None):
    if user == None:
      user = ctx.author
    putin = Image.open("Images/putin.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((111, 111))
    putin.paste(pfp, (554, 88))
    
    putin.save("Images/putin1.jpg")
    await ctx.send(file=discord.File("Images/putin1.jpg"))
    
  # Command that sends an edited photo of the
  # pinged pfps over the peeping boyfriend meme
  @commands.command()
  async def bflook(self, ctx, user1:discord.Member=None,user2:discord.Member=None, user3:discord.Member=None):
    if user1 == None:
      user1 = ctx.author
    if user2 == None:
      user2 = ctx.author
    if user3 == None:
      user3 = ctx.author
    bflook = Image.open("Images/bf_looking.jpg")

    asset1 = user1.avatar_url_as(size = 128)
    data1 = BytesIO(await asset1.read())
    pfp1 = Image.open(data1)
    pfp1 = pfp1.resize((131, 131))
    bflook.paste(pfp1, (972, 188))

    asset2 = user2.avatar_url_as(size = 128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)
    pfp2 = pfp2.resize((131, 131))
    bflook.paste(pfp2, (643, 108))

    asset3 = user3.avatar_url_as(size = 128)
    data3 = BytesIO(await asset3.read())
    pfp3 = Image.open(data3)
    pfp3 = pfp3.resize((131, 131))
    bflook.paste(pfp3, (300, 195))

    bflook.save("Images/bf_looking1.jpg")
    await ctx.send(file=discord.File("Images/bf_looking1.jpg"))

  # Command that edits the Drake Hotline Bling
  # meme to show the pinged pfp and some text input
  # from the user
  @commands.command()
  async def drake(self, ctx, user:discord.Member=None):
    if user == None:
      user = ctx.author
    drake = Image.open("Images/drake.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((111, 111))
    drake.paste(pfp, (37, 103))
    drake.paste(pfp, (198, 431))
    
    await ctx.send("What's the top text?")
    def check(reply):
      return reply.author == ctx.author and reply.channel == ctx.channel 
    try:
      reply = await self.client.wait_for("message", check=check, timeout=45)
    except asyncio.TimeoutError:
      await ctx.send(f"Bruh, {ctx.author.mention} why didn't you reply")
    font = ImageFont.truetype("impact.ttf", 35)
    draw = ImageDraw.Draw(drake)
    draw.text((420, 180), reply.content, (0, 0, 0),font=font)

    await ctx.send("What's the bottom text?")
    def check(reply):
      return reply.author == ctx.author and reply.channel == ctx.channel 
    try:
      reply = await self.client.wait_for("message", check=check, timeout=45)
    except asyncio.TimeoutError:
      await ctx.send(f"Bruh, {ctx.author.mention} why didn't you reply")
    font = ImageFont.truetype("impact.ttf", 35)
    draw = ImageDraw.Draw(drake)
    draw.text((420, 570), reply.content, (0, 0, 0),font=font)

    drake.save("Images/drake1.jpg")
    await ctx.send(file=discord.File("Images/drake1.jpg"))

def setup(client):
  client.add_cog(Images(client))