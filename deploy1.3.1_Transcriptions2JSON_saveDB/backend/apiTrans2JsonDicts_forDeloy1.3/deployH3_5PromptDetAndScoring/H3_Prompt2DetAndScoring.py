import json
from base_analyzer import BaseAnalyzer
from typing import Dict  # Thêm import này nếu bạn sử dụng Dict trong format_output




class VocabPronGrammarAnalyzer(BaseAnalyzer):
    UNIFIED_PROMPT = """
You are a professional grader, an expert in evaluating the quality of English teaching. Your task is to evaluate the Mentor's teaching performance for the Mentee in three areas: Vocabulary, Pronunciation, and Grammar.

**Instructions:**
1. **Evaluation Criteria:** Assess the Mentor's performance in each of the three areas: Vocabulary, Pronunciation, and Grammar.
2. **Factors for Evaluation:** For each criterion, evaluate based on **three specific factors**. Each factor should be scored out of 10.
3. **Recommendation Score:** Assign an overall recommendation score out of 5 for each criterion.
4. **Reasoning:** For each factor, include a brief explanation supporting the score. Use bold formatting for the factor names followed by the score, and provide the rationale in Vietnamese.
5. Timestamp range should be 10 minutes
**Response JSON (without ```JSON)**

**Example:**

{
  "criteria": {
    "teachingVocab": {
      "timestamp": {
        "start": "00:18:02",
        "end": "00:18:12"
      },
      "recommendationScore": {
        "score": "3/5",
        "reason": "<b>Đưa ra định nghĩa: 6/10</b> Định nghĩa của 'enjoy the scenery' đã được cung cấp, nhưng có thể thêm nhiều ví dụ để tăng cường sự hiểu biết.\n<b>Luyện phát âm: 7/10</b> Phát âm đã được chú trọng, nhưng có thể được nhấn mạnh hơn.\n<b>Hình thức từ: 5/10</b> Hình thức của từ chưa được thảo luận rõ ràng."
      }
    },
    "pronunciation": {
      "timestamp": {
        "start": "00:14:26",
        "end": "00:15:05"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Nhận thức: 8/10</b> Người hướng dẫn đã chỉ ra hiệu quả các vấn đề phát âm.\n<b>Thực hành phát âm: 7/10</b> Phát âm đã được luyện tập, nhưng có thể tập trung hơn.\n<b>Khen ngợi: 8/10</b> Sự khích lệ tích cực đã được cung cấp hiệu quả."
      }
    },
    "grammar": {
      "timestamp": {
        "start": "00:23:09",
        "end": "00:23:30"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Ví dụ minh họa: 8/10</b> Các ví dụ về sử dụng ngữ pháp đã được cung cấp.\n<b>Giải thích thuật ngữ: 7/10</b> Thuật ngữ đã được giải thích nhưng có thể rõ ràng hơn.\n<b>Cách sử dụng: 8/10</b> Cách sử dụng đã được trình bày tốt."
      }
    }
  }
}

    """  # Your existing prompt

    @staticmethod
    def format_output(results: Dict) -> Dict:
        return {
            "criteria": {
                "teachingVocab": results.get("criteria", {}).get("teachingVocab", {}),
                "pronunciation": results.get("criteria", {}).get("pronunciation", {}),
                "grammar": results.get("criteria", {}).get("grammar", {})
            }
        }

def main():
    try:
        with open('transcription.txt', 'r', encoding='utf-8') as f:
            transcription = f.read()

        analyzer = VocabPronGrammarAnalyzer(transcription)
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