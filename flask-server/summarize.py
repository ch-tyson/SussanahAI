import cohere
from dotenv import load_dotenv
import os

load_dotenv()
co = cohere.Client(os.getenv('COHERE_API_KEY','5kgNUypL3OHefbOcf5IrbYnkBFhcBYpFs8vGDSFG'))

def summary(text):
  response = co.summarize(
    text=text,
    model='large',
    length='medium',
    format='paragraph',
    extractiveness='medium'
)

summary = response.summary

