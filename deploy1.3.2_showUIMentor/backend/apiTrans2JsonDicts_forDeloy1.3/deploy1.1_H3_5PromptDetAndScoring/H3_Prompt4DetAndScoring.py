import json
from base_analyzer import BaseAnalyzer
from typing import Dict

class CorrectionAnalyzer(BaseAnalyzer):
    UNIFIED_PROMPT = """You are a professional grader, an expert in evaluating the quality of English teaching. From the teaching part from the Mentor teaching part to the Mentee
Instructions: Detect correctingMistakesRightWay, correctingMistakesRightTime of Mentor teaching part. 
Response: JSON output (not include ```JSON)

{
  "criteria": {
    "correctingMistakesRightWay": {
      "timestamp": {
        "start": "00:10:34",
        "end": "00:10:49"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Chỉ ra lỗi sai: 8/10</b> Nhận xét: Mistakes were pointed out effectively.\\n<b>Cách sửa đúng: 7/10</b> Correction methods were appropriate but could be more varied.\\n<b>Luyện tập sửa sai: 7/10</b> Practice for correcting mistakes was present but could be more structured."
      }
    },
    "correctingMistakesRightTime": {
      "timestamp": {
        "start": "00:10:40",
        "end": "00:10:54"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Hot correction: 8/10</b> Nhận xét: Immediate corrections were made effectively.\\n<b>Cold correction: 7/10</b> Delayed corrections were also present but could be more frequent."
      }
    }
  }
}"""

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