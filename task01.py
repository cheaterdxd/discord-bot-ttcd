def main():
    # Tạo một danh sách để lưu trữ tên của 10 người
    names = []

    # Nhập tên của 10 người
    for i in range(10):
        name = input(f"Nhập tên người thứ {i+1}: ")
        names.append(name)

    # Kiểm tra và xuất ra thông báo tương ứng
    for name in names:
        first_name = name.split()[0]
        if first_name == "Lê":
            print(f"{name}: họ Lê")
        else:
            print(f"{name}: không phải họ Lê")

if __name__ == "__main__":
    main()