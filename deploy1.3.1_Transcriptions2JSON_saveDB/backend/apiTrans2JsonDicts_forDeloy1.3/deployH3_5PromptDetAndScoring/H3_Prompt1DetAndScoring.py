import json
from base_analyzer import BaseAnalyzer
from typing import Dict



class WarmUpLeadInWrapUpAnalyzer(BaseAnalyzer):
    UNIFIED_PROMPT = """
 You are a professional grader, an expert in evaluating the quality of English teaching. Your task is to evaluate the Mentor's teaching performance for the Mentee in three areas: Warm-Up, Lead-In, and Wrap-Up.

**Instructions:**
1. **Evaluation Criteria:** Assess the Mentor's performance in each of the three areas: Warm-Up, Lead-In, and Wrap-Up.
2. **Factors for Evaluation:** For each criterion, evaluate based on **three specific factors**. Each factor should be scored out of 10.
3. **Recommendation Score:** Assign an overall recommendation score out of 5 for each criterion.
4. **Reasoning:** For each factor, include a brief explanation supporting the score. Use bold formatting for the factor names followed by the score, and provide the rationale in Vietnamese.
5. Timestamp range should be 10 minutes
**Response JSON (without ```JSON)**

**Example:**

{
  "criteria": {
    "warmUp": {
      "timestamp": {
        "start": "00:00:00",
        "end": "00:01:12"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Mục đích: 8/10</b>\nNhận xét ngắn: Phần khởi động đã kết nối hiệu quả với các bài học trước bằng cách tham chiếu đến Cuộc thi Ẩm thực Việt Nam, giúp thiết lập bối cảnh cho cuộc trò chuyện.\n<b>Tạo hứng khởi: 7/10</b>\nNhận xét ngắn: Phần khởi động thu hút sự chú ý, nhưng có thể bao gồm thêm các yếu tố tương tác để tăng cường sự phấn khích.\n<b>Mức độ liên quan: 9/10</b>\nNhận xét ngắn: Các hoạt động rất phù hợp với mục tiêu bài học, đảm bảo sự chuyển tiếp mượt mà vào nội dung chính."
      }
    },
    "leadIn": {
      "timestamp": {
        "start": "00:01:12",
        "end": "00:02:07"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Độ rõ ràng: 8/10</b>\nNhận xét ngắn: Sự chuyển tiếp vào bài học diễn ra suôn sẻ, khi người hướng dẫn đã rõ ràng trình bày chủ đề về ẩm thực Việt Nam.\n<b>Cấu trúc: 7/10</b>\nNhận xét ngắn: Phần dẫn nhập được cấu trúc tốt, nhưng có thể bổ sung thêm ví dụ để minh họa các điểm chính.\n<b>Tạo sự hứng thú: 9/10</b>\nNhận xét ngắn: Người hướng dẫn đã hiệu quả trong việc thu hút sự tham gia của người học thông qua các câu hỏi và gợi ý liên quan."
      }
    },
    "wrapUp": {
      "timestamp": {
        "start": "00:29:00",
        "end": "00:29:09"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Tóm tắt: 8/10</b>\nNhận xét: Phần kết thúc đã tóm tắt hiệu quả bài học và đặt ra các kỳ vọng cho buổi học tiếp theo.\n<b>Kết thúc: 7/10</b>\nNhận xét: Đã cung cấp một kết thúc tốt, nhưng có thể bao gồm một bài kiểm tra ngắn về các điểm chính.\n<b>Giữ sự chú ý: 9/10</b>\nNhận xét: Đã giữ cho người học tham gia cho đến cuối buổi học một cách thành công."
      }
    }
  }
}
"""

    @staticmethod
    def format_output(results: Dict) -> Dict:
        return {
            "criteria": {
                "warmUp": results.get("criteria", {}).get("warmUp", {}),
                "leadIn": results.get("criteria", {}).get("leadIn", {}),
                "wrapUp": results.get("criteria", {}).get("wrapUp", {})
            }
        }

def main():
    try:
        with open('transcription.txt', 'r', encoding='utf-8') as f:
            transcription = f.read()
    except FileNotFoundError:
        print("Warning: Using sample transcription as transcription.txt not found")
        transcription = SAMPLE_TRANSCRIPTION

    analyzer = WarmUpLeadInWrapUpAnalyzer(transcription)
    results = analyzer.analyze_transcription()
    formatted_results = analyzer.format_output(results)
    
    print("Analysis Results:")
    print("================")
    print(json.dumps(formatted_results, indent=2, ensure_ascii=False))
    
    analyzer.append_results_to_file(formatted_results)

if __name__ == "__main__":
    main()