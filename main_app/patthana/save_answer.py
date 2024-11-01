# Tạo dictionary để lưu trữ cặp ID câu hỏi và câu trả lời của học viên
question_answer_dict = {} 

def manage_data_dict(question_id: int, student_answer: str = None, action: str = "add"):
    """
    Hàm quản lý cặp giá trị [ID câu hỏi, câu trả lời học viên] trong dictionary.
    
    Parameters:
    - question_id: int - ID của câu hỏi.
    - student_answer: str - Câu trả lời của học viên (dùng khi action là 'add').
    - action: str - Hành động ('add', 'remove', 'get', 'list_all').

    Tác dụng:
    - Thực hiện thêm, xóa, truy xuất, hoặc thống kê tất cả cặp dữ liệu trong question_answer_dict.
    """
    # Kiểm tra tính hợp lệ của action
    if action not in {"add", "remove", "get", "list_all"}:
        raise ValueError("Hành động không hợp lệ! Chỉ chấp nhận 'add', 'remove', 'get', hoặc 'list_all'.")
    # Dùng raise ValueError() sẽ tốt hơn print() ở rất nhiều mặt.

    global question_answer_dict

    # Thêm cặp [ID câu hỏi (key), Câu trả lời (value)] vào  " question_answer_dict ""
    if action == 'add':
        if question_id in question_answer_dict: #Chỗ này anh Hoan chưa có. Mục đích là tránh ghi đè không mong muốn.
            print(f"Câu hỏi {question_id} đã tồn tại. Đã cập nhật câu trả lời.")
        question_answer_dict[question_id] = student_answer  # đây là câu lệnh trong mảng  dictionary, giúp thêm cặp giá trị câu hỏi (key) và câu trả lời (value) vào mảng, cú pháp khái quát dict[key]=value
        print(f"Đã thêm cặp giá trị {question_id}: '{student_answer}'")

   # Xóa cặp dữ liệu dựa trên ID câu hỏi (key)
    elif action == 'remove':
        if question_answer_dict.pop(question_id, None) is not None: # Dùng pop sẽ tối ưu hóa hơn vòng lặp for của anh Hoan. Ngắn hơn, dễ đọc hơn và giảm thiểu rủi ro khi tác động vào dic.
            print(f"Đã xóa câu hỏi: {question_id}")
        else:
            print(f"Không tìm thấy câu hỏi {question_id} để xóa!")

    # Truy xuất câu trả lời dựa trên ID câu hỏi (key)
    elif action == 'get':
        answer = question_answer_dict.get(question_id)
        if answer is not None: # Trả về giá trị trực tiếp thay vì chỉ in, cho phép linh hoạt hơn khi sử dụng hàm (ví dụ, có thể lưu giá trị hoặc in ra khi cần thiết).
            print(f"Truy xuất: {question_id} -> {answer}")
            return answer
        else:
            print(f"Không tìm thấy câu hỏi {question_id}!")

    # Thống kê tất cả câu hỏi và câu trả lời
    elif action == 'list_all':
        if question_answer_dict:
            print("Danh sách câu hỏi và câu trả lời:")
            for key, value in sorted(question_answer_dict.items()):# Sử dụng sorted() để sắp xếp cặp câu hỏi - câu trả lời theo question_id trước khi in, giúp người dùng dễ theo dõi.
                print(f"{key} -> {value}")
        else:
            print("Không có dữ liệu nào.")
            # Kiểm tra trước khi in để đảm bảo dictionary không rỗng, giúp cải thiện trải nghiệm người dùng khi không có dữ liệu nào.
    else:
        print(f"Hành động '{action}' không hợp lệ.")
