# # This variable will store the ID of the specific message you want to track
# SPECIFIC_MESSAGE_ID = "1296860511664734302"  # Replace with your actual message ID

# @client.event
# async def on_raw_reaction_add(payload):
#     channel = await client.fetch_channel(payload.channel_id)

#     user = await client.fetch_user(payload.user_id)

#     await channel.send("Bấm nút sau để lấy quyền truy cập lớp học của bạn", view=input.startup_get_role_view())

    # emoji = payload.emoji
    # message = await client.fetch_message(payload.message_id)

    # modal = MyModal(title="User Input Form")
    # view1 = ModalView()
    # view1.set_view(title="Nhập thông tin mail/ sdt:")
    # await channel.send(view=view1)
    # print(type(payload))

    
    # await payload..send_modal(modal)
    # Ignore if the bot is reacting to its own message
    # if user.bot:
    #     return

    # # Check if the reaction is on the specific message
    # if reaction.message.id == SPECIFIC_MESSAGE_ID:
    #     print(f"{user.name} reacted with {reaction.emoji} on the tracked message!")
    #     await reaction.message.channel.send(f"{user.mention} reacted with {reaction.emoji} on the specific message.")



'''
def load_file_user(class_name: str) -> list:
    # Load data for class name
    global danh_sach_hoc_vien_path
    try:
        with open(danh_sach_hoc_vien_path, "r", encoding="UTF8") as read_class_user:
            data = yaml.safe_load_all(read_class_user)
            for i in data: 
                print(i[class_name])
                if(i[class_name]):
                    print("found")
                    class_users = i[class_name]
                    return [user_name.strip().strip("\n") for user_name in class_users]
                else:
                    return [-2]
    except FileNotFoundError as e:
        print(f"{colorama.Fore.RED}Lỗi load file danh sách lớp!{colorama.Fore.RESET}")
        return [-1]
    except KeyError as e:
        print(f"{colorama.Fore.RED}Danh sách chưa có lớp này!{colorama.Fore.RESET}")
        return [-2]
    except Exception as e:
        print(f"Error:\n{e}")
        traceback.print_exc()
        return [-3]


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}', ephemeral=True)


@client.tree.command()
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')


# The rename decorator allows us to change the display of the parameter on Discord.
# In this example, even though we use `text_to_send` in the code, the client will use `text` instead.
# Note that other decorators will still refer to it as `text_to_send` in the code.
@client.tree.command()
@app_commands.rename(text_to_send='text')
@app_commands.describe(text_to_send='Text to send in the current channel')
async def send(interaction: discord.Interaction, text_to_send: str):
    """Sends the text into the current channel."""
    await interaction.response.send_message(text_to_send)


# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.
@client.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    """Says when a member joined."""
    # If no member is explicitly provided then we use the command user here
    member = member or interaction.user

    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


# A Context Menu command is an app command that can be run on a member or on a message by
# accessing a menu within the client, usually via right clicking.
# It always takes an interaction as its first parameter and a Member or Message as its second parameter.

# This context menu command only works on members
@client.tree.context_menu(name='Show Join Date')
async def show_join_date(interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')


# This context menu command only works on messages
@client.tree.context_menu(name='Report to Moderators')
async def report_message(interaction: discord.Interaction, message: discord.Message):
    # We're sending this response message with ephemeral=True, so only the command executor can see it
    await interaction.response.send_message(
        f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
    )

    # Handle report by sending it into a log channel
    log_channel = interaction.guild.get_channel(0)  # replace with your channel id

    embed = discord.Embed(title='Reported Message')
    if message.content:
        embed.description = message.content

    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at

    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

    await log_channel.send(embed=embed, view=url_view)
'''


# @client.tree.command(description="Chức năng gắn role tự động dành cho học viên")
# async def truy_cap_role(interaction:discord.Interaction):
#     # interaction.
#     # if gmail == "" and phone_number == "":
#     #     await interaction.response.send_message("Vui lòng nhập email và số điện thoại", ephemeral=True)
#     #     return
#     def check(m: discord.Message):  # m = discord.Message.
#         return m.author.id == interaction.user.id and m.channel.id == interaction.channel.id
#     await interaction.response.send_message("Hãy nhập vào địa chỉ mail hoặc số điện thoại bạn đã cung cấp (trong 60 giây):", ephemeral=True)
#     try:
#         #              event = on_message without on_
#         msg = await client.wait_for('message', check = check, timeout = 60.0)
#         await interaction.followup.send(f"**{interaction.user.name}**, đã xác nhận mail là {msg.content}!", ephemeral=True)
#         # ...
#         info_user = strings_helper.clean_email(msg.content)
#         role_assigned = await auto_role.process(interaction.guild, interaction.user.id, info_user)
#         if role_assigned == -1:
#             await interaction.followup.send("Thông tin bạn vừa nhập không được ghi nhận với Trung tâm ! Vui lòng báo cáo với quản trị viên để nhận hỗ trợ.",ephemeral=True)
#         if role_assigned == -2:
#             # todo: check
#             pass
#         if role_assigned == -3:
#             # todo: check
#             pass
#         # msg = discord.Message
#     except asyncio.TimeoutError: 
#         # at this point, the check didn't become True, let's handle it.
#         await interaction.followup.send(f"**{interaction.user.name}**, không nhận được tin nhắn", ephemeral=True)
#         return
#     finally:
#         await msg.delete()



