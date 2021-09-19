# bot1.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN1')


default_prefix = 'r!'
custom_prefix = ''
async def get_pre(bot,message):
	if custom_prefix == '':
		prefix = default_prefix
	else:
		prefix = custom_prefix
	return prefix

bot = commands.Bot(command_prefix=get_pre)
bot.remove_command('help')

anime_x = 716888462011269142
bot_maker = 507288392875114506
perm_role_ids = [719581357155811360,719582051300540567,719598194564137030,722408851965739138,722331193382666320,722331797605711883]


@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to discord!')
	game = discord.Game(name = 'Pokémon')
	await bot.change_presence(status = discord.Status.online, activity = game)


@bot.event
async def on_member_join(member):
	if member.guild.id == 734412017431085067:
		role = discord.utils.get(member.guild.roles, name = 'FRIEND')
		if role != None and role not in member.roles:
			await member.add_roles(role)
	elif member.guild.id == 718020463074476052:
		role1 = discord.utils.get(member.guild.roles, name = 'POKEFAN')
		#role2 = discord.utils.get(member.guild.roles, name = 'TRAINER')
		role3 = discord.utils.get(member.guild.roles, name = '•ADMIN•')
		if role1 != None and role1 not in member.roles:
			await member.add_roles(role1)
		#if role2 != None  and role1 not in member.roles:
			# await member.add_roles(role2)
		if role3 != None and member.id == bot_maker:
			member.add_roles(role3)


@bot.event
async def on_command_error(ctx,error):
	if isinstance(error, commands.CommandNotFound):
		pass
	

@bot.command(name = 'help', help = 'find help on a topic')
@commands.cooldown(1,300,commands.BucketType.user)
async def givehelp(ctx, arg = ''):
	global custom_prefix
	global default_prefix
	if custom_prefix == '':
		prefix = default_prefix
	else:
		prefix = custom_prefix
	if arg == '':
		embed_txt = discord.Embed(color = discord.Color.orange(),title = "Help", description = "Commands Available")
		embed_txt.add_field(name = prefix + "ping", value = "Pings the bot")
		embed_txt.add_field(name = prefix + "prefix", value = "Changes prefix of the bot")
		embed_txt.add_field(name = prefix + "give", value = "Gives a ROLE to a specified member")
		embed_txt.add_field(name = prefix + "take", value = "Revokes user from a ROLE")
		embed_txt.add_field(name = prefix + "find", value = "Allows user to find user with the ROLE")
		embed_txt.add_field(name = prefix + "rolesof", value = "Displays Roles of a user")
		embed_txt.add_field(name = prefix + "create", value = "Creates a ROLE")
		embed_txt.add_field(name = prefix + "delete", value = "Deletes a ROLE")
		embed_txt.add_field(name = prefix + "log", value = "Makes a Log in a channel")
		embed_txt.add_field(name = prefix + "rmvrlall", value = "Removes a ROLE from all members in Server")
		embed_txt.add_field(name = prefix + "gvrlall", value = "Gives a ROLE to all members in Server")
		embed_txt.add_field(name = prefix + "npart", value = "Finds Number of Participants")
		embed_txt.add_field(name = prefix + "bfmt", value = "Makes a random battle bracket.")
		embed_txt.add_field(name = prefix + "genrand", value = "Generates Random Number between 2 values a user inputs")
		embed_txt.add_field(name = prefix + "turnoff", value = "It logs off the bot")
		await ctx.send(content = None, embed = embed_txt)
	elif arg == 'give':
		embed_txt = discord.Embed(color = discord.Color.blue(),title = "Give Role", description = "Give Role by " + prefix + "give " + ctx.message.author.mention + " ROLE.")
		embed_txt.add_field(name = "ROLE NAME", value = "ROLE should be the exact Role Name.")
		embed_txt.add_field(name = "ROLE WITH SPACES", value = "If the Role has space in between then send Role Name like HO-OH where role name is HO OH")
		await ctx.send(content = None, embed = embed_txt)
	elif arg == 'take':
		embed_txt = discord.Embed(color = discord.Color.blue(),title = "Take Role", description = "Take Role by " + prefix + "take " + ctx.message.author.mention + " ROLE.")
		embed_txt.add_field(name = "ROLE NAME", value = "ROLE should be the exact Role Name.")
		await ctx.send(content = None, embed = embed_txt)
	elif arg == 'prefix':
		embed_txt = discord.Embed(color = discord.Color.blue(),title = "Set Prefix", description = "Set Prefix by " + prefix + "prefix  a.")
		embed_txt.add_field(name = "STRING", value = "a should be a Valid String(A-Z,0-9).")
		await ctx.send(content = None, embed = embed_txt)
	elif arg == 'find':
		embed_txt = discord.Embed(color = discord.Color.blue(),title = "Find User with ROLE", description = "Find User using " + prefix + "find ROLE.")
		embed_txt.add_field(name = "ROLE NAME", value = "ROLE should be the exact Role Name.")
		await ctx.send(content = None, embed = embed_txt)
	else:
		await ctx.send("The bot maker is currently working on it.")


@bot.command(name = 'genrand')
async def generate(ctx,startnum:int,endnum:int):
	if startnum < endnum:
		gennum = random.randint(startnum,endnum)
	elif startnum > endnum:
		gennum = random.randint(endnum,startnum)
	else:
		gennum = startnum
	await ctx.send(gennum)


@bot.command(name = 'find', help = "finds user with the ROLE")
@commands.cooldown(2,300,commands.BucketType.user)
async def find_user(ctx, *, role_name:str):
	global perm_role_ids
	has_perm = False
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	rlnm = "•" + role_name + "•"
	role = discord.utils.find(lambda r: r.name == role_name or r.name == role_name.upper() or r.name == role_name.lower() or r.name == rlnm or r.name == rlnm.upper() or r.name == rlnm.lower() or r.name == role_name.replace("-"," ") or r.name == role_name.replace("-"," ").lower() or r.name == role_name.replace("-"," ").upper(), ctx.message.guild.roles)
	member_with_role = None
	for member in ctx.message.guild.members:
		if role in member.roles:
			member_with_role = member
			break
	
	if role == None:
			await ctx.send("The role \"" + role_name + "\" does not exist.\nSee Command help if you want to find role with spaces.")
	elif member_with_role == None:
		await ctx.send("No Member with role \"" + role_name + "\" was found.")
	else:
		await ctx.send(member.mention + " has the role of " + role.name)


@bot.command(name = 'rolesof', help = 'displays all roles of a member')
@commands.cooldown(1,300,commands.BucketType.user)
async def all_role_find(ctx,user:discord.Member):
	global perm_role_ids
	has_perm = False
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	if has_perm == True:
		embedMsg = discord.Embed(title = user.name + " has the following role(s)\n",color = discord.Color.orange())
		role_names = []
		for role in user.roles:
			if role.name != '@everyone':
				role_names.append(role.name)
	
		for i in range(0,len(role_names)):
			embedMsg.add_field(name = 'Role ' + str(i+1), value = role_names[i])
		await ctx.send(content = None,embed=embedMsg)
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')


@bot.command(name = 'create')
async def make_new_role(ctx,*,role_name:str):
	global perm_role_ids
	has_perm = False
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	if has_perm == True:
		await ctx.guild.create_role(name = role_name, permissions = discord.Permissions(value=1024))
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')


@bot.command(name = 'delete')
async def del_role(ctx,*,role_name:str):
	global perm_role_ids
	has_perm = False
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	if has_perm == True:
		rlnm = "•" + role_name + "•"
		role = discord.utils.find(lambda r: r.name == role_name or r.name == role_name.upper() or r.name == role_name.lower() or r.name == rlnm or r.name == rlnm.upper() or r.name == rlnm.lower() or r.name == role_name.replace("-"," ") or r.name == role_name.replace("-"," ").lower() or r.name == role_name.replace("-"," ").upper(), ctx.message.guild.roles)
		await role.delete()
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')


'''@bot.command(name = 'rctrl')
async def mk_rct_rl(ctx,emoji:unicode,*,role_name:str):
	rlnm = "•" + role_name + "•"
	role = discord.utils.find(lambda r: r.name == role_name or r.name == role_name.upper() or r.name == role_name.lower() or r.name == rlnm or r.name == rlnm.upper() or r.name == rlnm.lower() or r.name == role_name.replace("-"," ") or r.name == role_name.replace("-"," ").lower() or r.name == role_name.replace("-"," ").upper(), ctx.message.guild.roles)
	if role != None:
		await ctx.send('React on the message to get ' + role.name + ' role.')
		await ctx.message.add_reaction(emoji)
	else:
		await ctx.send('No role with this name was found')

@bot.event
async def on_raw_reacion_add():
'''

'''@bot.command(name = 'enter')
async def let_mem_enter(ctx):
	role = discord.utils.get(ctx.message.guild.roles, name = 'quiz')
	if role != None:
		await ctx.author.add_roles(role)
		await ctx.send(ctx.author.mention + ' you have succesfully entered in ' + role.name)
	else:
		await ctx.send(role.name + ' was not found.')'''

'''
@bot.command(name = 'join')
@commands.cooldown(1,600,commands.BucketType.user)
async def add_mem_entry(ctx):
	role = discord.utils.get(ctx.message.guild.roles, name = 'TOURNAMENT')
	if role not in ctx.author.roles:
		await ctx.author.add_roles(role)
		await ctx.send(ctx.author.mention + ' you have successfully entered ' + role.name)
	else:
		await ctx.send(ctx.author.mention + ' you have already registered for tournament.')'''


@bot.command(name = 'leave')

@commands.cooldown(1,600,commands.BucketType.user)
async def rem_mem_entry(ctx):
	role = discord.utils.get(ctx.message.guild.roles, name = 'TOURNAMENT')
	if role in ctx.author.roles:
		await ctx.author.remove_roles(role)
		await ctx.send(ctx.author.mention + ' you have successfully quit from ' + role.name)
	else:
		await ctx.send(ctx.author.mention + ' you have not entered tournament.')


@bot.command(name = 'log')
async def mklog_gym(ctx,*,logval:str):
	global perm_role_ids
	has_perm = False
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.guild.id != 718020463074476052:
		channel = await bot.fetch_channel(733350343387250800)
	else:
		channel = ctx.message.channel
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	for role in ctx.author.roles:
		if role.name == 'LOG PERM':
			has_perm = True
	
	if has_perm == True:
		embedMsg = discord.Embed(title = '\u200b',description = logval,color=discord.Color.blue())
		await channel.send(embed=embedMsg)
	else:
		ctx.send("You dont have the permission to run this command.")
		
	

@bot.command(name = 'ping',aliases = ['p'])
async def do_ping(ctx):
	global perm_role_ids
	has_perm = False
	global perm_role_ids
	
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	if has_perm:	
		await ctx.send('Pong! {0}'.format(round(bot.latency,1)))
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')


@bot.command(name = 'prefix', help = 'changes current prefix of bot')
@commands.cooldown(1,600,commands.BucketType.user)
async def setprefix(ctx,nprefix:str):
	global perm_role_ids
	global custom_prefix 
	has_perm = False
	
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	
	if has_perm:
		prefix_db = open("C:/Users/Linux/Documents/discord_bots/prefix.txt", "w")
		prefix_db.write(nprefix)
		prefix_db.close()
		custom_prefix = nprefix
		await ctx.send("Prefix has been changed to " + nprefix)
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')



@bot.command(name = 'rmvrlall')
async def remove_from_all(ctx,*,role_name:str):
	global perm_role_ids
	has_perm = False
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	if has_perm == True:
		rlnm = "•" + role_name + "•"
		role = discord.utils.find(lambda r: r.name == role_name or r.name == role_name.upper() or r.name == role_name.lower() or r.name == rlnm or r.name == rlnm.upper() or r.name == rlnm.lower() or r.name == role_name.replace("-"," ") or r.name == role_name.replace("-"," ").lower() or r.name == role_name.replace("-"," ").upper(), ctx.message.guild.roles)
		for mem in ctx.guild.members:
			if role in mem.roles and role != discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles) :
				await mem.remove_roles(role)
			elif role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				ctx.send(role.name + ' cannot be removed from all.')
		await ctx.send(role.name + ' was removed from all users in the server.')
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')


@bot.command(name = 'give', help = 'gives role to a user',aliases = ['gv'])
async def give_role(ctx, user:discord.Member, *, role_name:str):
	global perm_role_ids
	has_perm = False
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	if has_perm:
		rlnm = "•" + role_name + "•"
		role = discord.utils.find(lambda r: r.name == role_name or r.name == role_name.upper() or r.name == role_name.lower() or r.name == rlnm or r.name == rlnm.upper() or r.name == rlnm.lower() or r.name == role_name.replace("-"," ") or r.name == role_name.replace("-"," ").lower() or r.name == role_name.replace("-"," ").upper(), ctx.message.guild.roles)
		if role == None:
			await ctx.send("The role \"" + role_name + "\" does not exist. If name of ROLE has spaces see help for give.")
		elif role not in user.roles:
			await user.add_roles(role)
			await ctx.send(role.name + " ROLE was given to " + user.mention)
		else:
			await ctx.send(user.mention + " already has the " + role.name)
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')


@bot.command(name = 'gvrlall')
async def remove_from_all(ctx,*,role_name:str):
	global perm_role_ids
	has_perm = False
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	if has_perm == True:
		rlnm = "•" + role_name + "•"
		role = discord.utils.find(lambda r: r.name == role_name or r.name == role_name.upper() or r.name == role_name.lower() or r.name == rlnm or r.name == rlnm.upper() or r.name == rlnm.lower() or r.name == role_name.replace("-"," ") or r.name == role_name.replace("-"," ").lower() or r.name == role_name.replace("-"," ").upper(), ctx.message.guild.roles)
		for mem in ctx.guild.members:
			if not mem.bot:
				if role not in mem.roles and role != discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles) :
					await mem.add_roles(role)
				elif role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
					ctx.send(role.name + ' cannot be removed from all.')
		await ctx.send(role.name + ' was added to all users in the server.')
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')


@bot.command(name = 'take', help = 'rovokes role of a user',aliases = ['tk'])
async def take_role(ctx, user:discord.Member, *, role_name:str):
	global perm_role_ids
	has_perm = False
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	if has_perm:
		rlnm = "•" + role_name + "•"
		role = discord.utils.find(lambda r: r.name == role_name or r.name == role_name.upper() or r.name == role_name.lower() or r.name == rlnm or r.name == rlnm.upper() or r.name == rlnm.lower() or r.name == role_name.replace("-"," ") or r.name == role_name.replace("-"," ").lower() or r.name == role_name.replace("-"," ").upper(), ctx.message.guild.roles)
		if role == None:
			await ctx.send("The role \"" + role_name + "\" does not exist. If name of ROLE has spaces see help for take.")
		elif role in user.roles:
			await user.remove_roles(role)
			await ctx.send(role.name + " ROLE was taken from " + user.mention)
		else:
			await ctx.send(user.mention + " does not have the " + role.name)
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')


@bot.command(name = 'npart')
@commands.cooldown(1,1000,commands.BucketType.user)
async def number(ctx):
	global perm_role_ids
	global custom_prefix 
	has_perm = False
	
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	tot_part = 0
	mem_list = []
	if ctx.message.guild.id == 718020463074476052:
		role = discord.utils.get(ctx.message.guild.roles,name = 'TOURNAMENT')
	else:
		role = discord.utils.get(ctx.message.guild.roles,name = 'TOURNAMENT')
	for mem in ctx.guild.members:
		if role in mem.roles:
			tot_part += 1
			mem_list.append(mem.name)
	if has_perm == True:
		await ctx.send("We have " + str(tot_part) + " participants for tournament currently.")
		for i in range(len(mem_list)):
			await ctx.send(mem_list[i]+ " is in tournament.")
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')
		

@bot.command(name = 'bfmt')
async def sendbracket(ctx,*,role_name:str):
	global perm_role_ids
	global custom_prefix 
	has_perm = False
	
	for role in ctx.message.author.roles:
		for i in range(0,len(perm_role_ids)):
			if role == discord.utils.find(lambda r: r.id == perm_role_ids[i], ctx.message.guild.roles):
				has_perm = True
				break
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if ctx.message.guild.id != 718020463074476052 and ctx.message.author.id == anime_x:
		has_perm = True
	
	mem_list = []
	rlnm = "•" + role_name + "•"
	role = discord.utils.find(lambda r: r.name == role_name or r.name == role_name.upper() or r.name == role_name.lower() or r.name == rlnm or r.name == rlnm.upper() or r.name == rlnm.lower() or r.name == role_name.replace("-"," ") or r.name == role_name.replace("-"," ").lower() or r.name == role_name.replace("-"," ").upper(), ctx.message.guild.roles)
	for mem in ctx.guild.members:
		if role in mem.roles:
			mem_list.append(mem)
	random.shuffle(mem_list)
	if has_perm == True:
		for i in range(0,len(mem_list),2):
			await ctx.send(mem_list[i].mention + " has to battle " + mem_list[i+1].mention)
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')

@give_role.error
async def give_error(ctx, error):
	global default_prefix
	global custom_prefix
	if custom_prefix == '':
		prefix = default_prefix
	else:
		prefix = custom_prefix
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Invalid format of command. You should use ' + prefix + 'give @user ROLE_NAME.')
	elif isinstance(error, commands.BadArgument):
		await ctx.send('Invalid format of command. You should use ' + prefix + 'give @user ROLE_NAME.')
	elif isinstance(error, commands.TooManyArguments):
		await ctx.send('Invalid format of command. Please use ' + prefix + 'help give to see the correct usage')
	else:
		await ctx.send('Invalid format of command. Please use ' + prefix + 'help give to see the correct usage')	


@take_role.error
async def take_error(ctx, error):
	global default_prefix
	global custom_prefix
	if custom_prefix == '':
		prefix = default_prefix
	else:
		prefix = custom_prefix
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Invalid format of command. You should use ' + prefix + 'take @user ROLE_NAME.')
	elif isinstance(error, commands.BadArgument):
		await ctx.send('Invalid format of command. You should use ' + prefix + 'take @user ROLE_NAME.')
	elif isinstance(error, commands.TooManyArguments):
		await ctx.send('Invalid format of command. Please use ' + prefix + 'help take to see the correct usage')
	else:
		await ctx.send('Invalid format of command. Please use ' + prefix + 'help take to see the correct usage')


'''@add_mem_entry.error
async def add_mem_entry_err(ctx,error):
	if isinstance(error, commands.CommandOnCooldown):
		msg = 'The command is on cooldown of {:.2f} mins'.format((error.retry_after/60))
		await ctx.send(msg)@add_mem_entry.error'''


@rem_mem_entry.error
async def rem_mem_entry_err(ctx,error):
	if isinstance(error, commands.CommandOnCooldown):
		msg = 'The command is on cooldown of {:.2f} mins'.format((error.retry_after/60))
		await ctx.send(msg)



@generate.error
async def generror(ctx,error):
	global default_prefix
	global custom_prefix
	if custom_prefix == '':
		prefix = default_prefix
	else:
		prefix = custom_prefix
	if isinstance(error, commands.BadArgument):
		await ctx.send('Invalid format of command. Please use ' + prefix + 'genrand startnum endnum to generate random number between stating number and ending number')
	else:
		await ctx.send('Invalid format of command. Please use ' + prefix + 'genrand startnum endnum to generate random number between stating number and ending number')


@setprefix.error
async def prefix_error(ctx, error):
	global default_prefix
	global custom_prefix
	if custom_prefix == '':
		prefix = default_prefix
	else:
		prefix = custom_prefix
	if isinstance(error, commands.BadArgument):
		await ctx.send('Invalid format of command. You cannot set this as prefix for commands.')
	else:
		await ctx.send('Invalid format of command. Please use ' + prefix + 'help prefix to see the correct usage')


@find_user.error
async def find_user_error(ctx,error):
	global default_prefix
	global custom_prefix
	if custom_prefix == '':
		prefix = default_prefix
	else:
		prefix = custom_prefix
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Invalid format of command. You should use ' + prefix + 'find ROLE_NAME.')
	elif isinstance(error, commands.BadArgument):
		await ctx.send('Invalid format of command. You should use ' + prefix + 'find ROLE_NAME.')
	elif isinstance(error, commands.TooManyArguments):
		await ctx.send('Invalid format of command. Please use ' + prefix + 'help find to see the correct usage')
	elif isinstance(error, commands.CommandOnCooldown):
		msg = 'The command is on cooldown of {:.2f} mins'.format((error.retry_after/60))
		await ctx.send(msg)
	else:
		await ctx.send('Invalid format of command. Please use ' + prefix + 'help find to see the correct usage')	


@all_role_find.error
async def all_role_find_error(ctx,error):
	if isinstance(error, commands.CommandOnCooldown):
		msg = 'The command is on cooldown of {:.2f} mins'.format((error.retry_after/60))
		await ctx.send(msg)


@setprefix.error
async def setprefix_error(ctx,error):
	if isinstance(error, commands.CommandOnCooldown):
		msg = 'The command is on cooldown of {:.2f} mins'.format((error.retry_after/60))
		await ctx.send(msg)


@all_role_find.error
async def allrlfind_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('An error occured running this command.')
	else:
		await ctx.send('An error occured running this command.')


@remove_from_all.error
async def rmvrlall_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('An error occured running this command.')
	else:
		await ctx.send('An error occured running this command.')


@number.error
async def number_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('An error occured running this command.')
	elif isinstance(error, commands.CommandOnCooldown):
		msg = 'The command is on cooldown of {:.2f} mins'.format((error.retry_after/60))
		await ctx.send(msg)
	else:
		await ctx.send('An error occured running this command.')


@sendbracket.error
async def sendbracket_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('An error occured running this command.')
	else:
		await ctx.send('An error occured running this command.')


@make_new_role.error
async def mknewrl_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('An error occured running this command.')
	else:
		await ctx.send('An error occured running this command.')


@mklog_gym.error
async def mklog_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('An error occured running this command.')
	else:
		await ctx.send('An error occured running this command.')


@del_role.error
async def delrl_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('An error occured running this command.')
	else:
		await ctx.send('An error occured running this command.')


@bot.command(name = 'turnoff', help = 'logs out bot')
async def logoff(ctx):
	has_perm = False
	
	if ctx.message.author.id == bot_maker:
		has_perm = True
	if has_perm:
		await ctx.send('The bot is now going offline for maintenance.')
		await bot.close()
	else:
		await ctx.send(ctx.message.author.mention + ' you do not have the permission to run this command')

bot.run(TOKEN)