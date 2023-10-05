from textblob import TextBlob


class ChatBot:
    def get_user_input(self):
        user_input = input("User: ")
        return user_input

    def analyze_sentiment(self, user_input):
        analysis = TextBlob(user_input)

        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negative"

    def respond(self, sentiment):
        if sentiment == "Positive":
            return "User's sentiment seems to be Positive."
        elif sentiment == "Neutral":
            return "User's sentiment seems to be Neutral."
        else:
            return "User's sentiment seems to be Negative."

    def chat(self):
        while True:
            user_input = self.get_user_input()
            sentiment = self.analyze_sentiment(user_input)
            response = self.respond(sentiment)
            print("ChatBot: ", response)


if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()