# ```cmd 
# curl -L -X POST "http://103.253.20.13:25010/api/text-to-speech" -H "Content-Type: application/json" -d "{\"text\": \"hello. Its me.Can you tell me?\",\"voice\": \"en-AU-WilliamNeural\",\"speed\": 1}" --output "1.mp3"
# ```

import requests
import json

def text_to_speech(input_text=None, file_path=None, voice="vi-VN-ManNeural", speed=1, output_file="1.mp3"):
    url = "http://103.253.20.13:25010/api/text-to-speech"
    headers = {"Content-Type": "application/json"}
    
    if input_text:
        text = input_text
    elif file_path:
        with open(file_path, "r") as file:
            text = file.read()
    else:
        raise ValueError("Either input_text or file_path must be provided.")
    
    data = {"text": text, "voice": voice, "speed": speed}
    response = requests.post(url, headers=headers, json=data)  # Changed from data=json.dumps(data) to json=data
    with open(output_file, "wb") as file:
        file.write(response.content)
    print(f"Audio file saved as {output_file}")

# Example usage
# text_to_speech("hello. Its me.Can you tell me?")
# text_to_speech(file_path="MucDichCuocSong.txt")

text_to_speech("""

GOSINGA ra đời là một tổ chức giáo dục phi lợi nhuận giới thiệu kiến thức do Đức Phật khám phá và truyền dạy không thông qua  con đường tôn giáo, với 2 khía cạnh khoa học và giáo dục nhằm thay đổi gốc rễ của con người từ tâm thấy và tâm biết để đạt được hạnh phúc liên tục và bền vững.
GOSINGA được lấy tên từ 1 bài kinh trong kinh Nikaya, nghĩa là Khu rừng sừng bò, nó mang tính ẩn dụ có nghĩa là nơi tập hợp những người trí giác ngộ được chân lý mà Đức Phật khám phá và giảng dạy.

Các khóa tu học của Gosinga tập trung vào truyền dạy phương pháp Thiền có tên gọi là KỸ NĂNG CHÚ TÂM LIÊN TỤC KHÔNG TẬP TRUNG.

Đa phần các trường phái thiền hiện nay đều thực hành thiền định theo kiểu chỉ có một loại chú tâm liên tục vào một đối tượng.
Đó là tập trung vào hơi thở, tập trung vào phồng xẹp, tập trung vào việc đếm hơi thở,...
Để đạt được sự chú tâm liên tục vào một đối tượng này cần phải nhất niệm, phải ức chế tâm. Vì thế sẽ phát sinh căng thẳng, mệt mỏi và phiền não làm cho việc thực hành khó có thể duy trì liên tục.
Và sự thực hành chú tâm liên tục này còn đòi hỏi phụ thuộc vào một không gian yên tĩnh, chủ yếu ở tư thế TĨNH là Tọa thiền để duy trì sự chú tâm liên tục vì thế không thực tiễn khi ứng dụng trong công việc và đời sống ở mọi lúc mọi nơi.
- Thứ 2, Nhiều người đang thực hành thiền nhưng không biết bắt đầu từ đâu, không có tiêu chuẩn đánh giá đang thực hành đúng hay sai và lộ trình rõ ràng từ pháp học pháp hành pháp thành. Dẫn tới người thực hành không có kết quả như mong đợi nên dễ chán nản, bỏ cuộc.

""", output_file="short1.mp3")