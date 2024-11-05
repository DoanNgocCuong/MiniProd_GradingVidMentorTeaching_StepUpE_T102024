import json
from base_analyzer import BaseAnalyzer
from typing import Dict  # Thêm import này nếu bạn sử dụng Dict trong format_output



class ThreePsScoring(BaseAnalyzer):
    UNIFIED_PROMPT = """

You are a professional grader, an expert in evaluating the quality of English teaching. From the teaching part from the Mentor teaching part to the Mentee
Instructions: Detect 3Ps (Presentation, Practice, Production) of Mentor teaching part. 
Response: JSON output (not include ```JSON)

{
  "criteria": {
    "3Ps": {
      "timestamp": {
        "start": "00:10:25",
        "end": "00:10:43"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Present: 8/10</b>\nNhận xét: Presentation of ideas was clear and structured.\n<b>Practice: 7/10</b>\nNhận xét: Practice opportunities were provided but could be more interactive.\n<b>Produce: 7/10</b>\nNhận xét: Production tasks were present but could be more challenging."
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