"""
Flask server for emotion detection application.
This module provides a web interface for emotion analysis using IBM Watson.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Handle emotion detection requests.
    Returns emotion analysis results or error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    # Get emotion analysis results
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response as requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
