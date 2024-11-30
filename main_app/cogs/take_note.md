#### how to send a message with ephemeral in cogs
```python
	@commands.command(name="hello")
	async def hello(self, ctx:commands.Context):
	# an example command with cogs
		# await self.client.say("Hello")
		await ctx.reply("hello", ephemeral=True)
```