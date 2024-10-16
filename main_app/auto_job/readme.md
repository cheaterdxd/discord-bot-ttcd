# Giới thiệu
## Vấn đề
Chức năng cho phép admin quản trị discord có thể không lo lắng vấn đề gắn role cho học viên.

## Giải quyết
Cho phép việc gắn role không cần sự can thiệp của quản trị viên, học viên chỉ cần thực hiện cung cấp email đã xác nhận khi đăng ký khóa học.

# Các bước thực hiện

1. User nhập thông tin xác thực
2. Lấy thông tin xác thực truy xuất trên dữ liệu google sheet của ban quản trị
3. Nếu đúng thì trả về những Role của lớp mà học viên đăng ký
4. Nếu Role cũ (học viên đã đăng ký trước đó & đã được cấp role) thì không hiển thị. 
5. Học viên sẽ chọn role từ danh sách trả về, nếu phù hợp thì cấp role


