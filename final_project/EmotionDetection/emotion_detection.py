"""
Emotion detection module using IBM Watson NLP service.
"""
import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyze emotion in the given text using IBM Watson.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions.
        
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion.
              Returns None values for all keys if status code is 400.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers=headers)

    # Check if the response status code is 400 (bad request)
    if response.status_code == 400:
        # Return dictionary with all values set to None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # If status code is not 400, proceed with normal processing
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    dominant_emotion = max(emotions, key=emotions.get)
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }