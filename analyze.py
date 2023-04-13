import os
from google.cloud import language_v1
from google.cloud import storage

# Set up credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

# Set up GCS client
storage_client = storage.Client()

# Get the bucket and blob object
bucket = storage_client.bucket("ids721-prj4")
blob = bucket.get_blob("parasite.csv")

# Download the file's content as string
content = blob.download_as_text()

# Set up NLP client
client = language_v1.LanguageServiceClient()

# Set up document
document = language_v1.Document(content=content, type_=language_v1.Document.Type.PLAIN_TEXT)

# Analyze sentiment
response = client.analyze_sentiment(request={'document': document})

# Get sentiment score and magnitude
score = response.document_sentiment.score
magnitude = response.document_sentiment.magnitude

# Create a new blob to store the sentiment analysis results
new_blob = bucket.blob("results.txt")

# Write the sentiment score and magnitude to the new blob
new_blob.upload_from_string(f"Sentiment score: {score}\nSentiment magnitude: {magnitude}")
