def Check_Input(danh_sach_cau_hoi, danh_sach_dap_an, danh_sach_cau_tra_loi):
    """
    Hàm kiểm tra đầu vào cho danh sách câu hỏi, đáp án và câu trả lời.
    
    Argument:
    - danh_sach_cau_hoi (list): Danh sách câu hỏi (mỗi phần tử phải chứa: ID_Cauhoi, STT, Cauhoi).
    - danh_sach_dap_an (list): Danh sách đáp án (mỗi phần tử phải chứa: ID_Dapan, STT, Dapan).
    - danh_sach_cau_tra_loi (list): Danh sách câu trả lời (mỗi phần tử phải chứa: ID_Cautraloi, STT, Cautraloi).

    Return:
    - tuple (bool, str): Trả về True nếu hợp lệ, hoặc False và thông báo lỗi nếu không hợp lệ.
    """
   
    if not danh_sach_cau_hoi: # Kiểm tra nếu danh sách câu hỏi rỗng
        return False, "Danh sách câu hỏi không có dữ liệu!" #Nếu sai thì in ra "Danh sách câu hỏi không có dữ liệu!"
    
    if not danh_sach_dap_an: # Kiểm tra nếu danh sách đáp án rỗng
        return False, "Danh sách đáp án không có dữ liệu!" #Nếu sai thì in ra "Danh sách đáp án không có dữ liệu!"
    
    if not danh_sach_cau_tra_loi: # Kiểm tra nếu danh sách câu trả lời rỗng
        return False, "Danh sách câu trả lời không có dữ liệu!" #Nếu sai thì in ra "Danh sách câu trả lời không có dữ liệu!"
    
    # Kiểm tra các phần tử trong danh sách câu hỏi
    for cau_hoi in danh_sach_cau_hoi: #Cho phần từ cau_hoi duyệt qua từng phần trong danh_sach_cau_hoi
        if len(cau_hoi) != 3 or not isinstance(cau_hoi[0], int) or not isinstance(cau_hoi[1], int) or not isinstance(cau_hoi[2], str):
            #Kiểm tra xem các câu hỏi trong danh sách câu hỏi có đúng 3 phần tử(ID_Cauhoi, STT, Cauhoi) hay không.
            #not isinstance(cau_hoi[0], int): Kiểm tra phần tử đầu tiên của đáp án (ID_Cauhoi) có phải là số nguyên hay không.
            #not isinstance(cau_hoi[1], int): Kiểm tra phần tử thứ hai của đáp án (STT) có phải là số nguyên hay không.
            #not isinstance(cau_hoi[2], str): Kiểm tra phần tử cuối cùng của đáp án (Cauhoi) có phải là chuỗi hay không.
            return False, f"Câu hỏi '{cau_hoi}' không hợp lệ! Phải có dạng (ID_Cauhoi, STT, Cauhoi)." #Nếu không có thì in ra "Câu hỏi ..không hợp lệ! Phải có dạng (ID_Cauhoi, STT, Cauhoi)"
    
    # Kiểm tra các phần tử trong danh sách đáp án
    for dap_an in danh_sach_dap_an:
        if len(dap_an) != 3 or not isinstance(dap_an[0], int) or not isinstance(dap_an[1], int) or not isinstance(dap_an[2], str):
            #Kiểm tra xem các đáp án trong danh sách đáp án có đúng 3 phần tử(ID_Dapan, STT, Dapan) hay không.
            #not isinstance(dap_an[0], int): Kiểm tra phần tử đầu tiên của đáp án (ID_Dapan) có phải là số nguyên hay không.
            #not isinstance(dap_an[1], int): Kiểm tra phần tử thứ hai của đáp án (STT) có phải là số nguyên hay không.
            #not isinstance(dap_an[2], str): Kiểm tra phần tử cuối cùng của đáp án (Dapan) có phải là chuỗi hay không.
            return False, f"Đáp án '{dap_an}' không hợp lệ! Phải có dạng (ID_Dapan, STT, Dapan)."#Nếu không có thì in ra "Đáp án ..không hợp lệ! Phải có dạng (ID_Cauhoi, STT, Cauhoi)"
    
    # Kiểm tra các phần tử trong danh sách câu trả lời
    for cau_tra_loi in danh_sach_cau_tra_loi:
        if len(cau_tra_loi) != 3 or not isinstance(cau_tra_loi[0], int) or not isinstance(cau_tra_loi[1], int) or not isinstance(cau_tra_loi[2], str):
            #Kiểm tra xem các câu trả lời trong danh sách câu trả lời có đúng 3 phần tử(ID_Cautraloi, STT, Cautraloi) hay không.
            #not isinstance(cau_tra_loi[0], int): Kiểm tra phần tử đầu tiên của câu trả lời ID_Cautraloi) có phải là số nguyên hay không.
            #not isinstance(cau_tra_loi[1], int): Kiểm tra phần tử thứ hai của câu trả lời (STT) có phải là số nguyên hay không.
            #not isinstance(cau_tra_loi[2], str): Kiểm tra phần tử cuối cùng của câu trả lời (Cautraloi) có phải là chuỗi hay không.
            return False, f"Câu trả lời '{cau_tra_loi}' không hợp lệ! Phải có dạng (ID_Cautraloi, STT, Cautraloi)." #Nếu không có thì in ra "Câu trả lời ..không hợp lệ! Phải có dạng (ID_Cauhoi, STT, Cauhoi)"
    
    return True, None # Nếu tất cả đều hợp lệ thì tiếp tục chương trình, không thì dừng chương trình.

# Ví dụ kiểm tra đầu vào:
danh_sach_cau_hoi = [
    (1, 1, "Thủ đô của Việt Nam là gì?"),
    (2, 2, "2 + 2 bằng bao nhiêu?")
]
danh_sach_dap_an = [
    (1, 1, "Hà Nội"),
    (2, 2, "4")
]
danh_sach_cau_tra_loi = [
    (1, 1, "Hà Nội"),
    (2, 2, "5")
]

# Gọi hàm kiểm tra
Check_Result, thong_bao_loi = Check_Input(danh_sach_cau_hoi, danh_sach_dap_an, danh_sach_cau_tra_loi)

if Check_Result:
    print("Dữ liệu đầu vào hợp lệ!")
else:
    print(f"Lỗi đầu vào: {thong_bao_loi}")


# Hàm kiểm tra câu trả lời
def check_answer(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an):
    """
    Hàm so sánh câu trả lời của người dùng với đáp án đúng.
    
    Args:
    - danh_sach_cau_hoi (list): Danh sách câu hỏi (ID_Cauhoi, STT, Cauhoi).
    - danh_sach_cau_tra_loi (list): Danh sách câu trả lời của người dùng (ID_Cautraloi, STT, Cautraloi).
    - danh_sach_dap_an (list): Danh sách đáp án đúng (ID_Dapan, STT, Dapan).

    Returns:
    - list: Danh sách các thông báo về kết quả câu trả lời.
    """
    
    ket_qua = []
    
    # Duyệt qua từng câu hỏi
    for i in range(len(danh_sach_cau_hoi)):
        id_cauhoi, stt_cauhoi, cau_hoi = danh_sach_cau_hoi[i]   # Lấy ID, STT, và câu hỏi
        id_dapan, stt_dapan, dap_an_dung = danh_sach_dap_an[i]  # Lấy ID, STT, và đáp án đúng
        
        # Kiểm tra nếu người dùng không trả lời
        if i >= len(danh_sach_cau_tra_loi) or danh_sach_cau_tra_loi[i][2].strip() == "":
            ket_qua.append(f"Câu hỏi: {cau_hoi}\nBạn chưa trả lời câu hỏi này!")
        else:
            id_traloi, stt_traloi, cau_tra_loi = danh_sach_cau_tra_loi[i]  # Lấy ID, STT, và câu trả lời của người dùng
            
            # So sánh câu trả lời với đáp án đúng
            if cau_tra_loi.strip().lower() == dap_an_dung.strip().lower():
                ket_qua.append(f"Câu hỏi: {cau_hoi}\nĐáp án '{cau_tra_loi}' là đáp án đúng.")
            else:
                ket_qua.append(f"Câu hỏi: {cau_hoi}\nĐáp án '{cau_tra_loi}' là đáp án sai, đáp án đúng là '{dap_an_dung}'.")
    
    return ket_qua


Check_Result, thong_bao_loi = Check_Input(danh_sach_cau_hoi, danh_sach_dap_an, danh_sach_cau_tra_loi)

if Check_Result:
    # Gọi hàm check_answer để kiểm tra câu trả lời
    ket_qua = check_answer(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an)
    
    # Hiển thị kết quả
    for kq in ket_qua:
        print(str(kq))
else:
    print(f"Lỗi đầu vào: {thong_bao_loi}")
