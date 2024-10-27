import discord, os, dotenv
from admin_panel import alertor_javis
from utils import custom_error

dotenv.load_dotenv()
DEBUG = os.getenv("DEBUG")
GUILD_ID = os.getenv(str(DEBUG)+"_guild")

class MyClient(discord.Client):
    """
        Initializes a new instance of the MyClient class.

        Args:
            intents (discord.Intents): The intents to be used by the client.

        Returns:
            None
    """
    alertor_javis = None
    def __init__(self, *, intents: discord.Intents, guild):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = discord.app_commands.CommandTree(self)
        self.MY_GUILD = guild
        self.set_persistent = False
        # self.alertor_javis = None
    
    async def init_view_get_role(self, view):
        """
            Add a persistent view to the command tree.
        """
        if self.set_persistent == False:
            self.add_view(view)
            self.set_persistent = True

    def init_javis(self, guild):
        """
            Initialize alertor_javis class.
        """

        # guild_object = self.get_guild(GUILD_ID)
        print(guild)
        print(type(guild))
        if guild is None:
            raise custom_error.GuildNotFoundException(f"Init Alertor Javis suspended because no guild object. Information:\nguild_object: {guild}")
        self.alertor_javis = alertor_javis.alartor_JAVIS(guild) # alart man for administration

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=self.MY_GUILD)
        await self.tree.sync(guild=self.MY_GUILD)