import discord

def get_member_info(guild: discord.Guild, member_id: int) -> str:
    member = discord.utils.get(guild.members, id=member_id)

    if member:
        # Member found, return their information as a string
        return f"- Member ID: {member.id}\n- Member Name: {member.name}\n- Member Display Name: {member.display_name}\n- Member Status: {member.status}\n- Member Joined At: {member.joined_at}\n- Member Is Bot: {member.bot}"
    else:
        # Member not found
        return f"Member with ID {member_id} not found in the guild."

def get_member(guild, member_id):
    return discord.utils.get(guild.members, id=member_id)