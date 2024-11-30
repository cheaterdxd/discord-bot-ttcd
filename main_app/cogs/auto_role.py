from discord.ext import commands
from admin_panel import alertor_javis
from utils import custom_error, debug_log
import os, dotenv, discord
from auto_job import auto_role
dotenv.load_dotenv()
DEBUG = os.getenv("DEBUG") 
startup_role_view_messsage_id = os.getenv("STARTUP_ROLE_VIEW_ID")
if DEBUG == "tuan":
    CHANNEL_ID = 902626872725217305
elif DEBUG == "ttcd":
    MY_GUILD = discord.Object(id=868410572369174539) # Trung tâm Chí Dũng guild
    CHANNEL_ID = os.getenv("STARTUP_ROLE_VIEW_CHANNEL_ID")
    print(type(CHANNEL_ID))
elif DEBUG == "bkt":
    MY_GUILD = discord.Object(id=895928190772609035) # BKT guild


class auto_role_bot(commands.Cog):
    alertor_javis = None
    set_persistent = False

    def __init__(self, bot:commands.Bot):
        self.bot = bot

    def init_view_get_role(self, view):
        """
        Add a persistent view to the command tree.
        """
        if self.set_persistent == False:
            self.bot.add_view(view)
            self.set_persistent = True

    def init_javis(self, guild):
        """
            Initialize alertor_javis class.
            Javis is used to send alerts to administrators channels.
        """

        # guild_object = self.get_guild(GUILD_ID)
        # print(guild)
        # print(type(guild))
        if guild is None:
            raise custom_error.GuildNotFoundException(f"Init Alertor Javis suspended because no guild object. Information:\nguild_object: {guild}")
        self.alertor_javis = alertor_javis.alartor_JAVIS(guild) # alart man for administration
    
    
    async def pre_init(self):
        # check available auto-role
        self.init_view_get_role(auto_role.startup_get_role_view(timeout=None))

        if str(startup_role_view_messsage_id) == '0' and startup_role_view_messsage_id != None: # check if autorole message is already available
            channel_get_role = self.bot.get_channel(int(CHANNEL_ID))

            if channel_get_role is not None:
                # Create the view
                view = auto_role.startup_get_role_view(timeout=None)
                
                # Create an embed with an image
                embed = discord.Embed(title="LẤY QUYỀN TRUY CẬP LỚP HỌC")
                file_img = discord.File("resource\\image\\auto_role_tutorial.png", filename="auto_role_tutorial.png")
                embed.set_image(url="attachment://auto_role_tutorial.png")
                try:
                    # Send the message with the embed and view
                    mes = await channel_get_role.send(embed=embed, view=view, file=file_img)
                    dotenv.set_key(".env","STARTUP_ROLE_VIEW_ID",str(mes.id))
                    debug_log.success("Tạo startup role view thành công và cập nhật ID thành công.")
                except Exception as e:
                    debug_log.error(f"Lỗi gửi tin nhắn: {str(e)}")            
            else:
                debug_log.error("Channel not found!")
        else:
            debug_log.info("Startup role view message already exists.")
        # init javis + check if log channel exists (if not, raise exception)
        try:
            for g in self.bot.guilds:
                if g.id == MY_GUILD.id:
                    self.init_javis(g)
        except custom_error.NotFoundAdminLogChannelException as e1:
            debug_log.error(f"Chưa có channel cho admin_log")
            # await client._connection.close()
            await self.bot.close()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} loaded successfully")
		# an example event with cogs

async def setup(bot):
	await bot.add_cog(auto_role_bot(bot))