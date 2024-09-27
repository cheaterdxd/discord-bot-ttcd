#Nhiệm vụ tuần 1: 20/09-26/09
#  Ok - Hiểu được lý do phải sử dụng github và cách vận hành của github, thông qua xem video hướng dẫn tại https://www.youtube.com/watch?v=q8xE-6HijbE
#  Tạm ổn - Hiểu được cách khai báo, sử dụng hàm 
#   - Hoàn thành tất cả bài tập dược giao 
# + xem xong video => hoàn thành 
# + thực hành theo video 
# + Tạo 1 file python, code 1 thứ bất kỳ (có thể lấy từ lớp anh Tod): yêu cầu trình bày dưới dạng module function (hàm). => hoàn thành.
# + Với file vừa tạo, hãy tạo commit trong github desktop và push file lên branch main. 

def quy_doi_tien(ngoai_te,ty_gia):
    quydoi=  ngoai_te * ty_gia
    return quydoi

print ("Thành tiền: ", quy_doi_tien(int(input("Nhập ngoại tệ:")),int(input("Nhập tỷ giá:")))  , "VND")