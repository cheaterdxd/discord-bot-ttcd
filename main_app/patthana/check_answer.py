def Check_Input(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an):
    """
    Kiểm tra tính hợp lệ của dữ liệu đầu vào:
    - Kiểm tra số lượng câu hỏi, câu trả lời, đáp án có khớp nhau không.
    - Kiểm tra ID của từng câu hỏi, câu trả lời, đáp án có tương ứng không.
    """
    # Kiểm tra số lượng phần tử
    if len(danh_sach_cau_hoi) != len(danh_sach_cau_tra_loi) or len(danh_sach_cau_hoi) != len(danh_sach_dap_an):
        return False, "Số lượng câu hỏi, câu trả lời, và đáp án không khớp!"

    # Kiểm tra từng phần tử có ID tương ứng hay không
    for i in range(len(danh_sach_cau_hoi)):
        id_cauhoi, _ = danh_sach_cau_hoi[i]
        id_traloi, _ = danh_sach_cau_tra_loi[i]
        id_dapan, _ = danh_sach_dap_an[i]

        if id_cauhoi != id_traloi or id_cauhoi != id_dapan:
            return False, f"Lỗi: ID tại câu hỏi {id_cauhoi} không khớp giữa câu hỏi, câu trả lời và đáp án."

    # Nếu mọi thứ hợp lệ
    return True, None


def Compare_Answer(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an):
    """
    Hàm so sánh câu trả lời của người dùng và đáp án đúng.
    """
    # Kiểm tra đầu vào
    hop_le, thong_bao_loi = Check_Input(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an)
    if not hop_le:
        return [thong_bao_loi]
    
    ket_qua = []
    
    # Duyệt qua từng câu hỏi và so sánh câu trả lời với đáp án
    for i in range(len(danh_sach_cau_hoi)):
        cau_hoi_hien_tai = danh_sach_cau_hoi[i][1]  # Chỉ lấy câu hỏi (bỏ ID)
        dap_an_nguoi_dung = set(danh_sach_cau_tra_loi[i][1].replace(" ", "").split(','))  # Chuyển câu trả lời của người dùng thành set
        dap_an_dung = set(danh_sach_dap_an[i][1].replace(" ", "").split(','))  # Chuyển đáp án đúng thành set

        # Kiểm tra nếu người dùng bỏ trống câu trả lời
        if not dap_an_nguoi_dung:  # Nếu tập hợp trống
            ket_qua.append(f"{cau_hoi_hien_tai}: Bạn đã không trả lời.")
        elif dap_an_nguoi_dung.issubset(dap_an_dung):  # Nếu câu trả lời của người dùng là tập hợp con của đáp án đúng
            ket_qua.append(f"{cau_hoi_hien_tai}: Bạn đã chọn đúng.")
        else:
            ket_qua.append(f"{cau_hoi_hien_tai}: Bạn đã trả lời sai, bạn chọn {', '.join(dap_an_nguoi_dung)}, đáp án đúng là {', '.join(dap_an_dung)}.")
    
    return ket_qua


# Ví dụ danh sách câu hỏi, câu trả lời, đáp án với ID
danh_sach_cau_hoi = [
    (1, "Câu hỏi 1: Đâu là thủ đô của Việt Nam?"),
    (2, "Câu hỏi 2: 2 + 2 bằng mấy?"),
    (3, "Câu hỏi 3: Python là gì?")
]

danh_sach_cau_tra_loi = [
    (1, "Hà Nội"),
    (2, "A, B"),  # Sai
    (3, "A, B, C, D, E")
]

danh_sach_dap_an = [
    (1, "Hà Nội"),
    (2, "A, C"),  # Đáp án đúng là A và C
    (3, "A, B, C, D, E")
]

# Kiểm tra dữ liệu đầu vào
hop_le, thong_bao_loi = Check_Input(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an)

if hop_le:
    print("Dữ liệu hợp lệ, tiếp tục xử lý...")
    # So sánh câu trả lời
    ket_qua = Compare_Answer(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an)

    # Hiển thị kết quả
    for kq in ket_qua:
        print(kq)
else:
    print(f"Dữ liệu không hợp lệ: {thong_bao_loi}")
