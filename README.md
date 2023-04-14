## Individual Project #4: Serverless Data Engineering Pipeline

- Reproduce the architecture of the example serverless data engineering project or perform something similar using only serverless technologies
- Enhance the project by extending the functionality of the NLP analysis: adding entity extraction, key phrase extraction, or some other NLP feature or doing Applied Computer Vision. 

________

### 1. Get movie reviews from IMDB (scrape.py)

This code inside `scrape.py` allows you to retrieve reviews for a specific movie from IMDB and save them as a CSV file. To use the code, you need to modify the URL in the code with the movie number that can be found in the URL of the corresponding movie page on IMDB. For example, the URL for the movie Parasite is https://www.imdb.com/title/tt6751668/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_parasite, where tt6751668 is the movie number.

```
# URL of the movie reviews page
url = 'https://www.imdb.com/title/tt6751668/reviews?ref_=tt_urv'
```

### 2. Upload .csv file to Google Cloud Storage (upload.py)

1. Create a new Google Cloud Platform project.

<img width="540" alt="Screenshot 2023-04-13 at 9 37 37 PM" src="https://user-images.githubusercontent.com/90014065/231919206-6626194f-2b57-4f1f-bd31-70153c74dc14.png">

2. Create a new service account and download credentials as a JSON file containing a private key.

<img width="527" alt="Screenshot 2023-04-13 at 9 41 16 PM" src="https://user-images.githubusercontent.com/90014065/231919611-22a89eb6-a625-414b-9500-69b173bbf8c0.png">

3. Create a new Google Cloud Storage bucket and assign Storage/Object Admin permission to your account.

<img width="714" alt="Screenshot 2023-04-13 at 9 48 48 PM" src="https://user-images.githubusercontent.com/90014065/231920591-75d0b432-7e51-4534-9903-590e8c78ef6a.png">

4. To upload your review file to the bucket, run the `upload.py` and specify your credential path/name, bucket name, and file name as arguments.

```
# Set your GCP credentials
storage_client = storage.Client.from_service_account_json('service_account.json')

# Set the name of the bucket and the name of the file you want to upload
bucket_name = 'ids721-prj4'
file_name = 'parasite.csv'
```

<img width="470" alt="Screenshot 2023-04-13 at 9 55 24 PM" src="https://user-images.githubusercontent.com/90014065/231921597-25504327-b014-47ed-9303-58211d800c3c.png">

### 3. Perform sentiment analysis using Google Cloud Language API (analysis.py)

1. To perform sentiment analysis of your review file in the bucket, run the `analysis.py` and specify your credential path/name, bucket name, and file name as arguments.

```
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

# Get the bucket and blob object
bucket = storage_client.bucket("ids721-prj4")
blob = bucket.get_blob("parasite.csv")
```

2. When running the file, the output will be automatically uploaded to your designated bucket and saved as 'result.txt'.

<img width="474" alt="Screenshot 2023-04-13 at 10 04 26 PM" src="https://user-images.githubusercontent.com/90014065/231923186-8411ce5a-fa6d-467d-ba4a-9138b7869dc9.png">

### 4. Check the result

<img width="319" alt="Screenshot 2023-04-13 at 10 09 45 PM" src="https://user-images.githubusercontent.com/90014065/231923805-62e76c8e-de36-4a06-ac41-1f6b7682ee62.png">

- The sentiment score is a value between -1.0 (negative) and 1.0 (positive) that indicates the overall sentiment of the analyzed text. 
- The sentiment magnitude is a score that represents the overall emotional intensity of the text, regardless of the polarity (positive or negative). 
