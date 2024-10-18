import re  # Import thư viện re để sử dụng các biểu thức chính quy (regular expressions)

def standardize_input(user_input: str) -> str:
    """
    Hàm chuẩn hóa dữ liệu đầu vào.

    Parameter:
    - user_input (str): Chuỗi dữ liệu đầu vào cần chuẩn hóa.

    Return:
    - str: Chuỗi đã được chuẩn hóa.
    """
    # Bước 1: Kiểm tra xem user_input có phải rỗng không 
    if not user_input.strip():
        return "Chuỗi không được để trống. Vui lòng nhập lại."

    # Bước 2: Kiểm tra và loại bỏ dấu cách ở đầu và đuôi
    # Strip() để xóa dấu cách ở đầu và cuối chuỗi
    # Upper() để chuyển tất cả các ký tự thành chữ in hoa
    standardized_input = user_input.strip().upper()

    # Bước 3: Loại bỏ tất cả các ký tự đặc biệt (chỉ giữ chữ cái, số, và khoảng trắng)
    # Sử dụng re.sub() để thay thế tất cả các ký tự không phải chữ cái hoặc số
    standardized_input = re.sub(r'[^\w\s]', '', standardized_input)
    # Giải thích:
    # [^\w\s]: tìm và loại bỏ mọi ký tự không phải là chữ cái (a-z, A-Z), số (0-9) hoặc khoảng trắng.
    # Ký tự ^ ở đầu biểu thức chỉ định phủ định (nghĩa là tìm những ký tự không thuộc tập hợp này).

    # Bước 4: Chuyển nhiều dấu cách thành một dấu cách
    # re.sub() với biểu thức \s+ thay thế tất cả khoảng trắng liên tiếp (một hoặc nhiều) bằng một khoảng trắng duy nhất
    standardized_input = re.sub(r'\s+', ' ', standardized_input)

    # Bước 5: Kiểm tra chuỗi đã chuẩn hóa có phải rỗng không
    if not standardized_input:
        return "Chuỗi chỉ chứa ký tự đặc biệt. Vui lòng nhập lại."

    # Trả về chuỗi đã chuẩn hóa
    return standardized_input