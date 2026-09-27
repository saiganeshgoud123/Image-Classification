from textblob import TextBlob
text = input("Enter a sentence: ")
analysis = TextBlob(text)
polarity = analysis.sentiment.polarity
if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"
print("\nText:", text)
print("Polarity:", polarity)
print("Sentiment:", sentiment)