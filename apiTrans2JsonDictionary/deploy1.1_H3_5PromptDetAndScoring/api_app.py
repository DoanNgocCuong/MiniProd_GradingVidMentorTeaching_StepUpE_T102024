from flask import Flask, request, jsonify
from typing import Dict
from H2_Prompt1DetAndScoring import WarmUpLeadInWrapUpAnalyzer
from H2_Prompt2DetAndScoring import VocabPronGrammarAnalyzer
from H2_Prompt3DetAndScoring import ThreePsScoring
from H2_Prompt4DetAndScoring import CorrectionAnalyzer
from H2_Prompt5DetAndScoring import ConversationAnalyzer

app = Flask(__name__)

def run_analysis(transcription: str) -> Dict:
    """Run all analyses and combine results."""
    
    analyzers = [
        WarmUpLeadInWrapUpAnalyzer(transcription),
        VocabPronGrammarAnalyzer(transcription),
        ThreePsScoring(transcription),
        CorrectionAnalyzer(transcription),
        ConversationAnalyzer(transcription)
    ]
    
    combined_results = {"criteria": {}}
    
    for analyzer in analyzers:
        try:
            results = analyzer.analyze_transcription()
            if results and "criteria" in results:
                combined_results["criteria"].update(results["criteria"])
        except Exception as e:
            print(f"Error in {analyzer.__class__.__name__}: {e}")
            continue
    
    return combined_results

@app.route('/analyze', methods=['POST'])
def analyze_transcription():
    try:
        # Get transcription from request body
        data = request.get_json()
        if not data or 'transcription' not in data:
            return jsonify({'error': 'No transcription provided'}), 400
            
        transcription = data['transcription']
        
        # Run analysis
        results = run_analysis(transcription)
        
        # Return results as JSON
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 