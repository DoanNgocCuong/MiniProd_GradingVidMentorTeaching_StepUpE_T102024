import requests
import json

# Load transcription from file
with open('transcription.txt', 'r') as file:
    transcription = file.read()

# Prepare the request data
data = {
    'transcription': transcription
}

# Send POST request to the API
response = requests.post('http://localhost:5000/analyze', json=data)

# Check if the request was successful
if response.status_code == 200:
    results = response.json()
    # Save results to a JSON file
    with open('analysis_results_apiTest.json', 'w') as outfile:
        json.dump(results, outfile, indent=4)
    print("Results saved to analysis_results_apiTest.json")
else:
    print(f"Error: {response.status_code} - {response.text}")