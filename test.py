def find_max(numbers):
    if not numbers:
        return None  # Trả về None nếu danh sách trống
    max_number = numbers[0]  # Giả sử phần tử đầu tiên là lớn nhất
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number
