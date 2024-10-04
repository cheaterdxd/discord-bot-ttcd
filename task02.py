"""Làm quen và hiểu cách sử dụng function để BOT gửi tin nhắn cho user
#Quy trình như sau:
# [1] Tại kênh chat bất kỳ, user gõ lệnh /kiem_tra
# [2] BOT sẽ nhắn tin trực tiếp cho user để user tương tác làm kiểm tra"""

import discord
async def on_message(message):
    if message.content.startswith('/kiem_tra'):
        await message.author.send('Xin chào!')


"""GIẢI THÍCH
+ message.content.startswith('kiem_tra'): BOT Kiểm tra xem tin nhắn có bắt đầu bằng chuỗi 'kiem_tra' hay không.
+ await message.author.send('Xin chào!'): message.author - BOT lấy thông tin về người đã gửi tin nhắn và send() gửi tin nhắn trực tiếp đến họ

"""
