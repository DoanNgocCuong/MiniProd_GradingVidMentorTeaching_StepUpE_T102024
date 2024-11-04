Demo: https://drive.google.com/drive/folders/1_oVkhMaU4M1-ZIkb5sL4XSRE1LmZUn3z
===========

Đây là một chương trình Python thực hiện các chức năng sau:

1. **Xử lý file từ Google Drive**:
- Kết nối với Google Drive API để truy cập và tải xuống các file từ một thư mục cụ thể
- Xử lý cả file video và file audio từ các thư mục tương ứng

2. **Xử lý Audio và Tạo Transcript**:
- Sử dụng API Whisper (qua URL `http://103.253.20.13:25029/role_assign`) để chuyển đổi audio thành text
- Xử lý 2 loại file audio: từ học viên (HV) và mentor
- Kết hợp transcript từ cả 2 người nói và định dạng thời gian

3. **Quản lý Database**:
- Tạo và quản lý SQLite database để lưu trữ thông tin:
  - Tên file video/audio
  - URL của video/audio
  - Nội dung transcript
- Có các chức năng thêm và xem dữ liệu

4. **Tổ chức File**:
- Tạo cấu trúc thư mục local để lưu trữ:
  - Thư mục Audio cho file âm thanh
  - Thư mục Text cho file transcript
  - Thư mục Transcript cho kết quả cuối cùng

Mục đích chính của code này có vẻ là để tự động hóa quá trình:
1. Tải file từ Google Drive
2. Chuyển đổi audio thành text
3. Tổ chức và lưu trữ dữ liệu một cách có hệ thống