from discord.ext import commands

class CurrentContextQuickAction(commands.Cog):
	def __init__(self, client:commands.Bot):
		self.client = client # sets the client variable so we can use it in cogs

	@commands.Cog.listener()
	async def on_ready(self):
		print("Current Context Quick Action loaded successfully")
		# an example event with cogs
	@commands.command()
	async def list_user(self, ctx:commands.Context):
		"""
        Retrieves and displays a list of users currently in the channel.

        This function fetches all members present in the channel where the command is invoked,
        compiles their display names into a string, and sends this list as an ephemeral message
        to the user who invoked the command.

        Parameters:
        interaction (discord.Interaction): The interaction object representing the command invocation.It contains information about the context in which the command was used.

        Returns:
        None: This function doesn't return any value. It sends a message through Discord's API.
        """
		members = ctx.channel.members
		output = ""
		for i in members:
			output += i.display_name + "\n"
		await ctx.channel.send(f"{output}", ephemeral=True)

async def setup(client):
	await client.add_cog(CurrentContextQuickAction(client))