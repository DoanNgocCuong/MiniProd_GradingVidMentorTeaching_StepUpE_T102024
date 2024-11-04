import os
import yaml
import json
from typing import Dict, Optional, Any
from funct_getOpenAIResponse import get_openai_response
from dotenv import load_dotenv

class WarmUpLeadInWrapUp:
    # New unified prompt for vocabulary, pronunciation, and grammar evaluation
    UNIFIED_PROMPT = """You are a professional grader, an expert in evaluating the quality of English teaching. Evaluate the Mentor's teaching performance for the Mentee in the following areas: Vocabulary, Pronunciation, and Grammar.

Instructions:
1. Detect timestamps for each section.
2. Provide a score and reason based on specific criteria.

**Evaluation Criteria**

1. Teaching Vocabulary:
   - Create a comfortable atmosphere and encourage participation (0-4 points): [score]  
     Reason: [reason in Vietnamese, explaining how the Mentor created a comfortable learning environment for vocabulary].
   - Explanation and contextualization of vocabulary (0-3 points): [score]  
     Reason: [reason in Vietnamese, emphasizing how the Mentor explained the meaning, provided examples, and context].
   - Feedback and correction on vocabulary usage (0-3 points): [score]  
     Reason: [reason in Vietnamese, analyzing the Mentor's feedback and correction approach].
   - Total Score: [Total out of 5].

2. Teaching Pronunciation:
   - Create a comfortable atmosphere and encourage participation (0-4 points): [score]  
     Reason: [reason in Vietnamese, explaining how the Mentor created a comfortable environment for pronunciation practice].
   - Guidance and adjustment of pronunciation (0-3 points): [score]  
     Reason: [reason in Vietnamese, highlighting the Mentor's guidance and correction on pronunciation].
   - Feedback and encouragement for pronunciation practice (0-3 points): [score]  
     Reason: [reason in Vietnamese, discussing how the Mentor provided feedback and motivated further practice].
   - Total Score: [Total out of 5].

3. Teaching Grammar:
   - Create a comfortable atmosphere and encourage participation (0-4 points): [score]  
     Reason: [reason in Vietnamese, explaining how the Mentor created a comfortable environment for grammar learning].
   - Explanation and provision of grammar examples (0-3 points): [score]  
     Reason: [reason in Vietnamese, emphasizing the Mentor's explanation and examples for grammar rules].
   - Feedback and correction on grammar (0-3 points): [score]  
     Reason: [reason in Vietnamese, analyzing the Mentor's feedback and corrections on grammar usage].
   - Total Score: [Total out of 5].

**Response JSON (without ```JSON)**

{
  "criteria": {
    "teachingVocab": {
      "timestamp": {
        "start": "00:18:02",
        "end": "00:18:12"
      },
      "recommendationScore": {
        "score": "3/5",
        "reason": "<b>Đưa ra định nghĩa: 6/10</b> The definition of 'enjoy the scenery' was provided, but more examples could enhance understanding.\\n<b>Luyện phát âm: 7/10</b> Pronunciation was addressed, but could be more emphasized.\\n<b>Form của từ: 5/10</b> The form of the word was not explicitly discussed.\\n<b>CCQ: 4/10</b> Concept Checking Questions were minimal.\\n<b>Reaffirm: 6/10</b> Reaffirmation was present but could be more structured."
      }
    },
    "pronunciation": {
      "timestamp": {
        "start": "00:14:26",
        "end": "00:15:05"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Perception: 8/10</b> The mentor effectively pointed out pronunciation issues.\\n<b>Pronunciation: 7/10</b> Pronunciation was practiced, but could be more focused.\\n<b>Predict: 6/10</b> Predictions about pronunciation were not clearly made.\\n<b>Performance: 7/10</b> Performance feedback was given, but could be more detailed.\\n<b>Practice: 7/10</b> Practice opportunities were present but could be expanded.\\n<b>Praise: 8/10</b> Positive reinforcement was provided effectively."
      }
    },
    "grammar": {
      "timestamp": {
        "start": "00:23:09",
        "end": "00:23:30"
      },
      "recommendationScore": {
        "score": "4/5",
        "reason": "<b>Show examples: 8/10</b> Examples of grammar usage were provided.\\n<b>Thuật ngữ: 7/10</b> Terminology was explained but could be clearer.\\n<b>Cách dùng: 8/10</b> Usage was demonstrated well.\\n<b>Cấu trúc: 7/10</b> Structure was mentioned but could be more detailed.\\n<b>CCQ: 6/10</b> CCQs were present but could be more varied.\\n<b>Recap: 8/10</b> A recap was provided effectively."
      }
    }
  }
}"""

    def __init__(self, transcription: str):
        self.transcription = transcription
        with open('config.yml', 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        self.extension_time = self.config['CONFIG'].get('DEFAULT_EXTENSION_TIME', 60)
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')

    def analyze_transcription(self) -> Dict[str, Any]:
        try:
            response = get_openai_response(
                system_prompt=self.UNIFIED_PROMPT,
                user_input_prompt=self.transcription,
                api_key=self.api_key
            )
            return json.loads(response) if isinstance(response, str) else response
        except Exception as e:
            print(f"Error in analysis: {e}")
            return {}

def format_output(results: Dict) -> Dict:
    """Format the analysis results into the required structure."""
    return {
        "criteria": {
            "teachingVocab": results.get("criteria", {}).get("teachingVocab", {}),
            "pronunciation": results.get("criteria", {}).get("pronunciation", {}),
            "grammar": results.get("criteria", {}).get("grammar", {})
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

def main():
    try:
        # Load transcription
        with open('transcription.txt', 'r', encoding='utf-8') as f:
            transcription = f.read()

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
        
    except FileNotFoundError:
        print(f"Error: Could not find transcription file")
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()