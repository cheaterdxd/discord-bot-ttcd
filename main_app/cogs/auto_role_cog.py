from discord.ext import commands
from admin_panel import alertor_javis
from utils import custom_error, debug_log
import os, dotenv, discord
from auto_job import auto_role
from main_app.Bot_custom import Bot_with_javis


# if DEBUG == "tuan":
#     CHANNEL_ID = 902626872725217305
# elif DEBUG == "ttcd":
#     MY_GUILD = discord.Object(id=868410572369174539) # Trung tâm Chí Dũng guild
#     CHANNEL_ID = os.getenv(f"STARTUP_ROLE_VIEW_CHANNEL_ID_{DEBUG}")
#     print(type(CHANNEL_ID))
# elif DEBUG == "bkt":
#     MY_GUILD = discord.Object(id=895928190772609035) # BKT guild


dotenv.load_dotenv()
RUN = os.getenv("RUN") 
GUILD_ID = os.getenv(f"{RUN}+_GUILD_ID")
START_ROLE_VIEW_CHANNEL_ID = os.getenv(f"STARTUP_ROLE_VIEW_CHANNEL_ID_{RUN}") 
startup_role_view_messsage_id = os.getenv(f"STARTUP_ROLE_VIEW_ID_{RUN}")


class auto_role_bot(commands.Cog):
    set_persistent = False

    def __init__(self, bot:Bot_with_javis):
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
        self.bot.javis = alertor_javis.alartor_JAVIS(guild) # alart man for administration
        debug_log.success("javis init for bot")
    
    
    async def pre_init(self):
        """
        Init view of the role view
        """
        # init persistent view
        self.init_view_get_role(auto_role.startup_get_role_view(timeout=None))


        # send init view if not already
        if str(startup_role_view_messsage_id) == '0' and startup_role_view_messsage_id != None: # check if autorole message is already available
            debug_log.error(f"Chưa có gửi view vào kênh")
            
            channel_get_role = self.bot.get_channel(int(START_ROLE_VIEW_CHANNEL_ID))

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
                    dotenv.set_key(".env",f"STARTUP_ROLE_VIEW_ID_{RUN}",str(mes.id))
                    debug_log.success("Tạo startup role view thành công và cập nhật ID thành công.")
                except Exception as e:
                    debug_log.error(f"Lỗi gửi tin nhắn: {str(e)}")            
            else:
                debug_log.error("Channel not found!")
        else:
            debug_log.info("View gắn role đã được gửi.")
        # init javis + check if log channel exists (if not, raise exception)
        try:
            for g in self.bot.guilds:
                debug_log.info(f" g.id = {g.id}, type = {type(g)}")
                debug_log.info(f" GUILD_ID = {GUILD_ID}, type = {type(GUILD_ID)}")
                if str(g.id) == GUILD_ID:
                    self.init_javis(g)
        except custom_error.NotFoundAdminLogChannelException as e1:
            debug_log.error(f"Chưa có channel cho admin_log")
            # await client._connection.close()
            await self.bot.close()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} loaded successfully")
        await self.pre_init()
		# an example event with cogs

async def setup(bot):
	await bot.add_cog(auto_role_bot(bot))