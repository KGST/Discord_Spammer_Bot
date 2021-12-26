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

# CREATES A NEW BOT OBJECT WITH '$' PREFIX.
bot = commands.Bot(command_prefix="$") #replacement for bot.client() as we want a bot object rather than a client for extra commands (SUCH AS PINGING FUNCTIONALITY ON DISCORD)

#RUNS THE BASIC WEBSITE AND PINGED BY THIRD PARTY TO KEEP THE BOT ACTIVE 24/7 (without this the bot would go offline)
from keepRunning import keepAlive

@bot.event #REMEMBER IS ACTUALLY A CLIENT EVENT
async def on_ready():
	print('Logged in as {0.user}'.format(bot)) #GIVES CONFIRMATION THAT BOT IS ONLINE

#First event
@bot.event
async def on_message(message):
	i = 0 #set counter variable

	#if the last message is sent by the bot, do nothing
	if message.author == bot.user: 
		return

	if message.content =="$megaspam":
		while i < 5:
			await message.channel.send('How do you do {}'.format(message.author.mention))
			i += 1

	#INCLUDES THE COMMANDS FOR THE BOT; WITHOUT IT, COMMANDS WILL NOT BE PASSED THROUGH (RESULTING IN NULL RETURN)
	await bot.process_commands(message)


#COMMAND $milf. INVOKES ONLY WHEN THE MESSAGE "$milf" IS SENT IN THE DISCORD SERVER. 
@bot.command(
	# ADDS THIS VALUE TO THE $help MESSAGE.
	help= "read about the bot on KGST's github profile",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief= "spamm your friends lol"
)
async def spam(ctx):
	await ctx.channel.send('Spamming {}'.format(ctx.author.mention))

# COMMAND $spammer. THIS TAKES AN IN A LIST OF ARGUMENTS FROM THE USER AND SIMPLY PRINTS THE VALUES BACK TO THE CHANNEL.
@bot.command(
	# ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
	help="makes the bot say its time to spam +(whatever is after the command [can be a person's @ in discord])",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="makes the bot spam for whatever you type after $spam"
)
async def spammer(ctx, *args):
	response = ""

	# LOOPS THROUGH THE LIST OF ARGUMENTS THAT THE USER INPUTS.
	for arg in args:
		response = response + " " + arg
	response = ('It is time to spam {}'.format(response))
	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
	await ctx.channel.send(response)

#COMMAND MEGA SPAMMER
@bot.command(
	# ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
	help="$spammer * 10",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="SPAM PING WITH THE HELP OF THIS BOT"
)
async def mega_spammer(ctx, *args):
	i = 0
	while i < 10:
		mmResponse = ""

		# LOOPS THROUGH THE LIST OF ARGUMENTS THAT THE USER INPUTS.
		for arg in args:
			mmResponse = mmResponse + " " + arg
	# if statement here for not pinging me
		mmResponse = ('It is time to spam {}'.format(mmResponse))

		i += 1
		# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
		await ctx.channel.send(mmResponse)
		
#KEEPS WEBSITE RUNNING; IMPORTED FROM keepRunning.py
keepAlive()
# EXECUTES BOT WITH THE GIVEN TOKEN (THIS WILL HAVE TO BE YOUR UNIQUE TOKEN)
bot.run(discordToken)
