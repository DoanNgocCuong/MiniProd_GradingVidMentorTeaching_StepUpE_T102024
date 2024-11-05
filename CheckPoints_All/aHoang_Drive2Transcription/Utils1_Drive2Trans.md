Demo: https://drive.google.com/drive/folders/1_oVkhMaU4M1-ZIkb5sL4XSRE1LmZUn3z
===========

# 1. CÁCH CHẠY 

Đây là một chương trình Python thực hiện các chức năng sau:

1. **Xử lý file từ Google Drive**:
- Kết nối với Google Drive API để truy cập và tải xuống các file từ một thư mục cụ thể
Cách kết nối: https://console.cloud.google.com/apis/credentials/oauthclient

- Xử lý cả file video và file audio từ các thư mục tương ứng

Lỗi bạn gặp phải là do API Google Drive chưa được kích hoạt cho dự án mà bạn đang sử dụng. Cụ thể, thông báo lỗi cho biết:

```
Google Drive API has not been used in project 333804057110 before or it is disabled.
```

Điều này có nghĩa là bạn cần phải kích hoạt Google Drive API cho dự án của mình trong Google Cloud Console. Dưới đây là các bước để khắc phục lỗi này:

    1. **Truy cập Google Cloud Console**:
      - Mở trình duyệt và truy cập vào [Google Cloud Console](https://console.developers.google.com/).

    2. **Chọn Dự Án**:
      - Chọn dự án mà bạn đang sử dụng (dự án có ID là `333804057110`).

    3. **Kích Hoạt Google Drive API**:
      - Trong bảng điều khiển bên trái, chọn "API & Services" > "Library".
      - Tìm kiếm "Google Drive API" và nhấp vào nó.
      - Nhấn nút "Enable" để kích hoạt API.

    4. **Chờ một chút**:
      - Sau khi kích hoạt, có thể mất một vài phút để thay đổi có hiệu lực. Hãy đợi một chút trước khi thử lại.

    5. **Chạy lại script**:
      - Sau khi đã kích hoạt API, hãy chạy lại script `workflow.py` của bạn.

    Nếu bạn đã thực hiện các bước trên mà vẫn gặp lỗi, hãy kiểm tra lại xem bạn đã sử dụng đúng thông tin xác thực (credentials) và đã cấp quyền truy cập cho ứng dụng của bạn hay chưa.


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




====================

# 2. KẾT QUẢ KHI CHẠY


```bash
(.venv) (base) PS D:\OneDrive - Hanoi University of Science and Technology\GIT\grading-video-mentor\CheckPoints_aMinh\aHoang_Drive2Transcription> python workflow.py   
INFO:googleapiclient.discovery_cache:file_cache is only supported with oauth2client<4.0.0
Files in folder: 18

INFO:googleapiclient.discovery_cache:file_cache is only supported with oauth2client<4.0.0
Files in folder: 18

Files in folder: 18
Audio Files:
  0345100005 - 09_10 - B17 - mentor.m4a: https://drive.google.com/file/d/1qTR8xJLhA2eItsWgpyxzjnV1zNni6H3m/view
Downloading...
From: https://drive.google.com/uc?id=1qTR8xJLhA2eItsWgpyxzjnV1zNni6H3m
To: D:\OneDrive - Hanoi University of Science and Technology\GIT\grading-video-mentor\CheckPoints_aMinh\aHoang_Drive2Transcription\audio_data\18\Audio\0345100005 - 09_10 - B17 - mentor.m4a
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 16.1M/16.1M [00:01<00:00, 14.1MB/s] 
ERROR:root:Request error: 500 Server Error: INTERNAL SERVER ERROR for url: http://103.253.20.13:25029/role_assign
  0345100005 - 09_10 - B17 - HV.m4a: https://drive.google.com/file/d/19gu23pRUCu4y7UaL6XkAlsuRo8NQbQB9/view
Downloading...
From: https://drive.google.com/uc?id=19gu23pRUCu4y7UaL6XkAlsuRo8NQbQB9
To: D:\OneDrive - Hanoi University of Science and Technology\GIT\grading-video-mentor\CheckPoints_aMinh\aHoang_Drive2Transcription\audio_data\18\Audio\0345100005 - 09_10 - B17 - HV.m4a
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14.1M/14.1M [00:00<00:00, 17.6MB/s] 
INFO:root:Processing completed successfully.
Output saved to: audio_data\18\Text\0345100005 - 09_10 - B17 - HV.txt


  0973453282 - 09_10 - B6 - mentor.m4a: https://drive.google.com/file/d/1bZwlMr_LBlT9sJM1h0J5vWShUPjF2qPJ/view
Downloading...
From: https://drive.google.com/uc?id=1bZwlMr_LBlT9sJM1h0J5vWShUPjF2qPJ
To: D:\OneDrive - Hanoi University of Science and Technology\GIT\grading-video-mentor\CheckPoints_aMinh\aHoang_Drive2Transcription\audio_data\18\Audio\0973453282 - 09_10 - B6 - mentor.m4a
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 17.7M/17.7M [00:00<00:00, 26.5MB/s] 
ERROR:root:Request error: 500 Server Error: INTERNAL SERVER ERROR for url: http://103.253.20.13:25029/role_assign
  0973453282 - 09_10 - B6 - HV.m4a: https://drive.google.com/file/d/1wvzgTTQDtAJM3iQr2Gar-lrUXf_qp9rC/view
Downloading...
From: https://drive.google.com/uc?id=1wvzgTTQDtAJM3iQr2Gar-lrUXf_qp9rC
To: D:\OneDrive - Hanoi University of Science and Technology\GIT\grading-video-mentor\CheckPoints_aMinh\aHoang_Drive2Transcription\audio_data\18\Audio\0973453282 - 09_10 - B6 - HV.m4a
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 13.7M/13.7M [00:00<00:00, 22.5MB/s] 
INFO:root:Processing completed successfully.
Output saved to: audio_data\18\Text\0973453282 - 09_10 - B6 - HV.txt



Video Files:
  0345100005 - 09_10 - B17.mp4: https://drive.google.com/file/d/1MVfrM-a58A1PEsdZZ_2YxQ73xQ0MwsZE/view
Error: ID already exists.
  0973453282 - 09_10 - B6.mp4: https://drive.google.com/file/d/1WI4SYsEF0mlJh5sNQV8wfst7IFPBYVGV/view
Error: ID already exists.



ID: 1, FILE NAME VIDEO: , FILE NAME AUDIO: 0345100005 - 09_10 - B17 - mentor.m4a, URL VIDEO: , URL AUDIO: https://drive.google.com/uc?id=1qTR8xJLhA2eItsWgpyxzjnV1zNni6H3m, TRANSCRIPT:
ID: 2, FILE NAME VIDEO: , FILE NAME AUDIO: 0345100005 - 09_10 - B17 - HV.m4a, URL VIDEO: , URL AUDIO: https://drive.google.com/uc?id=19gu23pRUCu4y7UaL6XkAlsuRo8NQbQB9, TRANSCRIPT:
ID: 3, FILE NAME VIDEO: , FILE NAME AUDIO: 0973453282 - 09_10 - B6 - mentor.m4a, URL VIDEO: , URL AUDIO: https://drive.google.com/uc?id=1bZwlMr_LBlT9sJM1h0J5vWShUPjF2qPJ, TRANSCRIPT:
ID: 4, FILE NAME VIDEO: , FILE NAME AUDIO: 0973453282 - 09_10 - B6 - HV.m4a, URL VIDEO: , URL AUDIO: https://drive.google.com/uc?id=1wvzgTTQDtAJM3iQr2Gar-lrUXf_qp9rC, TRANSCRIPT:
(.venv) (base) PS D:\OneDrive - Hanoi University of Science and Technology\GIT\grading-video-mentor\CheckPoints_aMinh\aHoang_Drive2Transcription> 
```



=========
Dựa trên kết quả bạn đã cung cấp, đây là phân tích và giải thích về những gì đã xảy ra khi bạn chạy script `workflow.py`:

### 1. **Thông tin chung**
- **Số lượng tệp**: Script đã tìm thấy 18 tệp trong thư mục Google Drive mà bạn đã chỉ định.
- **Tải xuống tệp**: Các tệp âm thanh (mentor và HV) đã được tải xuống thành công từ Google Drive.

### 2. **Thông báo và Kết quả**
- **Thông báo INFO**: 
  - `INFO:googleapiclient.discovery_cache:file_cache is only supported with oauth2client<4.0.0`: Đây là một cảnh báo cho biết rằng tính năng cache không được hỗ trợ với phiên bản oauth2client lớn hơn 4.0.0. Điều này không ảnh hưởng đến chức năng chính của script.
  
- **Tải xuống tệp âm thanh**:
  - Các tệp âm thanh như `0345100005 - 09_10 - B17 - mentor.m4a` và `0973453282 - 09_10 - B6 - mentor.m4a` đã được tải xuống thành công với thông báo "100%". Điều này cho thấy quá trình tải xuống diễn ra suôn sẻ.

- **Lỗi 500 Server Error**:
  - `ERROR:root:Request error: 500 Server Error: INTERNAL SERVER ERROR for url: http://103.253.20.13:25029/role_assign`: Lỗi này cho biết rằng có vấn đề với server mà bạn đang gửi yêu cầu đến. Lỗi 500 thường chỉ ra rằng có lỗi bên trong server, không phải do yêu cầu của bạn. Bạn có thể cần kiểm tra server hoặc API mà bạn đang sử dụng để xử lý âm thanh.

- **Thông báo "Processing completed successfully"**:
  - Điều này cho thấy rằng quá trình xử lý tệp âm thanh (như chuyển đổi hoặc trích xuất thông tin) đã hoàn thành thành công cho một số tệp, và kết quả đã được lưu vào tệp văn bản.

- **Lỗi "ID already exists"**:
  - `Error: ID already exists.`: Điều này cho thấy rằng khi bạn cố gắng chèn dữ liệu vào cơ sở dữ liệu, một ID đã tồn tại. Điều này có thể xảy ra nếu bạn đang cố gắng chèn dữ liệu với ID đã được sử dụng trước đó. Bạn cần đảm bảo rằng ID là duy nhất cho mỗi bản ghi.

### 3. **Dữ liệu trong cơ sở dữ liệu**
- Các bản ghi đã được chèn vào cơ sở dữ liệu với các thông tin như:
  - **FILE NAME AUDIO**: Tên tệp âm thanh đã tải xuống.
  - **URL AUDIO**: Đường dẫn đến tệp âm thanh trên Google Drive.
  - **TRANSCRIPT**: Chưa có nội dung vì có thể chưa được xử lý thành công do lỗi server.

### Kết luận
- **Tải xuống và xử lý tệp âm thanh**: Bạn đã thành công trong việc tải xuống và xử lý một số tệp âm thanh.
- **Lỗi server**: Cần kiểm tra lại server mà bạn đang gửi yêu cầu để xử lý âm thanh.
- **ID trùng lặp**: Cần xem xét cách quản lý ID trong cơ sở dữ liệu để tránh lỗi trùng lặp.

Nếu bạn cần thêm thông tin hoặc hỗ trợ về một phần cụ thể nào đó, hãy cho tôi biết!




# 3. TRANSCRIPTIONS LƯU Ở ĐÂU


Trong mã Python bạn đã cung cấp, các bản sao chép (transcriptions) được lưu trữ trong thư mục `Text` bên trong thư mục `audio_data` mà bạn đã tạo. Cụ thể, quá trình lưu trữ diễn ra như sau:

1. **Tạo Thư Mục**: 
   - Khi bạn gọi hàm `google_drive_files(folder_id)`, mã sẽ tạo một thư mục cha có tên là `audio_data` và một thư mục con có tên là `Text` để lưu trữ các tệp văn bản chứa bản sao chép.

2. **Lưu Bản Sao Chép**:
   - Trong hàm `process_audio_outputs(output1, output2, output_filename)`, sau khi xử lý âm thanh và tạo ra bản sao chép, mã sẽ lưu bản sao chép vào tệp văn bản với tên được tạo từ tên tệp âm thanh gốc. Tệp văn bản này sẽ được lưu trong thư mục `Text`.

3. **Đường Dẫn Lưu Trữ**:
   - Đường dẫn lưu trữ cho các bản sao chép sẽ là:
     ```
     audio_data/<folder_name>/Text/<output_filename>
     ```
   - Trong đó `<folder_name>` là tên của thư mục Google Drive mà bạn đã tải xuống và `<output_filename>` là tên tệp văn bản chứa bản sao chép.

### Ví dụ
Nếu bạn có một tệp âm thanh có tên `0345100005 - 09_10 - B17 - HV.m4a`, thì bản sao chép sẽ được lưu trong tệp có tên `0345100005 - 09_10 - B17 - HV.txt` trong thư mục `Text`.

### Kiểm Tra
Để kiểm tra các bản sao chép đã được lưu, bạn có thể mở thư mục `audio_data` và tìm thư mục con `Text` để xem các tệp văn bản chứa bản sao chép.

Nếu bạn cần thêm thông tin hoặc có câu hỏi khác, hãy cho tôi biết!