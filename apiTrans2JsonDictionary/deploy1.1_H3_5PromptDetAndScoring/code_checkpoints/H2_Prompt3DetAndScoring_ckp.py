import os
import yaml
import json
from typing import Dict, Optional, Any
from funct_getOpenAIResponse import get_openai_response
from dotenv import load_dotenv

class ThreePsScoring:
    UNIFIED_PROMPT = """You are a professional grader, an expert in evaluating the quality of English teaching. From the teaching part from the Mentor teaching part to the Mentee
Instructions: Detect Warm-Up, Lead-In, Wrap-Up of Mentor teaching part. 
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
        "reason": "<b>Present: 8/10</b>\\nNhận xét: Presentation of ideas was clear and structured.\\n<b>Practice: 7/10</b>\\nNhận xét: Practice opportunities were provided but could be more interactive.\\n<b>Produce: 7/10</b>\\nNhận xét: Production tasks were present but could be more challenging."
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
            "3Ps": results.get("criteria", {}).get("3Ps", {})
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
        analyzer = ThreePsScoring(transcription)
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