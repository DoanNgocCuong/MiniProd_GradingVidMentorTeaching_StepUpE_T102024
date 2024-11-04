import os
import requests
import json

try:
    # Load transcription from file với encoding UTF-8
    with open('transcription.txt', 'r', encoding='utf-8') as file:
        transcription = file.read()

    # Prepare the request data
    data = {
        'transcription': transcription
    }

    # Send POST request to the API
    response = requests.post('http://localhost:5000/analyze', json=data)

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        
        output_file = 'analysis_results_apiTest.json'
        
        # Kiểm tra xem file có tồn tại không
        if os.path.exists(output_file):
            print(f"File {output_file} đã tồn tại, sẽ ghi đè lên.")
        else:
            print(f"File {output_file} chưa tồn tại, sẽ tạo mới.")
        
        # Lưu kết quả vào file JSON với encoding UTF-8
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(results, outfile, indent=4, ensure_ascii=False)
            
        print(f"Đã lưu kết quả vào {output_file}")
    else:
        print(f"Lỗi: {response.status_code} - {response.text}")

except Exception as e:
    print(f"Có lỗi xảy ra: {str(e)}")