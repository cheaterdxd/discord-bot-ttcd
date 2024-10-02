import re  # Import thư viện re để sử dụng các biểu thức chính quy (regular expressions)

def standardize_input() -> str:
    """
    Hàm chuẩn hóa dữ liệu đầu vào

    Parameter: 
    - "Không có tham số truyền vào"

    Return:
    str: Chuỗi đã được chuẩn hóa.
    """
    
    while True:  # Vòng lặp để yêu cầu người dùng nhập lại nếu chuỗi không hợp lệ
        user_input = input("Nhập chuỗi: ")  # Người dùng nhập chuỗi trực tiếp

        # Bước 1: Kiểm tra và loại bỏ dấu cách ở đầu và đuôi
        # Strip() để xóa dấu cách ở đầu và cuối chuỗi
        # Upper() để chuyển tất cả các ký tự thành chữ in hoa
        standardized_input = user_input.strip().upper()

        # Bước 2: Loại bỏ tất cả các ký tự đặc biệt (chỉ giữ chữ cái, số, và khoảng trắng)
        # Sử dụng re.sub() để thay thế tất cả các ký tự không phải chữ cái hoặc số
        standardized_input = re.sub(r'[^\w\s]', '', standardized_input)
        # Giải thích:
        # [^\w\s]: tìm và loại bỏ mọi ký tự không phải là chữ cái (a-z, A-Z), số (0-9) hoặc khoảng trắng.
        # Ký tự ^ ở đầu biểu thức chỉ định phủ định (nghĩa là tìm những ký tự không thuộc tập hợp này).

        # Bước 3: Chuyển nhiều dấu cách thành một dấu cách
        # re.sub() với biểu thức \s+ thay thế tất cả khoảng trắng liên tiếp (một hoặc nhiều) bằng một khoảng trắng duy nhất
        standardized_input = re.sub(r'\s+', ' ', standardized_input)

        # Bước 4: Kiểm tra nếu chuỗi đã chuẩn hóa là rỗng
        if standardized_input:
            # Nếu chuỗi hợp lệ (không rỗng), thoát khỏi vòng lặp while
            break
        else:
            # Nếu chuỗi rỗng hoặc không hợp lệ, yêu cầu người dùng nhập lại
            print("Chuỗi đầu vào không hợp lệ, hãy nhập lại.")
    
    return standardized_input  # Trả về chuỗi đã chuẩn hóa
# Ví dụ test thử gồm dòng 43 và 44
a = standardize_input()
print(a)