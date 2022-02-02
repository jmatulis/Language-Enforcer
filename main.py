import discord
import os 
from keep_alive import keep_alive
from discord.ext import commands

my_secret = os.environ['TOKEN']
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def embed(ctx):
  embedVar=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
  await ctx.channel.send(embed = embedVar)

@client.command()
async def restricted(ctx):
  server = ctx.guild.name.strip(' ')
  file = f'{server}_words.txt'
  try:
    f = open(file, "r")
  except:
    await ctx.channel.send("No restricted words yet. Try !add <word>")
  if(os.stat(file).st_size == 0):
    await ctx.channel.send("No restricted words yet. Try !add <word>")
  for x in f:
    await ctx.channel.send(x.strip())
  f.close()


@client.command()
async def helpme(ctx):
  await ctx.channel.send("!restricted - displays retristed words\n!add <word> - add words to restricted list")

#@client.command()
#async def remove(ctx,*, word):
  #REMOVE WORD
 # server = ctx.guild.name.strip(' ')
 # file = f'{server}_words.txt'
 # f = open(file, "w+")
 # Lines = f.readlines()
  #for line in Lines:
  #  if(line.strip() == word):
      
  #    f.close()
  #   return
  #f.close()
  #print(newword)
  #f = open(file, "a")
  #f.write(newword.strip())
  #f.write('\n')
  #f.close()
  #newword.strip()
  #await ctx.channel.send('Word added')
  #return

@client.command()
async def add(ctx, *, newword):
  #ADD NEW WORD
  server = ctx.guild.name.strip(' ')
  file = f'{server}_words.txt'
  f = open(file, "r+")
  Lines = f.readlines()
  for line in Lines:
    if(line.strip() == newword):
      await ctx.channel.send('Word is already restricted.')
      f.close()
      return
  f.close()
  print(newword)
  f = open(file, "a")
  f.write(newword.strip())
  f.write('\n')
  f.close()
  newword.strip()
  await ctx.channel.send('Word added')
  return


@client.command()
async def setstrikes(ctx):
  await ctx.channel.send("Hi")



@client.event
async def on_message(message):
  #CHECKS TO SEE IF IT IS A COMMAND
  await client.process_commands(message)
  if(message.content.startswith("!")):
    return
  #CHECK IF MESSAGE IS FROM BOT
  if message.author == client.user:
    return
  server = message.author.guild.name.strip(' ')
  file = f'{server}_words.txt'
  restricted_words = []
  f = open(file, "a+")
  f.close()
  f = open(file, "r")
  for x in f:
    restricted_words.append(x.strip())
  f.close()


  #CHANGE NICK TO 'ok' IF MESSAGE IS 'change'
  if message.content == 'penis':
    await message.author.edit(nick="ok")
  
  
  nick = message.author.nick
  #CHECK FOR RESTRICTED WORD IN MESSAGE AND ADDS '(Strike: #)' TO NICK
  for word in restricted_words:
    if message.content.lower().count(word) > 0:
      await message.channel.send('Do not do that')
      if nick.count('(Strike: 1)')>0:
        nick = nick[:-11]
        await message.author.edit(nick = nick+'(Strike: 2)')
      elif nick.count('Strike: 2')>0:
        nick = nick[:-11]            
        await message.author.edit(nick = nick+'(Strike: 3)')
        await message.author.kick(reason = 'Cringe')
        await message.channel.send(f'{message.author.nick} has been kicked from the server')
        return
      else:
        print('O')
        await message.author.edit(nick=nick+f" (Strike: 1)") 
        await message.channel.send(f'Nickname changed for {message.author.mention}')

keep_alive()
client.run(os.getenv('TOKEN'))
