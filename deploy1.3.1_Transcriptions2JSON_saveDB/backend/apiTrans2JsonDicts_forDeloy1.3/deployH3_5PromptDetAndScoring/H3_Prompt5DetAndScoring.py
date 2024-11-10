import json
from base_analyzer import BaseAnalyzer
from typing import Dict

class ConversationAnalyzer(BaseAnalyzer):
    UNIFIED_PROMPT = """
You are a professional grader, an expert in evaluating the quality of English teaching. Your task is to evaluate the Mentor's teaching performance in the areas of **Building Conversations**, **Teaching Idea Development**, and **Giving Feedback**.

**Instructions:**
1. **Evaluation Criteria:** Assess the Mentor's performance in three areas: **Building Conversations**, **Teaching Idea Development**, and **Giving Feedback**.
2. **Factors for Evaluation:** For each criterion, evaluate based on **three specific factors**, scoring each factor out of 10.
3. **Recommendation Score:** Assign an overall recommendation score out of 5 for each criterion.
4. **Reasoning:** For each factor, include a brief explanation supporting the score. Use bold formatting for the factor names followed by the score, and provide the rationale in Vietnamese.
5. Timestamp range should be 10 minutes
**Response JSON (without ```JSON)**

**Example:**

{
  "criteria": {
    "buildingConversations": {
      "timestamp": {
        "start": "00:07:01",
        "end": "00:07:14"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Dẫn dắt tốt: 8/10</b>\nNhận xét: Người hướng dẫn đã dẫn dắt cuộc trò chuyện hiệu quả, tạo bối cảnh phù hợp cho nội dung bài học.\n<b>Câu hỏi chất lượng: 7/10</b>\nNhận xét: Chất lượng câu hỏi tốt nhưng cần thêm các câu hỏi mở để khuyến khích người học suy nghĩ sâu hơn.\n<b>Kích thích tư duy: 7/10</b>\nNhận xét: Cuộc trò chuyện đã kích thích người học suy nghĩ, nhưng có thể cải thiện để tạo động lực thảo luận sôi nổi hơn."
      }
    },
    "teachingIdeaDevelopment": {
      "timestamp": {
        "start": "00:12:00",
        "end": "00:12:41"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Câu hỏi theo dõi: 8/10</b>\nNhận xét: Các câu hỏi theo dõi được sử dụng hiệu quả để phát triển ý tưởng của người học.\n<b>Sửa lỗi sai ý gốc: 7/10</b>\nNhận xét: Có thực hiện việc sửa lỗi ý tưởng, nhưng có thể xây dựng theo hướng mang tính đóng góp nhiều hơn.\n<b>Phát triển ý tưởng: 7/10</b>\nNhận xét: Phần phát triển ý tưởng đã khuyến khích người học mở rộng suy nghĩ, tuy nhiên có thể đẩy mạnh hơn."
      }
    },
    "givingFeedback": {
      "timestamp": {
        "start": "00:09:56",
        "end": "00:10:25"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Phù hợp và tạo động lực: 8/10</b>\nNhận xét: Phản hồi được đưa ra rất phù hợp và tạo động lực cho người học.\n<b>Đánh giá cụ thể: 7/10</b>\nNhận xét: Phản hồi cụ thể, nhưng có thể đi sâu hơn vào các chi tiết để giúp người học hiểu rõ hơn.\n<b>Kịp thời: 8/10</b>\nNhận xét: Phản hồi được đưa ra kịp thời, hỗ trợ người học điều chỉnh ngay trong quá trình học."
      }
    }
  }
}
"""

    @staticmethod
    def format_output(results: Dict) -> Dict:
        return {
            "criteria": {
                "buildingConversations": results.get("criteria", {}).get("buildingConversations", {}),
                "teachingIdeaDevelopment": results.get("criteria", {}).get("teachingIdeaDevelopment", {}),
                "givingFeedback": results.get("criteria", {}).get("givingFeedback", {})
            }
        }

def main():
    try:
        with open('transcription.txt', 'r', encoding='utf-8') as f:
            transcription = f.read()

        analyzer = ConversationAnalyzer(transcription)
        results = analyzer.analyze_transcription()
        formatted_results = analyzer.format_output(results)
        
        print("Analysis Results:")
        print("================")
        print(json.dumps(formatted_results, indent=2, ensure_ascii=False))
        
        analyzer.append_results_to_file(formatted_results)
        
    except FileNotFoundError:
        print(f"Error: Could not find transcription file")
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main() 