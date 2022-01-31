import discord

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

newnick = 'lol'
restricted_words = []
f = open("words.txt", "r")
for x in f:
  x.strip()
  restricted_words.append(x)
@client.event
async def on_message(message):

  #CHECK IF MESSAGE IS FROM BOT
  if message.author == client.user:
    return

  #ADD NEW WORD
  if message.content.startswith('!add'):    
    newword = message.content.lstrip('!add ')
    print(newword)
    f = open("words.txt", "a")
    f.write(newword)
    f.write('\n')
    f.close()
    restricted_words.append(newword)
    print(restricted_words)
    await message.channel.send('Word added')
    return

  #CHANGE NICK TO 'ok' IF MESSAGE IS 'change'
  if message.content == 'change':
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


client.run('OTM3MTA0ODEzNjkzNTAxNTEw.YfW43g.Nc1K04L0FXsA5q-FyoG_bS0Xbes')
