import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Upload the file to S3
s3.upload_file('parasite.csv', 'my-bucket', 'parasite.csv')
