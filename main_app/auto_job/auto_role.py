import traceback, os
from google_api.authenticator import authen_me
from google_api.work_with_sheets_data import check_user_exist
from discord import utils, Interaction, Color, ui, Interaction, ButtonStyle
from main_app.utils import member_helper
from utils import debug_log, strings_helper, custom_error
from gui_view.input import colored_message_embed




class get_info_modal(ui.Modal, title='XÁC THỰC HỌC VIÊN'):
    input_field = ui.TextInput(label="Nhập SĐT/mail đã đăng ký", placeholder="Số điện thoại hoặc mail", custom_id="ROOT#input_info_textinput")
    async def on_submit(self, interaction):
        debug_log.info(type(interaction))
        # await interaction.response.send_message(f"You entered: {self.input_field.value}")
        await prepare_data_for_process(interaction, self.input_field.value)

class startup_get_role_view(ui.View):
    @ui.button(label="Xác thực tôi", style=ButtonStyle.green, emoji="✅", custom_id="ROOT#get_role_button")
    async def button_callback(self, interaction:Interaction, button:ui.Button):
        button.disabled = True
        await interaction.response.send_modal(get_info_modal())


def data_check_in_specific_case(data):
    """
    Hàm kiểm tra dữ liệu đầu vào

    Parameters:
    - data: dữ liệu đầu vào

    Returns:
    - data: nếu dữ liệu đầu vào hợp lệ
    - False nếu dữ liệu đầu vào không hợp lệ
    """
    valid_format_data = []
    if strings_helper.is_mail_address(data) is False and strings_helper.is_phone_number(data) is False:
        split_words = ""
        if "/" in data:
            split_words = "/"
        if  "," in data:
            split_words = ","
        if  ";" in data:
            split_words = ";"
        if  "_" in data:
            split_words = "_"
        if  " " in data:
            split_words = " "
        if split_words != "":
            data = data.split(split_words)
            for i in data:
                if strings_helper.is_mail_address(i) or strings_helper.is_phone_number(i):
                    valid_format_data.append(str(i))
            if len(valid_format_data) > 0:
                return valid_format_data
    return False


async def processing_role(guild, member_id:str, info_user_clean, interaction:Interaction)->list|str:
    """
    Hàm xử lý khi người dùng truyền thông tin role và member_id vào

    Parameters:
        guild: đối tượng discord.Guild
        member_id: id của member muốn gán role
        info: thông tin của user, bao gồm role và index của user trong sheet

    """

    #  = strings_helper.clean_email(user_info)

    sheet_resource = await authen_me()
    ret = check_user_exist(sheet_resource, user_info=info_user_clean)
    if ret == False: # trường hợp này không tìm thấy info của user vừa nhập
        # return -1 # không tìm thấy info, trả signal cho app
        raise custom_error.NotValidUserInfoException("Thông tin người dùng vừa nhập không tìm thấy trong danh sách gán role")
    member_object = utils.get(guild.members, id=member_id)
    
    user_role_column_raw_data = ret.get('role')
    # check if multi role
    if "," in user_role_column_raw_data:
        user_role_list = user_role_column_raw_data.split(",")
        for role in user_role_list:
            role = str(role).strip()
            # debug_log.info(role)
            role_object = utils.get(guild.roles, name=role)
            if role_object is not None and member_object is not None:
                await member_object.add_roles(role_object)
            else:
                # debug_log.error("Error code: [-2] - Không tìm thấy role cần gán cho thành viên")
                raise custom_error.RoleNotFoundException("Không tìm thấy role để gán", user_role_column_raw_data)
        return user_role_column_raw_data
    else: # in case just one role
        role_object = utils.get(guild.roles, name=user_role_column_raw_data)
        if role_object is not None and member_object is not None:
            await member_object.add_roles(role_object)
            return user_role_column_raw_data
        else:
            # debug_log.error("Error code: [-2] - Không tìm thấy role cần gán cho thành viên")
            raise custom_error.RoleNotFoundException("Không tìm thấy role để gán", user_role_column_raw_data)
        
async def prepare_data_for_process(interaction:Interaction, user_info:str):
    guild = interaction.guild
    debug_log.info(type(interaction))
    member_id = interaction.user.id
    message_alert = ""
    member_info_collect = member_helper.get_member_info(guild, int(member_id))# Một số thông tin khác cần để tag admin
    try:
        info_user_clean = strings_helper.clean_email(user_info)
        member_name = member_helper.get_member(guild, int(member_id)).name
        
        if strings_helper.is_mail_address(info_user_clean) is False and strings_helper.is_phone_number(info_user_clean) is False:
            if data_check_in_specific_case(info_user_clean) is False:
                await interaction.response.send_message(embed=colored_message_embed("Thông tin bạn nhập vào không phải mail/sđt!",Color.brand_red()),ephemeral=True)
                message_alert = f"[THÔNG BÁO LỖI] User nhập sai ĐỊNH DẠNG thông tin: \n- Dữ liệu user:{member_name}\n- User nhập vào: {info_user_clean}"
            else: # tách case, bắt nhập lại
                await interaction.response.send_message(embed=colored_message_embed("Vui lòng chỉ nhập mail hoặc sdt, không nhập cả hai!",Color.brand_red()),ephemeral=True)
                message_alert = f"[THÔNG BÁO LỖI] User nhập sai ĐỊNH DẠNG thông tin: \n- Dữ liệu user:{member_name}\n- User nhập vào: {info_user_clean}"
        else: 
            # xác thực dữ liệu xong thì bắt đầu gắn role
            role_list_success = await processing_role(guild, member_id, info_user_clean, interaction)
            # trả về thành công nếu ko có error nào được raise
            await interaction.response.send_message(embed=colored_message_embed("Đã gán cấp quyền truy cập lớp học thành công",Color.green()),ephemeral=True)
            message_alert = f"[THÔNG BÁO] Thành viên mới đã xác thực thành công: \n- Thành viên:{member_name}\n- Role: {role_list_success}"
    except custom_error.NotValidUserInfoException as e1: # -1, error báo khi không tìm thấy user nào trong sheet (đúng format, sai value)
        await interaction.response.send_message(embed=colored_message_embed("Thông tin bạn vừa nhập không được ghi nhận với Trung tâm ! Vui lòng báo cáo với quản trị viên để nhận hỗ trợ.",Color.brand_red()),ephemeral=True)
        debug_log.error(f"Error code: [-1] - {e1}")
        # traceback.print_exc()
        # member_info_collect = member_helper.get_member_info(guild, int(member_id))
        message_alert = f"[THÔNG BÁO LỖI] User nhập sai dữ liệu xác thực: \n- Dữ liệu user:{member_info_collect}\n- User nhập vào: {info_user_clean}" # tin nhắn gửi admin

    except custom_error.RoleNotFoundException as e2: # -2, error báo không tìm thấy role cho user
        await interaction.response.send_message(embed=colored_message_embed("Có lỗi xảy ra khi tìm role cho bạn, vui lòng đợi quản trị viên sửa lỗi.",Color.brand_red()),ephemeral=True)
        debug_log.error(f"Error code: [-2] - {e2}")
        # traceback.print_exc()
        # member_info_collect = member_helper.get_member_info(guild, int(member_id))
        message_alert = f"[THÔNG BÁO LỖI] Không tìm thấy role cho user:\n{member_info_collect}\nRole thiếu: {e2.missing_role}"
    
    
    except Exception as e: # -3, bất kỳ error nào khác cho hệ thống
        await interaction.response.send_message(embed=colored_message_embed("Không thể gán role cho bạn, vui lòng đợi quản trị viên sửa lỗi.",Color.brand_red()),ephemeral=True)
        message_alert = f" [THÔNG BÁO LỖI] Lỗi hệ thống {e}"
        debug_log.error(f"Error code [-3]: {e}")
        traceback.print_exc() # cần traceback vì không xác định được lỗi
    finally: # luôn gửi tin nhắn cho admin cuối cùng
        try:
            client = interaction.client
            debug_log.info(client)
            if client is None:
                debug_log.error("Client is None")
            else:
                await client.javis.send_alert_to_admins(message_alert)
        except Exception as e:
            traceback.print_exc()
            debug_log.error(f"Error sending alert: {e}")
    


