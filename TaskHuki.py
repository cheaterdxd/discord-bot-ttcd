# Nguoi dung nhap cac gia tri a,b,y
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
y = float(input("Nhập giá trị của y: "))

# Ham tinh Phuong trinh bac nhat mot an x
def giai_pt_bac_nhat(a, b, y):
    
    if a == 0:
        if b == y:
            return "Phương trình có vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        x = (y - b) / a
        return x


# Goi ham va in ket qua
nghiem = giai_pt_bac_nhat(a, b, y)
print(f"Nghiệm của phương trình là: {nghiem}")