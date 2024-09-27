import random
danh_sach = input("Nhập các số, cách nhau bởi khoảng trắng: ").split()
n = len(danh_sach)
for i in range(n - 1, 0, -1):
    j = random.randint(0, i)
    print(danh_sach[j], end=' ')
    danh_sach[j] = danh_sach[i]
    danh_sach[i] = danh_sach[j]
print(danh_sach[0])