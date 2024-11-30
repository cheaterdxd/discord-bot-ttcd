import discord
from discord.ext import commands
import debug_log

async def delete_message_by_id(channel:discord.TextChannel, message_id:int):
    try:
        message = await channel.fetch_message(message_id)
        await message.delete()
        debug_log.success(f"Deleted message with ID: {message_id}")
    except discord.NotFound:
        debug_log.error(f"Message with ID {message_id} not found.")
    except discord.Forbidden:
        debug_log.error(f"Bot does not have permission to delete message with ID {message_id}.")
    except discord.HTTPException as e:
        debug_log.error(f"Failed to delete message with ID {message_id}: {e}")
