# Giới thiệu
## Vấn đề
Chức năng cho phép admin quản trị discord có thể không lo lắng vấn đề gắn role cho học viên.

## Giải quyết
Cho phép việc gắn role không cần sự can thiệp của quản trị viên, học viên chỉ cần thực hiện cung cấp email đã xác nhận khi đăng ký khóa học.

# Các bước thực hiện

1. User nhập thông tin xác thực
2. Lấy thông tin xác thực truy xuất trên dữ liệu google sheet của ban quản trị
3. Nếu đúng thì trả về những Role của lớp mà học viên đăng ký
4. Nếu Role cũ (học viên đã đăng ký trước đó & đã được cấp role) thì không hiển thị. 
5. Học viên sẽ chọn role từ danh sách trả về, nếu phù hợp thì cấp role

## Các kịch bản test auto role
- [x] nhập đúng user bằng mail/sdt và có role thỏa mãn
- [x] nhập đúng user bằng mail/sdt và không có role thỏa mãn (role chưa được tạo)
- [x] nhập đúng user bằng mail/sdt và thiếu role (tức là có nhiều role, thiếu 1 vài role chưa được thỏa mãn)
- [x] nhập sai user bằng mail/sdt
- [x] user xác thực bằng một trong nhiều mail/sdt
- [x] user nhập vào không phải mail/sdt
- [x] user nhập vào cả mail và sdt
## Các kịch bản test khả năng có sẵn của chức năng auto-role 
- [x] Khi không có channel admin_log --> thoát
- [ ] Khi không có quyền

# TODO

- [ ] phân biệt giữa role thêm được và role thiếu trong case3
- [ ] mỗi lần gán xong thì chuyển trạng thái thành Yes
- [ ] Kiểm tra số lần gọi kiểm duyệt role trong 1 ngày

## Issue

### 1. cannot set reaction in reponse interaction
```python
await interaction.response.send_message() always returns None

You can get around this by using await interaction.channel.send() which returns discord.Message and therefore you are able to add_reaction()

    message = await interaction.channel.send(f"**{question}**", embed=emb)

    await message.add_reaction('👍')
Late, but there is a better way of doing this. Using interaction.original_response we can get the interactionMessage object and add reaction from there.

await interaction.response.send_message(f"**{question}**", embed=emb)
msg = await interaction.original_response()
await msg.add_reaction('👍')
```

# Một số trigger ẩn
- Khi bot gửi tin nhắn có "view xác thực" sẽ lưu vào ".env" message_id của tin nhắn. Bot sẽ tự động kiểm tra và [xóa/đơn giản là không tạo tin mới] tin nhắn xác thực đã từ trước vào gửi vào channel. 
