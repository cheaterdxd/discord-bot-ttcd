"""GIẢI THÍCH CÁC HÀM Ở DƯỚI"""

"""Bước 1"""
"""Làm hàm Check_Answer cho phép truyền value1 và value2 vào để so sánh:"""
#Nếu value1 bằng value2 thì kết quả trả về True
#ngược lại nếu 2 value không bằng nhau thì kết quả trả về False

"""Bước 2"""
"""Truyền danh sách có sẵn vào. Chỗ này thì em Kiệt chưa biết là ép danh sách vào theo kiểu nào: 1 nhập tay; 2 là truyền theo dạng excel được thống kê sẵn rồi viết lệnh SQL đưa dô"""
#Vì vậy, chỗ này em Kiệt tạo thử cái list tên là my_list. Trong đó có các giá trị [10, 20, 30, 40, 50]

"""Bước 3"""
"""Người dùng lựa chọn cách so sánh để nhập giá trị"""
#Nhập giá trị trực tiếp từ bàn phím (Cách 1).
#Lấy giá trị từ một danh sách có sẵn (Cách 2).

"""Bước 4"""
"""Xử lý lựa chọn"""
#Nếu người dùng chọn cách 1: Sẽ yêu cầu nhập hai giá trị thông qua input(). Sau đó các giá trị này sẽ được so sánh. Chỗ này ép kiểu int để input đưa về kiểu số nguyên. Chứ không thôi nó để kiểu chuỗi thì không thể so sánh giá trị mà nó so sánh số ký tự.
#Nếu người dùng chọn cách 2: Người dùng sẽ nhập chỉ số của các phần tử trong danh sách my_list, sau đó sẽ lấy các giá trị tương ứng và so sánh chúng.
#Kiểm tra tính hợp lệ của chỉ số: Nếu chỉ số người dùng nhập không hợp lệ (ngoài phạm vi của danh sách), chương trình sẽ thoát với thông báo lỗi.

"""Bước 5"""
"""Gọi hàm để so sánh và in kết quả"""
# Mình tạo ra biến result và mình cho bằng với hàm Check_Answer có chứa (value1, value2) để in ra kết quả mà hàm Check_Answer đã làm.


def Check_Answer(value1, value2):
    # So sánh hai giá trị
    if value1 == value2:
        return True  # Nếu giá trị bằng nhau thì trả về True
    else:
        return False # Nếu giá trị không bằng nhau thì trả về False
    
# Danh sách các giá trị
my_list = [10, 20, 30, 40, 50]

# Người dùng lựa chọn cách so sánh
print("Chọn cách so sánh:")
print("1. Nhập giá trị từ bàn phím")
print("2. Lấy giá trị từ danh sách có sẵn")

choice = int(input("Nhập lựa chọn của bạn (1 hoặc 2): "))

if choice == 1:
    # Nhập giá trị từ người dùng
    value1 = int(input("Nhập giá trị thứ nhất: "))
    value2 = int(input("Nhập giá trị thứ hai: "))
elif choice == 2:
    # Lấy giá trị từ danh sách
    print("Danh sách giá trị:", my_list)
    index1 = int(input(f"Nhập chỉ số phần tử thứ nhất (từ 0 đến {len(my_list) - 1}): "))
    index2 = int(input(f"Nhập chỉ số phần tử thứ hai (từ 0 đến {len(my_list) - 1}): "))
    
    # Kiểm tra xem chỉ số có hợp lệ không
    if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):
        value1 = my_list[index1]
        value2 = my_list[index2]
    else:
        print("Chỉ số không hợp lệ!")
        exit()
else:
    print("Lựa chọn không hợp lệ!")
    exit()

# Gọi hàm để so sánh
result = Check_Answer(value1, value2)
print(f"Kết quả so sánh: {result}")