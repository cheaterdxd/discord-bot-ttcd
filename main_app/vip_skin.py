from discord.ext import commands
from discord import Message, Embed, Color
from utils import debug_log as dbl

class skin_message(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin_COGS loaded successfully")
        # an example event with cogs

    @commands.Cog.listener()
    async def on_message(self, message:Message):
        dbl.info(f"message detected: {message}")
        if message.author == self.bot.user:
            return
        
        print(f"Message from {message.author}: {message.content}")

        # Example: Reply to a specific keyword
        if "hello" in message.content.lower():
            await message.channel.send(f"Hello, {message.author.mention}!")

        embed_vip = Embed(
            title=f"{message.author}",
            color=Color.yellow()  # Yellow foreground
        )

        # Add fields for more text
        embed_vip.add_field(name="Tin nhắn", value=message.content, inline=False)
        # embed.add_field(name="Field 2", value="You can style this further!", inline=False)

        # Set footer and author
        embed_vip.set_footer(text="Sponsored by TTCD Vip Skin")

        # Set a thumbnail or image (optional)
        # embed.set_thumbnail(url="https://example.com/some-image.png")  # Add a valid image URL

        # Pass to command processing if needed
        await message.edit(embed=embed_vip)
        await self.bot.process_commands(message)


    # # Load a Cog
    # @commands.command(name="load")
    # @commands.is_owner()
    # async def load_cog(self, ctx:commands.Context, extension: str):
    #     try:
    #         await self.bot.load_extension(f"cogs.{extension}")
    #         await ctx.reply(f"Loaded `{extension}` successfully.", ephemeral=True)
    #     except Exception as e:
    #         await ctx.reply(f"Failed to load `{extension}`. Error: {e}", ephemeral=True)


async def setup(bot):
    await bot.add_cog(skin_message(bot))