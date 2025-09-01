import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers with the required model ID
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create the payload with the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }
    # Make a POST request to the API
    response = requests.post(url, json=payload, headers=headers)
    
    # 1. Convert response text to a dictionary
    formatted_response = json.loads(response.text)

    # 2. Extract the required set of emotions and their scores
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_scores['anger']
    disgust_score = emotion_scores['disgust']
    fear_score = emotion_scores['fear']
    joy_score = emotion_scores['joy']
    sadness_score = emotion_scores['sadness']

    # 3. Find the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # 4. Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
