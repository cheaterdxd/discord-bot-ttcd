import discord
def colored_message_embed(content, color_choose):
    embed = discord.Embed(title="Thông báo", description=content, color=color_choose)
    return embed
