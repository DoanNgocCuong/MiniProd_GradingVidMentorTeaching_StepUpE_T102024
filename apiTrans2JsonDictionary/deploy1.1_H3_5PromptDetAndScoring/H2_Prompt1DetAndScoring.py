import os
import yaml
import json
from typing import Dict, Optional, Any
from funct_getOpenAIResponse import get_openai_response
# from funct_extendTranscriptionSegment import extend_transcription_segment
from dotenv import load_dotenv

class WarmUpLeadInWrapUp:
    # Single unified prompt
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
    def __init__(self, transcription: str):
        """Initialize with transcription and load necessary configurations.

        Args:
            transcription (str): The transcription text to analyze
        """
        self.transcription = transcription
        
        # Load config for extension time
        with open('config.yml', 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.extension_time = self.config['CONFIG'].get('DEFAULT_EXTENSION_TIME', 60)
        
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')

    def analyze_transcription(self) -> Dict[str, Any]:
        """
        Analyze the transcription using the unified prompt.
        
        Returns:
            Dict[str, Any]: Analysis results in the specified format
        """
        try:
            response = get_openai_response(
                system_prompt=self.UNIFIED_PROMPT,
                user_input_prompt=self.transcription,
                api_key=self.api_key
            )
            
            # Parse response
            results = json.loads(response) if isinstance(response, str) else response
            
            return results
            
        except Exception as e:
            print(f"Error in analysis: {e}")
            return {}

def format_output(results: Dict) -> Dict:
    """Format the analysis results into the required structure."""
    return {
        "criteria": {
            "warmUp": results.get("criteria", {}).get("warmUp", {}),
            "leadIn": results.get("criteria", {}).get("leadIn", {}),
            "wrapUp": results.get("criteria", {}).get("wrapUp", {})
        }
    }

def append_results_to_file(new_results: Dict, filename: str = 'analysis_results.json'):
    """
    Append new results to existing JSON file or create new one if doesn't exist.
    
    Args:
        new_results (Dict): New analysis results to append
        filename (str): Name of the JSON file to append to
    """
    try:
        # Try to read existing file
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
                
            # Merge existing criteria with new criteria
            if 'criteria' in existing_data and 'criteria' in new_results:
                existing_data['criteria'].update(new_results['criteria'])
            else:
                existing_data.update(new_results)
                
        else:
            # If file doesn't exist, use new results as initial data
            existing_data = new_results
            
        # Write back the combined results
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"Error handling results file: {e}")
        
# Thêm SAMPLE_TRANSCRIPTION vào đầu file
SAMPLE_TRANSCRIPTION = """
[00:04:15] Mentee: Oh, good afternoon. 
[00:04:32] Mentor: Hello. 
[00:04:35] Mentor: Good afternoon. 
"""

def main():
    try:
        # Thay đổi phần load transcription
        try:
            with open('transcription.txt', 'r', encoding='utf-8') as f:
                transcription = f.read()
        except FileNotFoundError:
            print("Warning: Using sample transcription as transcription.txt not found")
            transcription = SAMPLE_TRANSCRIPTION

        # Analyze
        analyzer = WarmUpLeadInWrapUp(transcription)
        results = analyzer.analyze_transcription()
        formatted_results = format_output(results)
        
        # Print results
        print("Analysis Results:")
        print("================")
        print(json.dumps(formatted_results, indent=2, ensure_ascii=False))
        
        # Append results to file
        append_results_to_file(formatted_results)
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()