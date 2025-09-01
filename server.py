"""
This script runs a Flask web server for the Emotion Detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer_route():
    """
    Analyzes the user-provided text for emotions and returns a formatted string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    dominant_emotion = response.pop('dominant_emotion')

    # Build the string of emotion scores
    emotion_strings = [f"'{key}': {value}" for key, value in response.items()]
    emotions_part = ", ".join(emotion_strings)

    return (
        f"For the given statement, the system response is {emotions_part}. "
        f"The dominant emotion is **{dominant_emotion}**."
    )

@app.route("/")
def render_index_page():
    """Renders the main HTML page for the application."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)