# Giai đoạn 1

- Thực hiện chức năng cho phép user thi patthana trên discord. 
- Câu hỏi: câu hỏi trắc nghiệm nhiều đáp án

- format file câu hỏi là YAML 

### Cách dùng module <code>_cau_hoi.py_</code> và <code>_cau_hoi.yaml_</code>

Mỗi câu hỏi được trình bày như ví dụ trong cau_hoi.yaml

```yaml
ID: 1
Q: "Bạn đang làm gì?"
A:
  - "tôi đang học"
  - "tôi đang nghỉ"
  - "tôi đang đi chơi"
  - "tôi đang ngủ"
RA: A
```

Mỗi câu được ngăn cách bởi dấu ```---```

### Cấu trúc class CAU_HOI_TRAC_NGHIEM
```python 
    id = 0 #: là id của câu hỏi
    quest = "" #: đây là câu hỏi
    answer = [] #: đây là list đáp án của câu hỏi
    r_answer = "" # đây là câu trả lời đúng , short of: right_answer
    u_answer = "" # đây là câu trả lời của user, short of: user_answer
```

### Để lấy đáp án
- Sau khi nhận đáp án từ user. Gọi method của class: <code> get_user_answer </code>

Example: 
```python
u_a = str(input("answer?\n>"))
ret = a.get_user_answer(u_a)
```

### Để check đáp án
- Gọi method <code> check_answer </code>

Example: 
- "a" là 1 instance của ***CAU_HOI_TRAC_NGHIEM***
```python
a.check_answer()
```

# Giai đoạn 2

- Mở rộng các loại câu hỏi

## Lưu ý

### Chạy test ở module 
```python

def hello1():
    print("1")

def hello2():
    print("2")

def hello3():
    print("3")

if __name__ == '__main__': # được chạy trực tiếp
    hello1()
```