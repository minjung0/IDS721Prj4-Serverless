from google.cloud import storage

# Set your GCP credentials
storage_client = storage.Client.from_service_account_json('service_account.json')

# Set the name of the bucket and the name of the file you want to upload
bucket_name = 'ids721-prj4'
file_name = 'parasite.csv'

# Upload the file to the bucket
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(file_name)
blob.upload_from_filename(file_name)
