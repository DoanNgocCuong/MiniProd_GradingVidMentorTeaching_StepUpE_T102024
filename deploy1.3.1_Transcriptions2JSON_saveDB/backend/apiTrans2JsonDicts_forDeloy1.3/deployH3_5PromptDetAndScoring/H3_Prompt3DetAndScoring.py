import json
from base_analyzer import BaseAnalyzer
from typing import Dict  # Thêm import này nếu bạn sử dụng Dict trong format_output



class ThreePsScoring(BaseAnalyzer):
    UNIFIED_PROMPT = """

You are a professional grader, an expert in evaluating the quality of English teaching.
Your task is to evaluate the Mentor's teaching performance based on the 3Ps method: Presentation, Practice, and Production.

Instructions:
- Highlight a timestamp range within 10 minutes that best represents the mentor's teaching effectiveness.

**Response JSON (without ```JSON)**

**Example:**

{
  "criteria": {
    "3Ps": {
      "timestamp": {
        "start": "00:9:25",
        "end": "00:10:43"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Present: 8/10</b>\nNhận xét: Phần trình bày của người hướng dẫn rõ ràng và có cấu trúc, giúp người học dễ dàng nắm bắt ý chính.\n<b>Practice: 7/10</b>\nNhận xét: Cơ hội thực hành được cung cấp nhưng có thể bổ sung thêm tính tương tác để nâng cao trải nghiệm học tập.\n<b>Produce: 7/10</b>\nNhận xét: Các bài tập sản xuất có mặt nhưng có thể tăng mức độ thách thức để khuyến khích người học sáng tạo và áp dụng kiến thức."
      }
    }
  }
}

    """  # Your existing prompt

    @staticmethod
    def format_output(results: Dict) -> Dict:
        return {
            "criteria": {
                "3Ps": results.get("criteria", {}).get("3Ps", {})
            }
        }

def main():
    try:
        with open('transcription.txt', 'r', encoding='utf-8') as f:
            transcription = f.read()

        analyzer = ThreePsScoring(transcription)
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