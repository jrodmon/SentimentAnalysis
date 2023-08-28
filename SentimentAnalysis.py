import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def analyze_sentiment(text):
    # Initialize the sentiment intensity analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Get sentiment scores
    sentiment_scores = sia.polarity_scores(text)
    
    # Determine the sentiment label
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment

# Get input from the user
input_text = input("Enter a text: ")

# Perform sentiment analysis
sentiment = analyze_sentiment(input_text)
print("Sentiment:", sentiment)