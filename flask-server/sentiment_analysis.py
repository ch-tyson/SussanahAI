import cohere
from cohere.responses.classify import Example
from dotenv import load_dotenv
import os

load_dotenv()

# Create a Cohere client using the COHERE_API_KEY from the environment variables
co = cohere.Client(os.getenv('COHERE_API_KEY','5kgNUypL3OHefbOcf5IrbYnkBFhcBYpFs8vGDSFG'))

# Define a list of example inputs and their corresponding labels for sentiment analysis
examples=[
    Example("I love this product", "Positive"),
    Example("This is the best day of my life", "Positive"),
    Example("I'm not happy with the service", "Negative"),
    Example("I hate waiting in line", "Negative"),
    Example("It's an average day", "Neutral"),
    Example("I don't feel strongly about this", "Neutral"),
    Example("I'm really looking forward to the weekend", "Positive"),
    Example("I can't wait to use this new app", "Positive"),
    Example("I'm so grateful for your help", "Positive"),
    Example("I'm feeling really down today", "Negative"),
    Example("I'm not happy with the product quality", "Negative"),
    Example("I'm disappointed with the service", "Negative"),
    Example("I regret buying this product", "Negative"),
    Example("I don't have any strong feelings about this", "Neutral"),
    Example("It's an average movie", "Neutral"),
    Example("The product does its job", "Neutral"),
    Example("It's not bad, but it's not great either", "Neutral")
]

# Function to classify the sentiment of a given text using Cohere's classify API
def classify_sentiment(text):
    response = co.classify(
        model='large',
        inputs=[text],
        examples=examples,
    )
    return response.classifications[0]

# Function to get the sentiment scores (confidence) for a given text
def get_sentiment_scores(text):
    response = classify_sentiment(text)
    print("First label: ", response.labels)
    positive_score = response.labels['Positive'].confidence
    negative_score = response.labels['Negative'].confidence
    neutral_score = response.labels['Neutral'].confidence
    return [positive_score, negative_score, neutral_score]

# Function to get the sentiment result (label) for a given text
def get_sentiment_result(text):
    response = classify_sentiment(text)
    return response.prediction
