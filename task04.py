def lay_cau_hoi_theo_level(level):
    # Trả về danh sách câu hỏi tương ứng với level đã chọn
    if level == 1:
        return cau_hoi_level_de
    elif level == 2:
        return cau_hoi_level_tb
    elif level == 3:
        return cau_hoi_level_kho
async def gui_cau_hoi_cho_user(danh_sach_cau_hoi: list, user):
    danh_sach_tra_loi = []
    # Khởi tạo danh sách để lưu câu trả lời
    for index, cau_hoi in enumerate(danh_sach_cau_hoi):
    # Gửi câu hỏi và chờ trả lời
    cau_tra_loi = await gui_va_doi_cau_tra_loi(cau_hoi, user, index + 1)
# Hàm nhận câu trả lời từ người dùng với điều kiện câu trả lời phải là A, B, C hoặc D
async def nhan_cau_tra_loi(user):
    while True:  # Vòng lặp liên tục cho đến khi nhận được câu trả lời hợp lệ
        def check_tra_loi(message):
            return message.author == user and message.content.upper() in ['A', 'B', 'C', 'D']
        
        # Bot sẽ đợi cho đến khi người dùng gửi câu trả lời hợp lệ (A, B, C, hoặc D)
        tra_loi = await bot.wait_for('message', check=check_tra_loi)
        return tra_loi.content.upper()  # Trả về câu trả lời hợp lệ (chuyển thành chữ hoa)
danh_sach_tra_loi.append(cau_tra_loi)
# Lưu câu trả lời vào danh sách
