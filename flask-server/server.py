
from flask import Flask, request, redirect, url_for, request, jsonify
from flask_cors import CORS
from spam_classify import get_spam_result, get_spam_percentage
from sentiment_analysis import get_sentiment_scores, get_sentiment_result
from summarize import summarize

# # Initialize the Cohere client with my API key just trying to figure out another way than just placing here (Mohith)
# co = cohere.Client('apiKey here')

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# API routes and endpoints to get data
@app.route('/')
def index():
	return {'message': 'Hello, my name is SussannahAI!'}

@app.route("/classify", methods=["POST"])
def spam():
    options = request.json["options"]
    text = request.json["paragraph"]
    processed_text = text

    responseData = {}
    for option in options:
        if option == "spam":
            spam = get_spam_result(processed_text)
            spam_value = get_spam_percentage(processed_text)
            responseData["spam"] = spam
            responseData["spamValue"] = spam_value
        elif option == "summary":
            summary = summarize(process_text)
            responseData["summary"] = summary
        elif option == "sentiment":
            sentiment = get_sentiment_result(processed_text)
            sentiment_value = get_sentiment_percentage(processed_text)
            responseData["sentiment"] = sentiment
            responseData["sentimentValue"] = sentiment_value

    response = jsonify(responseData)
    
    return response

@app.route("/classify", methods=["POST"])
def summarize():
    options = request.json["options"]
    text = request.json["paragraph"]
    processed_text = text

    responseData = None
    for option in options:
        if option == "summarize":
            responseData = summary(processed_text)

    response = jsonify(responseData)
    
    return response

if __name__ == '__main__':
	app.run(debug=True)