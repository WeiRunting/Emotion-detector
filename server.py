"""
Server module for Sentiment Analysis Flask application.
Provides web interface and API endpoints for sentiment analysis.
"""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)


@app.route("/")
def index():
    """首页路由，返回 HTML 界面"""
    return render_template('index.html')


@app.route("/emotionDetector", methods=['GET'])
def sent_analyzer():
    """
    情感分析路由，处理GET请求并返回分析结果
    
    Returns:
        str: 格式化的情感分析结果或错误信息
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if text is provided
    if not text_to_analyze:
        return "No text provided. Please enter some text to analyze.", 400

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response.get('label')
    score = response.get('score')

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again.", 400

    # Return a formatted string with the sentiment label and score
    sentiment = label.split('_')[1] if '_' in label else label
    return f"The given text has been identified as {sentiment} with a score of {score:.4f}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
