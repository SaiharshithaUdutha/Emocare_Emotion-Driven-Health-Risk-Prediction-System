from textblob import TextBlob
from sklearn.preprocessing import LabelEncoder


def detect_emotion(text):

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity == 0:
        return "neutral"
    else:
        return "negative"