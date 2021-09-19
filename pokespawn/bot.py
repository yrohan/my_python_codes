# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pandas as pd
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')

def file_check(file_name):
	fcheck = os.path.isfile("C:/Users/Linux/Documents/pokespawn/" + file_name)
	return fcheck

gen1_starters = ['bulbasaur','squirtle','charmander']
picked_pokemon = ""
tot_server_messages = 0
poke_data = pd.read_csv("C:/Users/Linux/Documents/pokespawn/gen1db.csv")
all_pokemon_list = []
for i in range(0,151):
	all_pokemon_list.append(poke_data["PokeName"][i])

def upd_sel_numbers(file_name):
	db_file2 = pd.read_csv("C:/Users/Linux/Documents/pokespawn/" + file_name)
	n = len(db_file2["SNo"])
	for i in range(0,n):
		db_file2["SNo"][i] = i+1

'''def level_up():
def exp_gain():'''

def pokemon_spawn_name():
	poke_number = random.randint(0,len(all_pokemon_list))
	pokemon_spawned = all_pokemon_list[poke_number]
	db_spawns = open("C:/Users/Linux/Documents/pokespawn/spawn.txt", "w")
	db_spawns.write(pokemon_spawned.lower())
	db_spawns.close()



def random_spawns():
	global tot_server_messages
	has_spawned = 0
	can_spawn = random.randint(0,100)
	
	if tot_server_messages == 10 and can_spawn >= 0:
		has_spawned = 1
		tot_server_messages = 0
		pokemon_spawn_name()
	else:
		has_spawned = 0
	return has_spawned

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to discord!')
	
@bot.event
async def on_message(message):
	global tot_server_messages
	
	bad_words = ["fuck","lick","kill"]
	commands = [".start",".pick",".catch",".turnoff"]
	
	content_of_msg = message.content.lower()
	if message.author == bot.user:
		return
	elif content_of_msg in bad_words:
		for word in bad_words:
			if message.content.lower().count(word) > 0:
				await message.channel.purge(limit=1)
				await message.channel.send("Warning " + message.author.mention + " you have used a bad word.")
	else:
		tot_server_messages = tot_server_messages + 1
	
	for command in commands:
		if message.content.count(command) == 1:
			await bot.process_commands(message)
	
	if content_of_msg == ".help":
		embed_txt = discord.Embed(color = discord.Color.orange(),title = "Help", description = "Commands Available")
		embed_txt.add_field(name = ".start", value = "It lets you start playing")
		embed_txt.add_field(name = ".pick", value = "It lets you pick a starter after you have used .start")
		embed_txt.add_field(name = ".catch", value = "It catches any wild pokemon that appears")
		embed_txt.add_field(name = ".select", value = "It lets you select pokemon with the number it was stored (it is not the same as dex number)")
		embed_txt.add_field(name = ".turnoff", value = "It logs off the bot")
		await message.channel.send(content = None, embed = embed_txt)
	
	poke_spawn = random_spawns()
	if poke_spawn == 1:
		db_spawns = open("C:/Users/Linux/Documents/pokespawn/spawn.txt","r")
		spawn_poke_name = db_spawns.readline()
		poke_name = spawn_poke_name.strip()
		db_spawns.close()
		file_name = poke_name + ".png"
		sprite_path = "C:/Users/Linux/Documents/pokespawn/normal/" + file_name
		file_url = "attachment://" + file_name
		print(file_name)
		poke_sprite = discord.File(sprite_path,filename = file_name)
		embed_txt = discord.Embed(color = discord.Color.blue(), title = "A wild pokémon has appeared.", description = "Use .catch <pokemon> to catch the pokemon")
		embed_txt.set_image(url = file_url)
		await message.channel.send(file = poke_sprite, embed = embed_txt)

@bot.command(name = 'start', help = 'pick a starter to play')
async def display_starters(ctx):
	img_name = "oshoB.png"
	img_path = "C:/Users/Linux/Documents/pokespawn/oshoB.png"
	img_url = "attachment://oshoB.png"
	starters_img = discord.File(img_path, filename = img_name)
	embed_txt = discord.Embed(color = discord.Color.green(), title = "Start", description = "use .pick <pokemon> to pick your starter") 
	embed_txt.add_field(name = "Gen 1", value= gen1_starters[0] + ", " + gen1_starters[1] + ", " + gen1_starters[2] + "\n")
	embed_txt.set_image(url = img_url)
	print(embed_txt.image.width, embed_txt.image.height, embed_txt.image.url)
	await ctx.send(file = starters_img, embed = embed_txt)

@bot.command(name = 'pick', help = 'name the starter you want to pick')
async def let_user_pick(ctx, starter_name: str):
	global picked_pokemon
	member_mention = ctx.message.author.mention
	member_name = ctx.message.author.name
	file_name = member_name + ".csv"
	response = ""
	val = file_check(file_name)
	if val:
		response = "You have already picked a starter."
		return
	else:
		db_file = open(file_name, "w")
		db_file.write("SNo,PokeName,Level")
		db_file.write("\n")
	
	print(val,response)
	print(len(gen1_starters))
	print(starter_name)

	for i in range(0,len(gen1_starters)):
		if starter_name == gen1_starters[i]:
			picked_pokemon = gen1_starters[i]
			break
		else:
			picked_pokemon = ""
	
	if picked_pokemon == "":
		response = 'Wrong starter name please Try again '
		await ctx.send(response)
		db_file.close()
		return
	else:
		db_file.write("1," + picked_pokemon + ",5")
		response = 'Congratulations ' + member_mention + 'you have picked a level 5 ' + picked_pokemon
		db_file.close()
		await ctx.send(response)


@bot.command(name = 'select', help = 'lets you select a pokemon from list of pokemons you have caught')
async def selpoke(ctx,num: int):
	member_mention = ctx.message.author.mention
	member_name = ctx.message.author.name
	file_name = member_name + ".csv"
	db_file2 = open("C:/Users/Linux/Documents/pokespawn/" + file_name)
	n = len(db_file2["SNo"])
	if num <= n:
		poke_name = db_file2["PokeName"][num]
		await ctx.send("Congratulations " + member_mention + " you have selected your " + poke_name)
	else:
		await ctx.send(member_mention + " you don't have pokémon with this number.")

@bot.command(name = 'catch', help = 'lets you catch a wild pokemon')
async def catchpoke(ctx, pokemon_name: str):
	i = 0
	member_mention = ctx.message.author.mention
	member_name = ctx.message.author.name
	await asyncio.sleep(2)
	db_spawns = open("C:/Users/Linux/Documents/pokespawn/spawn.txt","r")
	spawn_poke_name = db_spawns.readline()
	poke_name = spawn_poke_name.strip()
	db_spawns.close()
	file_name = member_name + ".csv"
	print("In catch command")
	print(poke_name)
	random_level = random.randint(1,50)
	val = file_check(file_name)
	if val:
		db_file = open(file_name,"a")
	else:
		await ctx.send(member_mention + " You have not picked a starter. Please pick a starter to start catching Pokemon.")
		return
	
	if poke_name == pokemon_name.lower():
		response = 'Congratulations ' + member_mention + ' you have caught a level ' + str(random_level) + ' ' + pokemon_name
		db_file.write("," + pokemon_name + "," + str(random_level))
		upd_sel_numbers(file_name)
		os.remove("C:/Users/Linux/Documents/pokespawn/spawn.txt")
	else:
		response = ' No Wild Pokémon available '
	
	db_file.close()
	await ctx.send(response)
	
@bot.command(name = 'turnoff', help = 'logs out bot')
async def logoff(ctx):
	await ctx.send('logging off')
	await bot.close()

bot.run(TOKEN)