# bot1.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


default_prefix = 'r!'
custom_prefix = ''
async def get_pre(bot,message):
	if custom_prefix == '':
		prefix = default_prefix
	else:
		prefix = custom_prefix
	return prefix

bot = commands.Bot(command_prefix=get_pre)


@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to discord!')
	game = discord.Game(name = 'Pokémon')
	await bot.change_presence(status = discord.Status.online, activity = game)


queue = []            
	
@bot.event
async def on_message(message):
	global queue
	if message.content == "queue":
		print(len(queue))
		queue.append(message.author)
		if len(queue) == 1:
			await message.channel.send('Wait For Someone !')
		elif len(queue) == 2:
			await message.channel.send("Please Join A Game" + queue[0].mention + " " + queue[1].mention)
	global custom_prefix
	global default_prefix
	if custom_prefix == '':
		prefix = default_prefix
	else:
		prefix = custom_prefix
	said_bad_word = False
	said_good_word = False
	said_nuetr_word = False
	nuetral_words = ["arrow","ho-oh","please","fine","voila"]
	good_words = ["hula","yay","treats","spearow","fearow"]
	bad_words = ["fuck","lick","kill","shit"]
	commands = ["ping","say","prefix","avatar","turnoff"]
	
	content_of_msg = message.content.lower()
	msg_contents = content_of_msg.split()
	for i in range(0,len(msg_contents)):
		if msg_contents[i] in bad_words:
			said_bad_word = True

	for i in range(0,len(msg_contents)):
		if msg_contents[i] in good_words:
			said_good_word = True
	
	for i in range(0,len(msg_contents)):
		if msg_contents[i] in nuetral_words:
			said_nuetr_word = True
	
	if message.author == bot.user:
		return
	elif said_bad_word:
			await message.channel.purge(limit=1)
			await message.channel.send("Warning " + message.author.mention + " you have used a bad word.")
	elif said_good_word:
			await message.channel.send("Wohoo " + message.author.mention + " you have said a good word. You get a HO-OH.")
	elif said_nuetr_word:
			await message.channel.send(message.author.mention + " you are a Lugia so you dont get a HO-OH.")
	elif content_of_msg.count('pokeball') > 0:
			await message.channel.send(message.author.mention + " you have caught a ")
	elif content_of_msg.count('masterball') > 0:
			await message.channel.send(message.author.mention + " you have caught a ")
	
	for command in commands:
		command = prefix + command 
		if message.content.count(command) == 1:
			await bot.process_commands(message)
	
	help_comm = prefix + 'help'
	if message.content == help_comm:
		embed_txt = discord.Embed(color = discord.Color.orange(),title = "Help", description = "Commands Available")
		embed_txt.add_field(name = prefix + "ping", value = "pings the bot")
		embed_txt.add_field(name = prefix + "prefix", value = "changes prefix of the bot")
		embed_txt.add_field(name = prefix + "turnoff", value = "It logs off the bot")
		await message.channel.send(content = None, embed = embed_txt)


@bot.command(name = 'ping')
async def do_ping(ctx):
	await ctx.send('Pong! {0}'.format(round(bot.latency,1)))

@bot.command(name = 'avatar')
async def send_meme(ctx,user:discord.Member = None):
	if user == None:
		user = ctx.message.author
	
	embedMsg = discord.Embed(title = user.name + '\'s Avatar')
	embedMsg.set_image(url= user.avatar_url)
	await ctx.send(content = None,embed = embedMsg)


@bot.command(name = 'say')
async def rep_msg(ctx,*,sent:str):
	await ctx.send(sent)

@bot.command(name = 'prefix')
async def setprefix(ctx,nprefix):
	global custom_prefix 
	custom_prefix = nprefix

@bot.command(name = 'turnoff', help = 'logs out bot')
async def logoff(ctx):
	await ctx.send('logging off')
	await bot.close()
	
bot.run(TOKEN)