import yaml
import random

def read_yaml_file(file_path: str) -> list:
    """
    Đọc nội dung từ file YAML và trả về danh sách các câu hỏi.

    Parameters:
    - file_path: str - Đường dẫn tới file YAML chứa các câu hỏi.

    Returns:
    - list - Danh sách các câu hỏi được đọc từ file, mỗi câu hỏi là một dict chứa ID, câu hỏi, lựa chọn và đáp án đúng.
    """

    with open(file_path, 'r', encoding='utf-8') as file:
    # Giải thích encoding='utf-8': Chỉ định mã hóa ký tự cho file khi mở để đảm bảo đọc đúng dữ liệu.
    # Đặc biệt là khi file chứa các ký tự đặc biệt hoặc ngôn ngữ không phải là tiếng Anh.
        return list(yaml.safe_load_all(file)) # An toàn hơn load()

def get_questions_by_level(level: str, questions: list) -> list:
    """
    Lọc các câu hỏi theo level được chỉ định.

    Parameters:
    - level: str - Level mong muốn (Ví dụ: 'dễ', 'trung bình', 'khó').
    - questions: list - Danh sách các câu hỏi chứa thông tin câu hỏi và level của chúng.

    Returns:
    - list - Danh sách các câu hỏi phù hợp với level được yêu cầu.
    """

    # Cần có 1 hàm chọn level trước.
    level_mapping = {'dễ': 'easy', 'trung bình': 'medium', 'khó': 'hard'}
    selected_level = level_mapping.get(level)

    filtered_questions = [q for q in questions if q.get('level') == selected_level] # Đây là list comprehension tối ưu hơn viết cụ thể từng dòng lệnh ra
    # Công dụng: Tạo danh sách filtered_questions, chứa các câu hỏi có mức độ (level) phù hợp với selected_level. Cụ thể, nó kiểm tra từng câu hỏi trong danh sách questions và chỉ giữ lại những câu hỏi mà giá trị của khóa 'level' trùng khớp với selected_level đồng thời sử dụng get() để tránh lỗi khi khóa 'level' không có trong câu hỏi.
    # Cấu trúc: new_list = [expression for item in iterable if condition]
    # Giải thích từng phần tử:
    # [q ...]: Mỗi phần tử trong danh sách mới sẽ là q, nơi q đại diện cho từng phần tử trong danh sách questions.
    # for q in questions: Lặp qua từng phần tử q trong danh sách questions.
    # if q.get('level') == selected_level: Đây là điều kiện để kiểm tra xem giá trị của key 'level' trong từng câu hỏi q có bằng với selected_level hay không. Nếu đúng, câu hỏi đó sẽ được thêm vào filtered_questions.

    # Số câu hỏi bạn muốn chọn
    number_of_questions_to_select = "Số câu muốn in ra" # Ví dụ: 20, 30, 50,... Chỗ này có thể để input hoặc mặc định bao nhiêu câu.

    return random.sample(filtered_questions, k=min(number_of_questions_to_select, len(filtered_questions))) if filtered_questions else []
    # Chọn ngẫu nhiên câu hỏi từ danh sách filtered_questions. Nếu danh sách này không rỗng, nó sẽ trả về một danh sách có độ dài bằng min(câu hỏi muốn in ra, câu hỏi đã lọc) được chọn ngẫu nhiên. Nếu danh sách này rỗng, nó sẽ trả về một danh sách rỗng.

# Test
file_path = 'E:\Downloads\cau_hoi.yaml'  
questions = read_yaml_file(file_path)
# print("\n".join(str(question) for question in questions))  # In ra mỗi dict 1 dòng

# Giả sử level đã được chọn từ trước
level = 'dễ'  # Thay đổi giá trị này nếu cần

questions_by_level = get_questions_by_level(level, questions)

for question in questions_by_level:
    # Chỉ in ra câu hỏi theo level thì:
    print(f"Q: {question['Q']}")