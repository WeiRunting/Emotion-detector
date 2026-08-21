# Sentiment Analysis Web Application
<img width="1898" height="642" alt="image" src="https://github.com/user-attachments/assets/3473aa39-8cbf-46f3-8109-e5c608727210" />
A Flask-based web application that performs sentiment analysis on user-provided text using IBM Watson's Natural Language Processing (NLP) service. The application provides both a user-friendly web interface and API endpoints for sentiment detection.

## Features

- **Web Interface**: User-friendly HTML interface for text input and sentiment analysis
- **Sentiment Analysis**: Utilizes IBM Watson's BERT-based sentiment analysis model
- **Real-time Results**: Instant feedback with sentiment classification and confidence scores
- **RESTful API**: GET endpoint for programmatic access
- **Error Handling**: Robust error handling for invalid inputs and API failures

## Technology Stack

- **Backend**: Python 3.11, Flask
- **NLP Service**: IBM Watson Sentiment Analysis API
- **Frontend**: HTML, Bootstrap, JavaScript
- **Testing**: unittest

## Project Structure
```bash
practice_project/
├── SentimentAnalysis/
│ ├── init.py
│ └── sentiment_analysis.py # Core sentiment analysis logic
├── static/
│ └── mywebscript.js # Frontend JavaScript
├── templates/
│ └── index.html # Web interface
├── server.py # Flask application server
├── test_sentiment_analysis.py # Unit tests
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/WeiRunting/Emotion-detector.git
cd Emotion-detector/practice_project
```

2. Install required dependencies:
```bash
pip install flask requests
```

3. Start the Flask server:
```bash
python server.py
```

