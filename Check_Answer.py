def Check_Answer(value1, value2):
    """
    Hàm kiểm tra câu trả lời (Hay nói cách khác là Hàm kiểm tra giá trị) 

    Parameter: 
    - Truyền vào tham số value1
    - Truyền vào tham số value2

    Return:
    - Trả về True nếu bằng nhau
    - Trả về False nếu không bằng nhau
"""
    if value1 == value2: #Nếu value1 bằng value2 thì
        return True #Trả về True
    else: #Ngược lại thì không bằng
        return False #Trả về False


def input_values():
    """Hàm nhập giá trị

    Parameter: 
    - "Không có tham số truyền vào"

    Return:
    - Trả về value1 và value2
"""
    value1 = int(input("Nhập giá trị thứ nhất: "))# Tạo biến cục bộ tên là value1 và cho phép nhập từ bàn phím
    value2 = int(input("Nhập giá trị thứ hai: "))# Tạo biến cục bộ tên là value2 và cho phép nhập từ bàn phím
    return value1, value2 #Trả về value1 và value2


def select_from_list(my_list):
    """Hàm lấy giá trị từ danh sách

    Parameter: 
    - Truyền vào danh sách my_list
     
    Return:
    - Trả về chỉ số index1 và index2
"""
    print("Danh sách giá trị:", my_list) #in danh sách my_list
    index1 = int(input(f"Nhập chỉ số phần tử thứ nhất (từ 0 đến {len(my_list) - 1}): ")) # Tạo biến cục bộ tên là index1 và cho phép nhập chỉ số từ 0 đến độ dài cuối cùng của danh sách bằng cách {len(my_list) - 1}
    index2 = int(input(f"Nhập chỉ số phần tử thứ hai (từ 0 đến {len(my_list) - 1}): ")) # Tạo biến cục bộ tên là index2 và cho phép nhập chỉ số từ 0 đến độ dài cuối cùng của danh sách bằng cách {len(my_list) - 1}
    
    if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):  # Hàm len(my_list) trả về số lượng phần tử trong danh sách my_list.
            # Vì chỉ số danh sách được bắt đầu từ 0. Vì vậy, chỉ số (index) lớn nhất của danh sách sẽ là len(my_list) - 1.
            # Ví dụ: Nếu my_list=[10, 20, 30, 40, 50], thì len(my_list) tức độ dài sẽ là 5, và chỉ số lớn nhất sẽ là 5 - 1 = 4. Vậy nên chỉ số hợp lệ sẽ là từ 0 đến 4.
        return my_list[index1], my_list[index2] #Trả về chỉ số index1 và index2 trong danh sách my_list
    else: #Ngược lại thì không trả về
        print("Chỉ số không hợp lệ!") # in thông báo "Chỉ số không hợp lệ"
        exit()# Sau đó dừng chương trình.


def main():
    """
    Hàm chính (Có thể hiểu đây là hàm dùng để gọi để chạy các function)
   
    Parameter: 
    - "Không có tham số truyền vào"

    Return:
    - "Không có giá trị trả về"
"""
    my_list = [10, 20, 30, 40, 50] #Khai báo danh sách my_list = [10, 20, 30, 40, 50]

    # Người dùng lựa chọn cách so sánh
    print("Chọn cách so sánh:") #lệnh in ra màn hình câu "Chọn cách so sánh:"
    print("1. Nhập giá trị từ bàn phím") #lệnh in ra màn hình câu "1. Nhập giá trị từ bàn phím:"
    print("2. Lấy giá trị từ danh sách có sẵn") #lệnh in ra màn hình câu "2. Lấy giá trị từ danh sách có sẵn:"

    choice = int(input("Nhập lựa chọn của bạn (1 hoặc 2): ")) #Tạo biến cục bộ tên là choice và cho phép nhập từ bàn phím

    #Sử dụng hàm if để phân chia lựa chọn của người dùng là tự nhập từ bàn phím hay chọn từ danh sách có sẵn (my_list)
    if choice == 1: #Nếu choice nhập có giá trị = 1
        value1, value2 = input_values() #Tạo biến cục bộ là value1, value2 gán với hàm input_values(). Vì hàm input_values() trả về hai giá trị nên 2 giá trị đó lần lượt bằng với value1 và value2 ở biến cục bộ này.
    elif choice == 2: #Nếu choice nhập có giá trị = 2
        value1, value2 = select_from_list(my_list) #Tạo biến cục bộ là value1, value2 gán với hàm select_from_list(my_list). Vì hàm select_from_list(my_list) trả về hai giá trị nên 2 giá trị đó lần lượt bằng với value1 và value2 ở biến cục bộ này.
    else: #Nếu không bằng 2 và không bằng 1
        print("Lựa chọn không hợp lệ!") # in ra màn hình "Lựa chọn không hợp lệ!"
        exit() #Thoát tiến trình ngay lập tức.


    # Sau khi có được 2 giá trị phù hợp thì gọi hàm để so sánh
    result = Check_Answer(value1, value2) #Tạo biến cục bộ tên result gán với hàng Check_Answer(value1,value2). Vì hàm Check_Answer(value1,value2) sẽ trả về True hoặc False
    print(f"Kết quả so sánh: {result}") #in ra màn hình "Kết quả so sánh: " kèm theo result


main() # Chạy chương trình chính
