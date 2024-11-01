#import module get_question cua anh Hoan
import get_question
import get_input_user

async def gui_cau_hoi_cho_user(danh_sach_cau_hoi: list, user):
    """
    Hàm gửi câu hỏi cho user

    Parameter:
    - danh_sach_cau_hoi (list): danh sách bộ câu hỏi lấy từ module get_question
    - user (int): Mã người dùng (User id)

    Return:
    - True: Người dùng đã trả lời hết các câu hỏi
    - False: Người dùng chưa trả lời hết, hoặc sai cú pháp
    """
    danh_sach_tra_loi = dict()
    # Khởi tạo danh sách để lưu câu trả lời
    for so_thu_tu, noi_dung_cau_hoi in enumerate(danh_sach_cau_hoi):
        # Gửi câu hỏi và chờ trả lời
        cau_tra_loi = await gui_va_doi_cau_tra_loi(user, so_thu_tu, noi_dung_cau_hoi)
        #Hàm chuẩn hóa đầu vào
        ket_qua = kiem_tra_cau_tra_loi(get_input_user.standardize_input(cau_tra_loi))
        if ket_qua == "Cú pháp không hợp lệ":
            print("Cú pháp không hợp lệ. Thoát")
            return False
        else:
            print("Cú pháp hợp lệ")
            danh_sach_tra_loi[so_thu_tu] = cau_tra_loi
    return True

async def gui_va_doi_cau_tra_loi(user, so_thu_tu, noi_dung_cau_hoi):
    pass

async def kiem_tra_cau_tra_loi(cau_tra_loi):
    """
    Hàm nhận câu trả lời từ người dùng với điều kiện câu trả lời phải là A, B, C hoặc D
    """
    tach_dap_an = cau_tra_loi.split()
    for tung_dap_an in tach_dap_an:
        if tung_dap_an not in ['A','B','C','D','E']:
            ket_qua = "Cú pháp không hợp lệ"
            return ket_qua
    ket_qua = "Cú pháp hợp lệ"
    return ket_qua

# Test thử:
if __name__ == '__main__': # được chạy trực tiếp
    # User id
    user = "889513636958179328"
    user_input = "1"
    level = get_input_user.standardize_input(user_input)
    danh_sach_cau_hoi = get_question.lay_danh_sach_cau_hoi(level)
    gui_cau_hoi_cho_user(danh_sach_cau_hoi,user)