import json
from base_analyzer import BaseAnalyzer
from typing import Dict

class CorrectionAnalyzer(BaseAnalyzer):
    UNIFIED_PROMPT = """
You are a professional grader, an expert in evaluating the quality of English teaching. Your task is to evaluate the Mentor's teaching performance specifically in areas of **Correcting Mistakes the Right Way** and **Correcting Mistakes at the Right Time**.

**Instructions:**
1. **Evaluation Criteria:** Assess the Mentor's performance in two areas: **Correcting Mistakes the Right Way** and **Correcting Mistakes at the Right Time**.
2. **Factors for Evaluation:** For each criterion, evaluate based on **three specific factors**, scoring each factor out of 10.
3. **Recommendation Score:** Assign an overall recommendation score out of 5 for each criterion.
4. **Reasoning:** For each factor, include a brief explanation supporting the score. Use bold formatting for the factor names followed by the score, and provide the rationale in Vietnamese.
5. Timestamp range should be 10 minutes
**Response JSON (without ```JSON)**

**Example:**

{
  "criteria": {
    "correctingMistakesRightWay": {
      "timestamp": {
        "start": "00:10:34",
        "end": "00:10:49"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Chỉ ra lỗi sai: 8/10</b>\nNhận xét: Người hướng dẫn đã chỉ ra lỗi sai một cách hiệu quả, giúp người học nhận biết và ghi nhớ lỗi.\n<b>Cách sửa đúng: 7/10</b>\nNhận xét: Phương pháp sửa lỗi phù hợp, nhưng có thể đa dạng hóa để tăng cường hiệu quả.\n<b>Luyện tập sửa sai: 7/10</b>\nNhận xét: Có thực hành sửa lỗi nhưng cần cấu trúc rõ ràng hơn để hỗ trợ việc ghi nhớ lâu dài."
      }
    },
    "correctingMistakesRightTime": {
      "timestamp": {
        "start": "00:10:40",
        "end": "00:10:54"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Sửa lỗi ngay lập tức (Hot correction): 8/10</b>\nNhận xét: Việc sửa lỗi ngay lập tức đã được thực hiện hiệu quả, giúp người học nhận biết lỗi trong thời gian thực.\n<b>Sửa lỗi chậm trễ (Cold correction): 7/10</b>\nNhận xét: Có thực hiện sửa lỗi chậm trễ nhưng cần tăng tần suất để người học có thêm cơ hội suy ngẫm.\n<b>Tần suất sửa lỗi: 7/10</b>\nNhận xét: Việc sửa lỗi đã được thực hiện thường xuyên, nhưng có thể tăng cường để nâng cao trải nghiệm học tập."
      }
    }
  }
}
"""

    @staticmethod
    def format_output(results: Dict) -> Dict:
        return {
            "criteria": {
                "correctingMistakesRightWay": results.get("criteria", {}).get("correctingMistakesRightWay", {}),
                "correctingMistakesRightTime": results.get("criteria", {}).get("correctingMistakesRightTime", {})
            }
        }

def main():
    try:
        with open('transcription.txt', 'r', encoding='utf-8') as f:
            transcription = f.read()

        analyzer = CorrectionAnalyzer(transcription)
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