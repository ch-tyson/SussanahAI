
from flask import Flask, request, redirect, url_for, request, jsonify
from flask_cors import CORS
from spam_classify import get_spam_result, get_spam_percentage

# # Initialize the Cohere client with my API key just trying to figure out another way than just placing here (Mohith)
# co = cohere.Client('apiKey here')

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# API routes and endpoints to get data
@app.route('/')
def index():
	return {'message': 'Hello, my name is SussannahAI!'}

@app.route("/spam", methods=["POST"])
def spam():
    options = request.json["options"]
    text = request.json["name"]
    processed_text = text

    responseData = {}
    for option in options:
        if option == "spam":
            spam = get_spam_result(processed_text)
            spam_percent = get_spam_percentage(processed_text)
            responseData["spam"] = spam
            responseData["spamPercent"] = spam_percent

    response = jsonify(responsiveData)
    
    return response

if __name__ == '__main__':
	app.run(debug=True)

# # Define the route for sentiment analysis (Mohith)
# @app.route('/sentiment_analysis', methods=['POST'])
# def sentiment_analysis():
#     text = request.json['text']
#     response = co.classify(
#         inputs=[text],
#         # Define the examples for the learning model for sentiment examples (Mohith)
#         examples=[
#             Example("This is the best day of my life!", "Positive"),
#             Example("I'm really looking forward to the weekend", "Positive"),
#             Example("I can't wait to use this new app", "Positive"),
#             Example("I'm so grateful for your help", "Positive"),
#             Example("I'm feeling really down today", "Negative"),
#             Example("I'm not happy with the product quality", "Negative"),
#             Example("I'm disappointed with the service", "Negative"),
#             Example("I regret buying this product", "Negative"),
#             Example("I don't have any strong feelings about this", "Neutral"),
#             Example("It's an average movie", "Neutral"),
#             Example("The product does its job", "Neutral"),
#             Example("It's not bad, but it's not great either", "Neutral")
#         ]
#     )
#     # Return the classifications (Mohith)
#     return response.classifications

# # Define the route for text summarization (Mohith)
# @app.route('/text_summarization', methods=['POST'])
# def text_summarization():
#     text = request.json['text']
#     response = co.summarize(text=text)
#     # Return the summary (Mohith)
#     return response.summary