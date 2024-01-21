import cohere
from cohere.classify import Example

co = cohere.Client('process.env.API_KEY')

from cohere.classify import Example

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


classify_spam("Win a free prize!")
# sample output The confidence levels of the labels are: [{'spam': 0.9999999999999999, 'non-spam': 1.1102230246251565e-16}]