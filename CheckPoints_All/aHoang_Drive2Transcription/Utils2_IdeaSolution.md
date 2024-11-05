# Bài Video Mentor:

## deploy 1.2. Refactor this code + ĐÓNG 1 API TỪ TRANSCRITPIONS => ra OUTPUT CUỐI DICTIONARY OF JSON. 

Về cách làm thì có 2 cách: 
- cách 1: Transcriptions => 1 Prompt = để mà đẩy ra các phần Detect (hiển thị lên UI), và chấm luôn. 
- cách 2: Từ 1 Prompt => chuyển ra: 3-4 Prompt Detect, Expand Transcriptions cho bước Chấm phía sau, 3-4 Prompt Chấm <đã có version trên AppsScript trước đó> ====================

2. Từ Drive => Database (STT, ID của video, Transcritpions của video, Day, có thể là thêm 2 cái link Audio). 
- Trích ID video, transcription của ID đấy. 
- Call vào API => trả ra 1 JSON Dictionary 
- Truyền JSON Dictionary đấy vào bản hiện tại => Hiển thị lên UI: Done ver1. 

=================

## deploy 1.3: Tuning Prompt, Tuning Drive => Database + Transcriptions. 