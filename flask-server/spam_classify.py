import cohere
from cohere.responses.classify import Example
from dotenv import load_dotenv
import os

load_dotenv()
co = cohere.Client(os.getenv('COHERE_API_KEY','5kgNUypL3OHefbOcf5IrbYnkBFhcBYpFs8vGDSFG'))

SPAM = "Spam"
NOT_SPAM = "NOT_SPAM"

examples=[
            Example("Get rich quick with this simple trick", SPAM),
            Example("You're the lucky winner of our lottery", SPAM),
            Example("Click here to claim your free vacation", SPAM),
            Example("Earn $5000 a day from home", SPAM),
            Example("Please review the attached invoice", NOT_SPAM),
            Example("Looking forward to our lunch meeting", NOT_SPAM),
            Example("Can you review my code?", NOT_SPAM),
            Example("Let's catch up over coffee", NOT_SPAM)
            
        ]

def classify_spam(text):
    response = co.classify(
        model='large',
        inputs=[text],
        examples=examples,
    )
    # print(response)
    return response.classifications[0]


# classify_spam("Win a free prize!")
# sample output The confidence levels of the labels are: [{'spam': 0.9999999999999999, 'non-spam': 1.1102230246251565e-16}]

def get_spam_percentage(text):
  response = classify_spam(text)
  print("First label: ", response.labels)
  spam_score = response.labels[SPAM].confidence
  non_spam_score = response.labels[NOT_SPAM].confidence
  return [spam_score, non_spam_score]

def get_spam_result(text):
  spam_score = get_spam_percentage(text)[0]
  if (spam_score > 0.5):
    return " spam"
  else:
    return " not spam"