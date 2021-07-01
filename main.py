import discord, time, json

client = discord.Client()

config = json.load(open("config.json", "r"))

@client.event
async def on_connect():
	print("Starting...")
	channel = client.get_channel(config["channel_id"])
	while True:
		await channel.send("%fish")
		time.sleep(0.5)
		await channel.send("%sell all")
		time.sleep(3.5)

client.run(config["token"], bot=False)