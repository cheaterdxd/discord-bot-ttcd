import yaml, os, dotenv
from utils import channel_helper, debug_log, custom_error
from discord import Guild, TextChannel
# from utils import custom_error
dotenv.load_dotenv()
DEBUG = os.getenv('DEBUG') 
ADMIN_LOG_CHANNEL_ID = os.getenv('ADMIN_LOG_CHANNEL_ID') 
# DEBUG = os.getenv('DEBUG') 

import os

# Get the current directory of input.py
current_dir = os.path.dirname(__file__)

# Construct the path to data.yml
file_admin_path = os.path.join(current_dir, 'admin_list_id.yaml')


class alartor_JAVIS:

    guild:Guild = None
    alert_channel_id:int = None
    alert_channel:TextChannel = None
    admin_id_list:list = None
    def __init__(self, guild)->int:
        self.guild:Guild = guild
        self.alert_channel_id = ADMIN_LOG_CHANNEL_ID
        self.alert_channel = None
        self.admin_id_list = []
        self.init_admin_data()
        self.init_log_channel("admin_log")
    
    def init_log_channel(self, channel_name):
        '''
        Init admin channel if not exist
        
        1. Check if channel exists
        2. If channel does not exist, create a new channel with the given name
        '''
        if str(self.alert_channel_id) == "0":
            self.alert_channel = channel_helper.check_exists_channel_by_name(self.guild, channel_name)
            if self.alert_channel is None:
                # self.alert_channel = channel_helper.create_channel(self.guild, channel_name)
                # debug_log.success(f"Tạo channel mới: '{channel_name}' with ID: {self.alert_channel.id}")
                # debug_log.error(f"Chưa có channel cho admin_log")
                # exit(-1)
                raise custom_error.NotFoundAdminLogChannelException("Chưa có channel cho admin_log")
            self.alert_channel_id = self.alert_channel.id # update channel_alert_id
            debug_log.success(f"Đã cập nhật channel ID : {self.alert_channel.id}")
        else: # not zero
            pass # channel has been created previous time
    def init_admin_data(self):
        '''
        Init admin id from yaml file
        
        1. If DEBUG is 'ttcd', load RELEASE data
        2. If DEBUG is not 'ttcd', load DEBUG data
        '''
        if DEBUG is None:
            print("DEBUG environment variable is not set.")
            raise ValueError("DEBUG environment variable is not set")
        with open(file_admin_path, "r") as admin_list_f:
            data = yaml.safe_load(admin_list_f)
            if isinstance(data, dict) and DEBUG == 'ttcd':
                self.admin_id_list = data["RELEASE"]
            else:
                self.admin_id_list = data['DEBUG']
            debug_log.success(f"Đã tải vào bot các admin IDs: {self.admin_id_list} thành công")
        
    
    async def send_alert_to_admins(self, message: str):
        '''
        Send alert message to all admins
        '''
        if str(self.alert_channel_id) == "0":
            debug_log.error("Không tìm thấy ID kênh thông báo!")
            return
        if self.alert_channel is None:
            debug_log.error("Không tìm thấy đối tượng kênh thông báo!")
            return
        await channel_helper.tag_multi_member_in_message(self.guild, self.alert_channel_id, self.admin_id_list, message)
        debug_log.success(f"Đã gửi tin nhắn thông báo cho tất cả admin")
        debug_log.info(f"{message}")

if __name__ == "__main__":
    bot_alert_t = alartor_JAVIS()
    print(bot_alert_t)
    