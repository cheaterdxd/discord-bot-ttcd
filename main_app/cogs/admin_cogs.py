from discord.ext import commands
from utils import debug_log

class AdminCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin_COGS loaded successfully")
		# an example event with cogs

    # Load a Cog
    @commands.command(name="load")
    @commands.is_owner()
    async def load_cog(self, ctx:commands.Context, extension: str):
        try:
            await self.bot.load_extension(f"cogs.{extension}")
            await ctx.reply(f"Loaded `{extension}` successfully.", ephemeral=True)
            debug_log.success(f"Loaded {extension} successfully.")
        except Exception as e:
            await ctx.reply(f"Failed to load `{extension}`. Error: {e}", ephemeral=True)

    # Unload a Cog
    @commands.command(name="unload")
    @commands.is_owner()
    async def unload_cog(self, ctx:commands.Context, extension: str):
        try:
            await self.bot.unload_extension(f"cogs.{extension}")
            await ctx.reply(f"Unloaded `{extension}` successfully.", ephemeral=True)
            debug_log.success(f"Unloaded {extension} successfully.")
        except Exception as e:
            await ctx.reply(f"Failed to unload `{extension}`. Error: {e}", ephemeral=True)

    # Reload a Cog
    @commands.command(name="reload")
    @commands.is_owner()
    async def reload_cog(self, ctx:commands.Context, extension: str):
        try:
            await self.bot.unload_extension(f"cogs.{extension}")
            await self.bot.load_extension(f"cogs.{extension}")
            await ctx.reply(f"Reloaded {extension}` successfully.", ephemeral=True)
            debug_log.success(f"Reloaded {extension} successfully.")
        except Exception as e:
            await ctx.reply(f"Failed to reload `{extension}`. Error: {e}", ephemeral=True)
async def setup(bot):
	await bot.add_cog(AdminCog(bot))
# # Adding the admin cog to the bot
# bot = commands.Bot(command_prefix="!")
# bot.add_cog(AdminCog(bot))

# # Loading all Cogs on startup
# for filename in os.listdir("./cogs"):
#     if filename.endswith(".py"):
#         bot.load_extension(f"cogs.{filename[:-3]}")

# bot.run("YOUR_BOT_TOKEN")
