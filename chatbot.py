from textblob import TextBlob


def get_sentiment(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return "Positive"
    elif blob.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"


def chatbot():
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        print("Chatbot: This seems a", get_sentiment(user_input), "statement.")


chatbot()
