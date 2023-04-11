import requests
from bs4 import BeautifulSoup
import csv

# URL of the movie reviews page
url = 'https://www.imdb.com/title/tt6751668/reviews?ref_=tt_urv'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all review containers
review_containers = soup.find_all('div', class_='review-container')

# Create a list to store the reviews
reviews = []

# Loop through each review container
for container in review_containers:
    # Get the text of the review
    review_text = container.find('div', class_='text').get_text(strip=True)
    # Append the review text to the list of reviews
    reviews.append(review_text)

# Write the reviews to a CSV file
with open('parasite.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in reviews:
        writer.writerow([review])
