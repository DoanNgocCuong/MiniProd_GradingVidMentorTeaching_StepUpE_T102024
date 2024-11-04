import os
import yaml
import json
from typing import Dict, Any
from funct_getOpenAIResponse import get_openai_response
from dotenv import load_dotenv

class BaseAnalyzer:
    def __init__(self, transcription: str):
        """Initialize base analyzer with common functionality."""
        self.transcription = transcription
        
        # Load config
        with open('config.yml', 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.extension_time = self.config['CONFIG'].get('DEFAULT_EXTENSION_TIME', 60)
        
        # Load environment variables
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')

    def analyze_transcription(self) -> Dict[str, Any]:
        """Base analysis method."""
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

    @staticmethod
    def append_results_to_file(new_results: Dict, filename: str = 'analysis_results.json'):
        """Append results to JSON file."""
        try:
            existing_data = {}
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                
                if 'criteria' in existing_data and 'criteria' in new_results:
                    existing_data['criteria'].update(new_results['criteria'])
                else:
                    existing_data.update(new_results)
            else:
                existing_data = new_results
                
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"Error handling results file: {e}") 