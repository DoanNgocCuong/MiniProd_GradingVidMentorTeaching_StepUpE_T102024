import json
from base_analyzer import BaseAnalyzer
from typing import Dict



class WarmUpLeadInWrapUpAnalyzer(BaseAnalyzer):
    UNIFIED_PROMPT = """You are a professional grader, an expert in evaluating the quality of English teaching. Your task is to evaluate the Mentor's teaching performance for the Mentee in three areas: Warm-Up, Lead-In, and Wrap-Up.

Instructions:
1. Detect timestamps for each section.
2. Provide a score and reason based on specific criteria.

**Evaluation Criteria**

1. Warm-Up:
   - Create a comfortable atmosphere and encourage participation (0-4 points): [score]  
     Reason: [reason in Vietnamese].
   - Positive feedback and encouragement (0-3 points): [score]  
     Reason: [reason in Vietnamese].
   - Suitable pace and natural transition (0-3 points): [score]  
     Reason: [reason in Vietnamese].
   - Total Score: [Total out of 10].

2. Lead-In:
   - Clear introduction and connection to lesson content (0-4 points): [score]  
     Reason: [reason in Vietnamese].
   - Motivation and interest (0-3 points): [score]  
     Reason: [reason in Vietnamese].
   - Connect with Mentee’s prior knowledge (0-3 points): [score]  
     Reason: [reason in Vietnamese].
   - Total Score: [Total out of 10].

3. Wrap-Up:
   - Comfortable atmosphere and participation (0-4 points): [score]  
     Reason: [reason in Vietnamese].
   - Positive feedback and encouragement (0-3 points): [score]  
     Reason: [reason in Vietnamese].
   - Suitable pace and natural transition (0-3 points): [score]  
     Reason: [reason in Vietnamese].
   - Total Score: [Total out of 10].

**Response JSON (without ```JSON)**

Example: 

{
  "criteria": {
    "warmUp": {
      "timestamp": {
        "start": "00:00:00",
        "end": "00:01:12"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Mục đích: 8/10</b>\nNhận xét ngắn: The warm-up effectively connected to previous lessons by referencing the Vietnam Food Contest, which helped set the context for the conversation.\n<b>Tạo hứng khởi: 7/10</b>\nNhận xét ngắn: The warm-up was engaging, but could have included more interactive elements to boost excitement."
      }
    },
    "leadIn": {
      "timestamp": {
        "start": "00:01:12",
        "end": "00:02:07"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Dẫn dắt vào bài: 8/10</b> Nhận xét ngắn: The transition to the lesson was smooth, as the mentor clearly outlined the topic of Vietnamese cuisine."
      }
    },

    "wrapUp": {
      "timestamp": {
        "start": "00:29:00",
        "end": "00:29:09"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Wrap-up: 8/10</b> Nhận xét: The wrap-up effectively summarized the lesson and set expectations for the next session."
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