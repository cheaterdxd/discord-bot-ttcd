
import discord, traceback
from utils import debug_log
def check_exists_channel_by_id(guild: discord.Guild, channel_name_id: int) -> discord.TextChannel|None:
    """
    Check if a channel with the given name exists in the specified Discord guild.

    Parameters:
    guild (discord.Guild): The Discord guild where the channel should be searched.
    channel_id (int): The ID of the channel to search for.

    Returns:
    discord.TextChannel: The channel object if found, otherwise None.
    """
    return discord.utils.get(guild.channels, id=channel_name_id)


def check_exists_channel_by_name(guild: discord.Guild, channel_name: str) -> discord.TextChannel|None:
    """
    Check if a channel with the given name exists in the specified Discord guild.

    Parameters:
    guild (discord.Guild): The Discord guild where the channel should be searched.
    channel_id (int): The ID of the channel to search for.

    Returns:
    discord.TextChannel: The channel object if found, otherwise None.
    """
    return discord.utils.get(guild.channels, name=channel_name)


async def create_channel(guild:discord.Guild, channel_name:str) -> discord.TextChannel:
    """
    Create a new text channel with the given name in the specified Discord guild.

    Parameters:
    guild (discord.Guild): The Discord guild where the channel should be created.
    channel_name (str): The name of the channel to create.

    Returns:
    discord.TextChannel: The newly created channel object.
    """
    try:
        channel = await guild.create_text_channel(channel_name)
        return channel
    except:
        debug_log.error(f"Failed to create channel '{channel_name}' in {guild.name}.")
        return None
    
async def send_to_channel(guild: discord.Guild, channel_id:int, message:str):
    """
    Send a message to a channel with the given name.
    
    Parameters:
    channel_id (int): The name of the channel to send the message to.
    message (str): The message to be sent.
    """
    debug_log.info(f"received channel_id: {channel_id}" )
    if(channel_id == 0):
        debug_log.error("No channel ID specified")
        traceback.print_exc()
    if(guild is None):
        debug_log.error("No valid Guild")
        traceback.print_exc()
    if(message == ""):
        debug_log.error("Zero length message")
        traceback.print_exc()
    channel = check_exists_channel_by_id(guild, channel_id)
    if channel:
        await channel.send(message)
        debug_log.success(f"Gửi tin nhắn tới channel '{channel.name}'")
    else:
        debug_log.error(f"Channel '{channel_id}' not found in your guild.")

async def tag_member_in_message(guild: discord.Guild, channel_id:int, member_id, message:str):
    """
    Tag a Discord member with their ID in a message.
    
    Parameters:
        channel_id (int): The ID of the channel to send the message to.
        member_id (str): The Discord ID of the member to be tagged.
        message (str): The message to be sent, including the tag.

    Returns:
        None: This function doesn't return any value. It sends messages through Discord's API
    """
    member = guild.get_member(member_id)
    if str(channel_id) == "0":
        debug_log.error("No channel ID specified")
        raise ValueError("Channel ID not valid")
    else:
        if member:
            await send_to_channel(guild, channel_id, f"{message} {member.mention}")
            debug_log.success(f"Đã gửi tin nhắn và tag '{member.display_name}' trong channel '{channel_id}'")
        else:
            debug_log.error(f"Không tìm thấy thành viên nào có ID '{member_id}'")

async def tag_multi_member_in_message(guild: discord.Guild, channel_id:int, member_id_list, message:str):
    """
    Tag a Discord member with their ID in a message.
    
    Parameters:
        channel_id (int): The ID of the channel to send the message to.
        member_id (str): The Discord ID of the member to be tagged.
        message (str): The message to be sent, including the tag.

    Returns:
        None: This function doesn't return any value. It sends messages through Discord's API
    """

    if str(channel_id) == "0":
        debug_log.error("No channel ID specified")
        raise ValueError("Channel ID not valid")
    else:
        tag_string = ""
        for admin_id in member_id_list:
            member = guild.get_member(int(admin_id))
            if member:
                tag_string += f"<@{admin_id}> "
            else:
                debug_log.error(f"Không tìm thấy thành viên nào có ID '{admin_id}'")
        
        await send_to_channel(guild, channel_id, f"{message}\n{tag_string}")
        debug_log.success(f"Đã gửi tin nhắn và tag '{tag_string}' trong channel '{channel_id}'")


