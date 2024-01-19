from flask import Flask, request
import cohere
from cohere.responses.classify import Example

co = cohere.Client('5kgNUypL3OHefbOcf5IrbYnkBFhcBYpFs8vGDSFG')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/spam_detection', methods=['POST'])
def spam_detection():
    text = request.json['text']
    response = co.classify(
        inputs=[text],
        examples=[
            Example("Get rich quick with this simple trick", "Spam"),
            Example("You're the lucky winner of our lottery", "Spam"),
            Example("Click here to claim your free vacation", "Spam"),
            Example("Earn $5000 a day from home", "Spam"),
            Example("Please review the attached invoice", "Not Spam"),
            Example("Looking forward to our lunch meeting", "Not Spam"),
            Example("Can you review my code?", "Not Spam"),
            Example("Let's catch up over coffee", "Not Spam")
        ]
    )
    return response.classifications

@app.route('/sentiment_analysis', methods=['POST'])
def sentiment_analysis():
    text = request.json['text']
    response = co.classify(
        inputs=[text],
        examples=[
            Example("This is the best day of my life!", "Positive"),
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
    )
    return response.classifications

@app.route('/text_summarization', methods=['POST'])
def text_summarization():
    text = request.json['text']
    response = co.summarize(text=text)
    return response.summary