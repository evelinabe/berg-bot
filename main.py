
import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = intents=discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents, ssl=False)

@bot.event
async def on_ready():
    print('bot ready')

@bot.event
async def on_message(message):

	if message.content == "hello":

		await message.channel.send("Hello, {}! How are you?".format(message.author.name))

@bot.event
async def on_message(message):
	if message.content == "how are you?":
		await message.channel.send("Very good, very good indeed {}! Thanks for asking.".format(message.author.name))

bot.run(DISCORD_TOKEN)
