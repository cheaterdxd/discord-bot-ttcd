#Nhiệm vụ tuần 1: 27/09-03/10
# Viết 1 hàm, đặt tên bất kỳ, thực hiện các nhiệm vụ sau: 
# - nhận tham số: 
# + ID câu hỏi
# + Câu trả lời của học viên

#- Tạo 1 mảng global để chứa cặp giá trị [ID câu hỏi, câu trả lời học viên] 
# - Thực hiện được các thao tác: thêm, xóa, truy xuất cặp dữ liệu vào dạng dữ liệu mảng

# Chọn loại dữ liêu mảng (trong python) nào để lưu cặp dữ liệu, hãy viết báo cáo lý luận vì sao dùng kiểu dữ liệu đó để xử lý mà không phải cặp khác.  

# Khai báo mảng global là từ điển  (kiểu từ điển có dạng a= { key1 : value 1, key2: value 2,....})
question_answer_dict = {}  # tên mang tính gợi nhớ nhiệm vụ và kiểu dữ liệu, khai báo rỗng, để chờ mình đổ dữ liệu vào.

# Định nghĩa hàm
def manage_data_dict(question_id, student_answer, action): # chỗ action rất hay (AI gợi ý hay), nó khái quát hóa để vô ruột mình chia trường  hợp: thêm, xóa, truy xuất, thống kê
    # question_id : biến mang câu hỏi , kiểu dữ liệu string
    # student_answer: biến mang câu trả lời, kiểu dữ liệu string
    global question_answer_dict  # Khai báo sử dụng biến toàn cục
    
    # Thêm cặp [ID câu hỏi (key), Câu trả lời (value)] vào  " question_answer_dict ""
    if action == 'add':  # add: cụm từ gợi nhớ cách hành động 
        question_answer_dict[question_id] = student_answer # đây là câu lệnh trong mảng  dictionary, giúp thêm cặp giá trị câu hỏi (key) và câu trả lời (value) vào mảng, cú pháp khái quát dict[key]=value
        print("Đã thêm cặp giá trị {question_id} : {student_answer}" ) # thông báo để người dùng biết vừa cập nhập thông tin gì
    
   # Xóa cặp dữ liệu dựa trên ID câu hỏi (key)
    elif action == 'remove':  # remove: cụm từ gợi nhớ cách hành động , elif: nếu điều kiện if không thõa thì chạy điều kiện này
        if question_id in question_answer_dict: #  hàm in: kiểm tra sự tồn tại của khóa
            del question_answer_dict[question_id] # xóa cặp câu hỏi : câu trả lời
            print(f"Đã xóa: {question_id}")
        else:
            print(f"Không tìm thấy câu hỏi {question_id} để xóa!")
    
    # Truy xuất câu trả lời dựa trên ID câu hỏi (key)
    elif action == 'get': # get: cụm từ gợi nhớ cách hành động
        if question_id in question_answer_dict: #  hàm in: kiểm tra sự tồn tại của khóa
            print(f"Truy xuất: {question_id} -> {question_answer_dict[question_id]}")
            return question_answer_dict[question_id] # kết thúc việc thực thi hàm và gửi giá trị lại cho nơi được gọi
        else:
            print("Không tìm thấy câu hỏi {question_id}!")
    
    # Liệt kê tất cả câu hỏi và câu trả lời
    elif action == 'list_all':  # list_all: cụm từ gợi nhớ cách hành động
        for key, value in question_answer_dict.items(): # for.. in: vòng lặp , lặp laị việc tìm các cặp key, value trong dữ liệu  ;;; 
            # question_answer_dict.items() : hàm này trả về danh sách tất cả các cặp key-value ( câu hỏi - câu trả lời)  dưới dạng kiểu dữ liệu Tuple
            # sau khi thực hiện hàm này thì question_answer_dict=[(key 1,value 1), (key 2,value 2),.....,(key n, value n)]
            print(f"{key} -> {value}")