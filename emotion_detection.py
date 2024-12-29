import requests

# Function for emotion detection
def emotion_detector(text_to_analyze):
    # Endpoint URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers for the Watson API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON with the text to analyze
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    try:
        # Sending POST request
        response = requests.post(url, json=input_json, headers=headers)
        
        # Checking if the request was successful
        response.raise_for_status()
        
        # Debugging: Print the full response JSON
        print("Full Response JSON:", response.json())
        
        # Adjust this key to match the actual API response structure
        emotions = response.json().get('emotion', {}).get('document', {}).get('emotion', {})
        
        return emotions
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Testing the function (for local validation)
if __name__ == "__main__":
    test_text = "I love this new technology."
    print("Emotion Analysis Result:", emotion_detector(test_text))
