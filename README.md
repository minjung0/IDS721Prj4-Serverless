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
