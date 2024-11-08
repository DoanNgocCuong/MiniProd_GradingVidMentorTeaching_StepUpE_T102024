1.3.3: Ghép luồng từ Database hiển thị lên UI view 1 - view xem video và chấm. 
- Đóng 1 workflow để lấy data từ Drive đổ về Database
(1 API Whisper, 1 API Prompting cho việc từ Transcription thành luồng)
- (frontend như cũ. Backend đóng 1 API để lấy dữ liệu từ database)
1.3.4_combine_update: 
- Cường: folder test (10 video chị Quyên sẽ chấm)
- Cường: Lưu điểm, note chị Quyên chấm + feedback
(frontend, backend đóng thêm 2 API: update điểm từ UI xuống database, API get score từ database ngược trở lại UI view 1)

1.3.5 

- Cường: Ghép 2 giao diện vào nhau 
- Tinh chỉnh lại Prompting. 
- Minh: Define phần folder chấm + cách thêm Audio
------------------------------------------------------
- Cường: Đóng phần lấy thông tin video thành api