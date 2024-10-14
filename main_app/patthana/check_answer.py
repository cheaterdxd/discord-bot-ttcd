def Check_Input(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an):
    """
    Hàm kiểm độ dài đầu vào của các danh sách.

    Parameter:
    - danh_sach_cau_hoi (list): Danh sách câu hỏi.
    - danh_sach_cau_tra_loi (list): Danh sách câu trả lời của người dùng.
    - danh_sach_dap_an (list): Danh sách đáp án đúng.

    Return:
    - Nếu sai thì trả về thông báo và dừng quá trình xử lý.
    - Nếu đúng thì tiếp tục quy trình xử lý
    """

    # Kiểm tra độ dài của danh sách
    if len(danh_sach_cau_hoi) != len(danh_sach_cau_tra_loi) or len(danh_sach_cau_hoi) != len(danh_sach_dap_an): # Kiểm tra độ dài của danh sách câu hỏi, câu trả lời và đáp án.
        return False, "Số lượng câu hỏi, câu trả lời, và đáp án không khớp!" #Trả về False nếu Số lượng câu hỏi, câu trả lời, và đáp án không khớp! và dừng xử lý.
    return True, None #Trả về True thì không có gì xảy ra và tiếp tục xử lý.


def Compare_Answer(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an):
    """
    Hàm so sánh câu trả lời của người dùng và đáp án đúng.

    Parameter:
    - danh_sach_cau_hoi (list): Danh sách câu hỏi.
    - danh_sach_cau_tra_loi (list): Danh sách câu trả lời của người dùng.
    - danh_sach_dap_an (list): Danh sách đáp án đúng.

    Return:
    - Danh sách câu hỏi kèm kết quả trả lời của người dùng.
    """

    # Kiểm tra đầu vào
    hop_le, thong_bao_loi = Check_Input(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an) #Tạo hai biến là hop_le và thong_bao_loi cho phép bằng với ham kim__tra_dau_vao
    if not hop_le: #Nếu không hợp lệ thì:
        return [thong_bao_loi] #Trả về thông báo lỗi
    
    ket_qua = []
    
    # Duyệt qua từng câu hỏi và so sánh câu trả lời với đáp án
    for i in range(len(danh_sach_cau_hoi)): #Sử dụng vòng lặp tạo một dãy số từ 0 đến len(danh_sach_cau_hoi)-1.len(danh_sach_cau_hoi) để trả về số lượng phần tử trong danh sách câu hỏi.
        cau_hoi_hien_tai = danh_sach_cau_hoi[i] #Lấy phần tử thứ i trong danh_sach_cau_hoi và gán vào biến cau_hoi_hien_tai. Điều này có nghĩa là ở mỗi lần lặp, biến này sẽ chứa câu hỏi hiện tại đang được xét.
        dap_an_nguoi_dung = danh_sach_cau_tra_loi[i] #Tương tự, lấy phần tử thứ i trong danh_sach_cau_tra_loi và gán vào biến dap_an_nguoi_dung. Biến này sẽ chứa câu trả lời mà người dùng đã chọn cho câu hỏi hiện tại.
        dap_an_dung = danh_sach_dap_an[i] #Lấy phần tử thứ i trong danh_sach_dap_an và gán vào biến dap_an_dung. Biến này sẽ chứa đáp án đúng cho câu hỏi hiện tại.
        # -> Nói nôm na, dễ hình dung thì chỗ này là chúng ta đang duyệt qua từng giá trị, rồi mang các giá trị đó đặt vào một cái bảng vô hình có các cột: Số lần lặp, số i, câu hỏi hiện tại, đáp án người dùng, đáp án đúng sao cho đúng thứ tự

        # Kiểm tra nếu người dùng bỏ trống câu trả lời
        if dap_an_nguoi_dung.strip() == "": #Nói nôm na là hàm strip() sẽ loại bỏ các khoảng trắng thừa ở đầu và cuối chuỗi dap_an_nguoi_dung. Điều này giúp đảm bảo rằng nếu người dùng chỉ nhập các khoảng trắng, nó sẽ được coi là chưa trả lời. và =="" là để kiểm tra xem chuỗi sau khi loại bỏ là có Rỗng thiệt sự chưa.
            ket_qua.append(f"{cau_hoi_hien_tai}: Bạn đã không trả lời.") #Nếu điều kiện ở trên đúng, thì hàm append sẽ giúp chúng ta thêm phần tử (cau_hỏi_hien_tai và thông báo "Bạn đã không trả lời.") vào danh sách ket_qua.
        elif dap_an_nguoi_dung == dap_an_dung: #Ngược lại, nếu dap_an_nguoi_dung bằng với dap_an_dung thì:
            ket_qua.append(f"{cau_hoi_hien_tai}: Bạn đã chọn đúng.") #Thì hàm append sẽ giúp chúng ta thêm phần tử (cau_hỏi_hien_tai và thông báo "Bạn đã chọn đúng.") vào danh sách ket_qua.
        else: #Ngược lại, nếu dap_an_nguoi_dung không bằng với dap_an_dung thì:
            ket_qua.append(f"{cau_hoi_hien_tai}: Bạn đã trả lời sai, bạn chọn {dap_an_nguoi_dung}, đáp án đúng là {dap_an_dung}.") #Thì hàm append sẽ giúp chúng ta thêm phần tử (cau_hoi_hien_tai: Bạn đã trả lời sai, bạn chọn {dap_an_nguoi_dung}, đáp án đúng là {dap_an_dung}.) vào danh sách ket_qua.
    
    return ket_qua #Trả về kết quả

#Trời ơi comment một hồi chóng mặt quớ huhu hichic. Nhưng cố gắng giải thích cho các bạn thân thương của Kiệt hehe < 3


# Mình giả sử khai báo một danh sách câu hỏi
danh_sach_cau_hoi = [
    "Câu hỏi 1: Nguyên nhân của Khổ có mấy?",
    "Câu hỏi 2: Sự thật là gì?",
    "Câu hỏi 3: Có bao nhiêu loại sự thật?"
]

danh_sach_cau_tra_loi = ["8", "", "3"] # Mình giả sử khai báo một danh sách câu trả lời
danh_sach_dap_an = ["8", "Sự thật là một sự vật hiện tượng đúng với tất cả các trường, mọi thời điểm, mọi không gian. Dù ta có như thế nào thì nó vẫn diễn ra như vậy như vậy.", "5"] # Mình giả sử khai báo một danh sách đáp án

ket_qua = Compare_Answer(danh_sach_cau_hoi, danh_sach_cau_tra_loi, danh_sach_dap_an) #Kết quả câu trả lời là kết quả mà hàm Compare_Answer đã làm ở trên

# Hiển thị kết quả
for kq in ket_qua: #Mình chọn vòng lặp for để lập qua từng phần tử trong dãy dữ liệu của ket_qua. Sau đó lưu vào biến tạm là kq
    print(kq) #Chỗ này là in ra kết quả

#Để Kiệt ví dụ vầy đi cho dễ hiểu he. Giả sử chúng ta đã thu được danh sách ket_qua như bên dưới nhe: 
""" ket_qua = ["Câu hỏi 1: Bạn đã chọn đúng.", "Câu hỏi 2: Bạn đã trả lời sai.", "Câu hỏi 3: Bạn đã không trả lời."]"""

#Khi chạy vòng lập for thì kết quả sẽ được hiển thị vầy nè:
"""
    Câu hỏi 1: Bạn đã chọn đúng.
    Câu hỏi 2: Bạn đã trả lời sai.
    Câu hỏi 3: Bạn đã không trả lời.
"""
 #Nhìn mướt và dễ hiểu nhiều. Nhìn nó tường minh hơn.
#Rồi nhe, xie xie, làm tới đây đuối như chái chúi rồi mina ơi @@. Có gì hông hiểu hỏi tui nhe. Chúc anh em ngày mới dui dẻ < 3

