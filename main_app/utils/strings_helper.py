import re

def clean_email(email: str) -> str:
    # Bước 1: Loại bỏ khoảng trắng thừa
    email = email.strip()
    
    # Bước 2: Chuyển về chữ thường
    email = email.lower()
    
    # Bước 3: Kiểm tra định dạng email hợp lệ
    # email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # if not re.match(email_regex, email):
    #     raise ValueError("Invalid email format")
    
    return email

def is_mail_address(input_mail_address)-> bool:
    """
    Hàm kiểm tra xem input_mail_address có phải là địa chỉ email hay không.

    Parameters:
        input_mail_address (str): Email cần kiểm tra

    Returns:
        - True nếu input_mail_address là đầu chỉ email
        - False nếu input_mail_address không phải là đầu chỉ email

    """

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, input_mail_address):
        return True
    else:
        return False

def is_phone_number(input_phone_number) -> bool:
    """
    Hàm kiểm tra xem input_phone_number có phải là số điện thoại hay không.

    Parameters:
        input_phone_number (str): Số điện thoại cần kiểm tra

    Returns:
        - True nếu input_phone_number là số điện thoại
        - False nếu input_phone_number không phải là số điện thoại
    
    """
    phone_number_regex = r'^\+?[0-9]{1,3}-?[0-9]{1,4}-?[0-9]{7,8}$'
    if re.match(phone_number_regex, input_phone_number):
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_phone_number('0971260877he'))