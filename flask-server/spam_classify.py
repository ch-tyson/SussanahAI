import cohere
from cohere.responses.classify import Example
from dotenv import load_dotenv
import os

load_dotenv()
co = cohere.Client(os.getenv('COHERE_API_KEY','process.env.API_KEY'))

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

def classify_spam(text):
    response = co.classify(
        model='large',
        inputs=[text],
        examples=examples,
    )
    print(response.classifications)
    return response.classifications


# classify_spam("Win a free prize!")
# sample output The confidence levels of the labels are: [{'spam':
# 0.9999999999999999, 'non-spam': 1.1102230246251565e-16}]

def get_spam_percentage(text):
    response = classify_spam(text)
    spam_score = response/labels['spam'].confidence
    non_spam_score = response.labels['non-spam'].confidence
    return [spam_score, non_spam_score]

def get_spam_result(text):
    spam_score = get_spam_percentage(text)[0]
    if (spam_score < 0.5):
        return " spam"
    else:
        return " not spam"