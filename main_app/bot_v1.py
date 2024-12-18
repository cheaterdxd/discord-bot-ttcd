import dotenv, os, pandas as pd, colorama, asyncio, traceback, discord
from main_app.Bot_custom import MyClient
from auto_job import auto_role
from utils import debug_log, custom_error
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN_DISCORD")
startup_role_view_messsage_id = os.getenv("STARTUP_ROLE_VIEW_ID")
DEBUG = os.getenv("DEBUG") # in debug mode, bot will delay at 5 minuts = 300 in diem danh
debug_log.info(DEBUG)
# debug_log.set_debug_mode(DEBUG)

MY_GUILD = discord.Object(id=os.getenv(str(DEBUG)+"_guild")) 

if DEBUG == "tuan":
    CHANNEL_ID = 902626872725217305
elif DEBUG == "ttcd":
    MY_GUILD = discord.Object(id=868410572369174539) # Trung tâm Chí Dũng guild
    CHANNEL_ID = os.getenv("STARTUP_ROLE_VIEW_CHANNEL_ID")
    print(type(CHANNEL_ID))
elif DEBUG == "bkt":
    MY_GUILD = discord.Object(id=895928190772609035) # BKT guild

intents = discord.Intents.all() # enable all gateway intents
intents.members = True
client = MyClient(intents=intents, guild=MY_GUILD) # initialize the client bot
stop_check_class = False # check status of continue diemdanh

if "ttcd" in DEBUG:# sài thật
    delay_time_at_diemdanh = 300 # 5 phut
    delete_after_at_diemdanh = 200
else: # đang code
    delay_time_at_diemdanh = 5 # 5 giay
    delete_after_at_diemdanh = 3

def get_class_user_displayname_from_danh_sach(class_name: str) -> list:
    """Hàm sử dụng để lấy danh sách học viên từ file danhsachlop.xlsx

    Args:
        class_name (str): tên lớp

    Returns:
        list: danh sách tên hiển thị của các học viên trong lớp
    """
    if class_name != "":
        # Read a specific sheet by index (e.g., sheet2)
        try:
            class_type_df: pd.DataFrame = pd.read_excel('danhsachlop.xlsx', sheet_name="type_of_class") # đọc file excel điểm danh ở tab type_of_class
            major_column_list = list(class_type_df.items()) # đọc các dòng trong tab --> mỗi dòng là 1 lớp
            sheet_contain_class = ""

            # mỗi dòng sẽ là 1 lớp, cần lấy thông tin lớp để diemdanh
            for major_col in major_column_list:
                if (class_name in list(major_col[1])):
                    sheet_contain_class = major_col[1].name
                    class_in_type_df: pd.DataFrame = pd.read_excel('danhsachlop.xlsx', sheet_name=sheet_contain_class)
                    print(f"found class in {sheet_contain_class}")
                    for col in list(class_in_type_df.items()):
                        print(col)
                        if(col[1].name == class_name):
                            return [user_name.strip().strip("\n") for user_name in  list(col[1])] # trả về 1 danh sách các học viên trong lớp
                    return [-2] # nếu chạy hết vòng for mà chưa tìm thấy class trong sheet major của nó thì nghĩa là có trong type_of_class nhưng chưa thêm vào sheet type của nó
            return [-4] # nếu chạy hết vòng for mà không return nghĩa là không tồn tại trong sheet type_of_class
        except FileNotFoundError as e:
            print(f"{colorama.Fore.RED}Lỗi load file danh sách lớp!{colorama.Fore.RESET}")
            traceback.print_exception(e)
            traceback.print_exc()
            return [-1]
        except Exception as e:
            print(f"Error:\n{e}")
            traceback.print_exc()
            return [-3]
 
def absent_user_string(list_remainer_user:list)->str:
    '''Trả về 1 chuỗi các học viên còn vắng'''
    output = "Chưa có mặt: \n"
    for i in list_remainer_user:
        output += f"- {i}\n"
    return output

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

    # check available auto-role
    await client.init_view_get_role(auto_role.startup_get_role_view(timeout=None))

    if str(startup_role_view_messsage_id) == '0' and startup_role_view_messsage_id != None: # check if autorole message is already available
        channel_get_role = client.get_channel(int(CHANNEL_ID))

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
        for g in client.guilds:
            if g.id == MY_GUILD.id:
                client.init_javis(g)
    except custom_error.NotFoundAdminLogChannelException as e1:
        debug_log.error(f"Chưa có channel cho admin_log")
        # await client._connection.close()
        await client.close()

@client.tree.command()
async def diem_danh(interaction: discord.Interaction):
    """Điểm danh lớp"""
    global stop_check_class
    stop_check_class = False
    list_user_id:list = get_class_user_displayname_from_danh_sach(interaction.channel.name)
    if list_user_id == [-1]: # handle lỗi chưa có file danh sách
        await interaction.response.send_message("Không tìm thấy file danhsachlop.xlsx", ephemeral=True)
    elif list_user_id == [-2]: # handle lỗi không tìm thấy trong sheet của major
        await interaction.response.send_message("Không tìm thấy lớp trong tab chuyên ngành của nó", ephemeral=True)
    elif list_user_id == [-3]: # handle các lỗi khác
        await interaction.response.send_message("Tồn tại lỗi khác, xem terminal để kiểm tra lỗi", ephemeral=True)
    elif list_user_id == [-4]: # handle các lỗi không tìm thấy trong type_of_class
        await interaction.response.send_message("Không tìm thấy lớp trong danh tab type_of_class", ephemeral=True)
    else: # không lỗi khác
        # print(ctx.channel.id)
        # print(ctx.guild.id)
        list_user_comat:list = []
        loop_count = 0
        while len(list_user_id) != 0 and stop_check_class is False:
            output_message = "Có mặt: \n"
            output_message += "".join(f"- {user}\n" for user in list_user_comat)
            current_members_of_channel = interaction.channel.members
            for person in current_members_of_channel:
                # print (f"{colorama.Fore.CYAN} [+] Kiểm tra bạn học: {person.display_name} {colorama.Fore.RESET}")
                if not person.bot:
                    if person.display_name in list_user_id:
                        output_message += f"- {person.display_name}\n"
                        list_user_id.remove(person.display_name)
                        list_user_comat.append(person.display_name)
                    else:
                        print(person.display_name)
            output_message += absent_user_string(list_user_id) 
            if DEBUG:
                if loop_count > 0:
                    output_message = f"CHECK lần {loop_count}:\n--------------\n" + output_message
                    await interaction.edit_original_response(content=output_message)
                else:
                    await interaction.response.send_message(content=output_message, ephemeral=True, silent=True)
                loop_count += 1
                await asyncio.sleep(delay_time_at_diemdanh) # stop at 5 minuts = 300
            else:
                if loop_count > 0:
                    output_message = f"CHECK lần {loop_count}\n--------------\n" + output_message
                    await interaction.edit_original_response(content=output_message)
                else:
                    await interaction.response.send_message(content=output_message, ephemeral=True, silent=True)
                loop_count += 1
                await asyncio.sleep(delay_time_at_diemdanh) # stop at 5 minuts = 300
                
@client.tree.command()
async def dung_diem_danh(interaction: discord.Interaction):
    '''Dừng điểm danh'''
    global stop_check_class
    stop_check_class = True
    await interaction.response.send_message("Anh Tân machine đã dừng điểm danh!", ephemeral=True)

@client.tree.command(description="Lệnh gán role cho mọi user trong Kênh gọi command")
@discord.app_commands.describe(
    role_name='Tên của role muốn gán'
)
async def role_set_all(interaction: discord.Interaction, role_name: str):
    """
    Gắn role cho các user trong channel

    Args:
        intents (discord.Intents): The intents to be used by the client.

    Returns:
        None
    """
    role = discord.utils.get(interaction.guild.roles, name=role_name)
    members = interaction.channel.members 
    print(members)
    if role:
        await interaction.response.send_message(f"Role '{role_name}' found with ID: {role.id}", ephemeral=True)
        for mem in members:
            if role not in mem.roles: 
                await mem.add_roles(role)
                await interaction.followup.send(f"Add '{role_name}' to: {mem.display_name}",ephemeral=True)
    else:
        await interaction.response.send_message(f"Role '{role_name}' not found", ephemeral=True)

@client.tree.command(description="Lệnh gắn role cho user")
@discord.app_commands.describe(
    user_name_list='Những người muốn gán role, có thể nhiều user cùng lúc, bằng cách đặt các tên hiển thị cách nhau bởi dấu, ví dụ: Tân,tuấn,tod',
    role_name='Tên của role muốn gán'
)
async def role_set_for(interaction: discord.Interaction, user_name_list: str, role_name: str):
    """
    Assigns a specified role to one or more users in the Discord server.

    This function takes a list of usernames and a role name, then attempts to assign
    the specified role to each user. It provides feedback for each successful assignment
    and notifies if a user already has the role or if the role doesn't exist.

    Parameters:
    interaction (discord.Interaction): The interaction object representing the command invocation.
    user_name_list (str): A comma-separated string of display names of users to assign the role to.
    role_name (str): The name of the role to be assigned.

    Returns:
    None: This function doesn't return any value. It sends messages through Discord's API
    to provide feedback on the role assignment process.
    """
    role = discord.utils.get(interaction.guild.roles, name=role_name)
    if role:
        await interaction.response.send_message(f"Role '{role_name}' found with ID: {role.id}", ephemeral=True)
        user_list = [user.strip().strip("\n") for user in user_name_list.split(",")]
        for user_name in user_list:
            member = discord.utils.get(interaction.guild.members, name=user_name)
            if role not in member.roles: 
                await member.add_roles(role)
                await interaction.followup.send(f"Add '{role_name}' to: {user_name}", ephemeral=True)
            else:
                await interaction.followup.send(f"'{user_name}' đã tồn tại role này rồi", ephemeral=True)
    else:
        await interaction.response.send_message(f"Role '{role_name}' not found", ephemeral=True)

@client.tree.command(description="Liệt kê ra các user hiện tại đang trong kênh")
async def get_user(interaction: discord.Interaction):
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

    members = interaction.channel.members
    output = ""
    for i in members: 
        output += i.display_name + "\n"
    await interaction.response.send_message(f"{output}", ephemeral=True)

@client.tree.command(description="Anh Tân xin chào")
async def hello(interaction:discord.Interaction):
    # đoạn trước này
    # 1 giây thực đoạn ví dụ: lấy thông tin .... 
    await interaction.response.send_message("Anh Tân đẹp trai đã gửi tin nhắn hello đến bạn!", ephemeral=True)


client.run(TOKEN)