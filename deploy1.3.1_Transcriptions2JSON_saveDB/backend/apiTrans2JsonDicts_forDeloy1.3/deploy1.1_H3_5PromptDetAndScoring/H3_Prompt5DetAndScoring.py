import json
from base_analyzer import BaseAnalyzer
from typing import Dict

class ConversationAnalyzer(BaseAnalyzer):
    UNIFIED_PROMPT = """You are a professional grader, an expert in evaluating the quality of English teaching. From the teaching part from the Mentor teaching part to the Mentee
Instructions: Detect ... of Mentor teaching part. 
Response: JSON output (not include ```JSON)

{
  "criteria": {
    "buildingConversations": {
      "timestamp": {
        "start": "00:07:01",
        "end": "00:07:14"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Dẫn dắt tốt: 8/10</b> Nhận xét: The mentor led the conversation well.\\n<b>Câu hỏi chất lượng: 7/10</b> Quality of questions was good but could be more open-ended."
      }
    },
    "teachingIdeaDevelopment": {
      "timestamp": {
        "start": "00:12:00",
        "end": "00:12:41"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Follow-up questions: 8/10</b> Nhận xét: Follow-up questions were effectively used.\\n<b>Sửa lỗi sai ý gốc: 7/10</b> Idea corrections were present but could be more constructive."
      }
    },
    "givingFeedback": {
      "timestamp": {
        "start": "00:09:56",
        "end": "00:10:25"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Phù hợp và tạo động lực: 8/10</b> Nhận xét: Feedback was appropriate and motivating."
      }
    }
  }
}"""

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