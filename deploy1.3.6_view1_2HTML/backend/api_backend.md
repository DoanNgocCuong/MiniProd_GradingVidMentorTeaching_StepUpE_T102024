```bash
http://localhost:3000/get_video_data?url=https://drive.google.com/file/d/10qe6DkNX6up7-oG69HRG3B4j1A-WiI_o/view
```

```bash
curl --location 'http://127.0.0.1:3000/save_evaluation' \
--header 'Content-Type: application/json' \
--data '{
           "url_video": "https://example.com/video1",
           "criteria": "Clarity",
           "score": 4,
           "note": "Clear and concise presentation"
         }'

```