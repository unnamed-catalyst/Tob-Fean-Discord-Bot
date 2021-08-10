import discord
import discord.utils
from discord.ext import commands
from time import sleep
from random import sample
import asyncio

air_emblem = "https://upload.wikimedia.org/wikipedia/commons/e/e4/EmblemaAireControl.png"
water_emblem = "https://qph.fs.quoracdn.net/main-qimg-6bc04b13261fc0215db17a25b13a27a5"
earth_emblem = "https://qph.fs.quoracdn.net/main-qimg-d1c71c408251a3dc7b049ae0f91d5633"
fire_emblem = "https://i.pinimg.com/originals/c4/1b/c4/c41bc4d415741da0e149133e977061c5.png"
questions_no = 7
questions_list = [f"""Which one of these sounds the most like you?\n
A. Being a peaceful person
B. Going with the flow
C. Always standing your ground
D. Being short tempered""",

f"""Cliché, but what's your favorite season?\n
A. Spring
B. Winter
C. Autumn/Fall
D. Summer""",
    
f"""Which of these would you rather ride to battle on?\n 
A. A big flying cloud (probably called Nimbus)
B. A fluffy polar bear
C. A rhino
D. A dragon but one of those lame kinds that doesn't breathe fire""",
    
f"""Which of these sounds like the better vacation?\n 
A. A spiritual journey on a mountain
B. Going skiing
C. A long, tough hike
D. Going to the beach on a hot day""",
    
f"""Choose from these colours.
A. Brown
B. Blue
C. Green
D. Red""",
    
f"""Choose a Valorant Agent.
A. Jett
B. Sage
C. Breach
D. Pheonix""",
    
f"""You just got to that cafe your friends planned on meeting at. What are you ordering?
A. I always bring my own sandwiches
B. Literally just a bottle of water
C. FOOD. GIVE ME ALL THE FOOD.
D. Something hot and spicy"""]


class Element_Test(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Command that performs a little quiz and gives 
  # the user one of the four elements based on 
  # their choices in the quiz
  # Based on the show 'Avatar The Last Airbender'
  @commands.command()
  async def element(self, ctx):
    reply = await self.confirm_question(ctx)
    random_list = sample(questions_list, questions_no)
    if reply.content.lower() == 'y':
      for index in range(questions_no):
        reply = await self.question(ctx, index+1, random_list[index])
        stop = await self.score_update(reply)
        # Error Handling incase user enters an option 
        # that isn't accepted
        if stop:
          await ctx.send("Invalid option, start again")
          return
    else:
      await ctx.send("Aight no element test for you!")
    if not stop:
      await ctx.send("And your element is...")
      # 3 second pause for suspense
      sleep(3)
      self.score = int(round(self.score/7))
      await self.reveal_element(ctx)
  
  # Asks if user is sure they want to take the quiz
  async def confirm_question(self, ctx):
    self.score = 0
    self.user = ctx.author

    confirm_question_embed = discord.Embed(title='AVATAR ELEMENT QUIZ', description=f"""Are you sure you want to take the element quiz? {ctx.author.mention} 
    \n\nPlease reply with "Y" or "y" to continue""", color=discord.Color.from_rgb(255, 255, 255))
    file = discord.File("ElementTest/avatar_thumbnail.jpg")
    confirm_question_embed.set_thumbnail(url="attachment://avatar_thumbnail.jpg")
    await ctx.send(embed = confirm_question_embed, file=file)

    def check(reply):
      return reply.author == ctx.author and reply.channel == ctx.channel 
    try:
      reply = await self.client.wait_for("message", check=check, timeout=45)
    except asyncio.TimeoutError:
      await ctx.send(f"Bruh, {ctx.author.mention} why didn't you reply")
    return reply
    
  # Asks the user questions which are passed as arguments
  # to this function
  async def question(self, ctx, question_no, question):
    question += f"\n\nReply with your option {ctx.author.mention}"
    question_embed = discord.Embed(title=f'AVATAR ELEMENT QUIZ - QUESTION {question_no}', description=question, color=discord.Color.from_rgb(255, 255, 255))
    file=discord.File("ElementTest/avatar_thumbnail.jpg")
    question_embed.set_thumbnail(url="attachment://avatar_thumbnail.jpg")
    await ctx.send(embed = question_embed, file=file)

    def check(reply):
      return reply.author == ctx.author and reply.channel == ctx.channel
    try:
      reply = await self.client.wait_for("message", check=check, timeout=45)
    except asyncio.TimeoutError:
      await ctx.send(f"Bruh, {ctx.author.mention} why didn't you reply")
    return reply

  async def score_update(self, reply):
    stop = False
    if reply.content.lower() == 'a':
      self.score += 1
    elif reply.content.lower() == 'b':
      self.score += 2
    elif reply.content.lower() == 'c':
      self.score += 3
    elif reply.content.lower() == 'd':
      self.score += 4
    else:
      stop = True
    return stop

  # Checks what element the user should get based on their score
  # and sends an embedded message with the result
  async def reveal_element(self, ctx):
    if self.score == 1:
      title = "AIR NATION"
      description = f"{ctx.author.mention}, you got the air nation! Guess it's time to go bald then..."
      picture = air_emblem
      color = discord.Color.from_rgb(0, 250, 250)
    elif self.score == 2:
      title = "WATER NATION"
      description = f"{ctx.author.mention}, you got the water nation! Just keep me off your blood bending list though"
      picture = water_emblem
      color = discord.Color.from_rgb(0, 0, 100)
    elif self.score == 3:
      title = "EARTH NATION"
      description = f"{ctx.author.mention}, you got the earth nation! Time to embrace your inner badgermole"
      picture = earth_emblem
      color = discord.Color.from_rgb(0,100,0)
    elif self.score == 4:
      title = "FIRE NATION"
      description = f"{ctx.author.mention}, you got the fire nation! Flameo Hotman... or whatever the new kids say"
      picture = fire_emblem
      color = discord.Color.from_rgb(175, 0, 0)

    result_embed = discord.Embed(title = title, description = description, color = color)
    result_embed.set_thumbnail(url = picture)
    await ctx.send(embed = result_embed)
  
def setup(client):
  client.add_cog(Element_Test(client))