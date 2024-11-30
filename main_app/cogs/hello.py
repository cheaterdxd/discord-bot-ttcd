from discord.ext import commands

class Hello(commands.Cog):
	def __init__(self, client:commands.Bot):
		self.client = client # sets the client variable so we can use it in cogs

	@commands.Cog.listener()
	async def on_ready(self):
		print("hello loaded successfully")
		# an example event with cogs
	
	@commands.command(name="hello")
	async def hello(self, ctx:commands.Context):
	# an example command with cogs
		# await self.client.say("Hello")
		await ctx.reply("hello", ephemeral=True)

async def setup(client):
	await client.add_cog(Hello(client))