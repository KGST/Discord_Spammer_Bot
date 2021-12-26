# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
discordToken = os.getenv("Token")

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX.
bot = commands.Bot(command_prefix="$") #replacement for bot.client() as we want a bot object rather than a client for extra commands

#RUNS THE BASIC WEBSITE AND PINGED BY THIRD PARTY TO KEEP THE BOT ACTIVE 24/7
from keepRunning import keepAlive

@bot.event 
async def on_ready():
	print('Logged in as {0.user}'.format(bot))

#First event
@bot.event
async def on_message(message):
	#DEFINE functions and variables
	i = 0 #set counter variable
	# def milf(): DOESN'T WORK? SAYS AWAIT IS OUTSIDE OF THE ASYNC FUNCTION
	# 	# CHECK IF THE MESSAGE SENT TO THE CHANNEL IS "milf".
	# 	if message.content == "$milf":
	# 		# SENDS A MESSAGE TO THE CHANNEL.
	# 		await message.channel.send('I am thirsty for {}'.format(message.author.mention))

	#if the last message is sent by the bot, do nothing
	if message.author == bot.user: 
		return

	if message.content =="$megamilf":
		while i < 5:
			await message.channel.send('I am thirsty for {}'.format(message.author.mention))
			i += 1

	#INCLUDES THE COMMANDS FOR THE BOT; WITHOUT IT, COMMANDS WILL NOT BE PASSED THROUGH RESULTING IN NULL RETURN
	await bot.process_commands(message)


#COMMAND $milf. INVOKES ONLY WHEN THE MESSAGE "$milf" IS SENT IN THE DISCORD SERVER. 
@bot.command(
	# ADDS THIS VALUE TO THE $help gorl MESSAGE.
	help= "bro r u stupid or some shit?",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief= "man's down bad for a bot"
)
async def milf(ctx):
	await ctx.channel.send('I am thirsty for {}'.format(ctx.author.mention))

#COMMAND $gorl. INVOKES ONLY WHEN THE MESSAGE "$gorl" IS SENT IN THE DISCORD SERVER.
@bot.command(
	# ADDS THIS VALUE TO THE $help gorl MESSAGE.
	help="This mother fucker came back!? Go get your nose sharpened :skull:",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="tells Gru to fuck off"
)
async def gorl(ctx):
	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
	await ctx.channel.send("alright calm the fuck down Gru ya already got a wife that looks like slenderman")

# COMMAND $milfomatic. THIS TAKES AN IN A LIST OF ARGUMENTS FROM THE USER AND SIMPLY PRINTS THE VALUES BACK TO THE CHANNEL.
@bot.command(
	# ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
	help="make the bot down bad for anything (after the command)",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="makes the bot thirsty for whatever you type after $milfomatic"
)
async def milfomatic(ctx, *args):
	response = ""

	# LOOPS THROUGH THE LIST OF ARGUMENTS THAT THE USER INPUTS.
	for arg in args:
		response = response + " " + arg
	response = ('I am thirsty for {}'.format(response))
	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
	await ctx.channel.send(response)

#COMMAND MEGA MILF
@bot.command(
	# ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
	help="$milfomatic * 10",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="SPAM PING THE THIRSTINESS OF THIS BOT"
)
async def mega_milfomatic(ctx, *args):
	i = 0
	while i < 10:
		mmResponse = ""

		# LOOPS THROUGH THE LIST OF ARGUMENTS THAT THE USER INPUTS.
		for arg in args:
			mmResponse = mmResponse + " " + arg
	# if statement here for not pinging me
		mmResponse = ('I am thirsty for {}'.format(mmResponse))

		i += 1
		# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
		await ctx.channel.send(mmResponse)
		
#KEEPS WEBSITE RUNNING; IMPORTED FROM keepRunning.py
keepAlive()
# EXECUTES BOT WITH THE GIVEN TOKEN
bot.run(discordToken)