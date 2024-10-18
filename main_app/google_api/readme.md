# Hướng dẫn thao tác với Google sheet api

1. Cần credentials.json mới chạy được
2. Cần chỉnh Sheet ranges cho chính xác

# Các file được xây dựng

### authenticator.py
- có hàm authen_me có nhiệm vụ trả về 1 service resource để gọi API 

### work_with_sheets_data.py
- hàm read_sheet_at
    + service_api
    + sheet_id
    + sheet_range
