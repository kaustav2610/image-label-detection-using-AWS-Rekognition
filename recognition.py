import csv
import boto3

with open('kaustav-kumar2610_accessKeys.csv','r') as input:
    next(input)
    reader=csv.reader(input)
    for line in reader:
        access_key_id=line[0]
        secret_access_key=line[1]

photo='rose.jpg'

client=boto3.client('rekognition',
                    aws_access_key_id=access_key_id,
                    aws_secret_access_key=secret_access_key,
                    region_name='us-east-1')

with open(photo, 'rb') as source_image :
    source_bytes = source_image.read()


response=client.detect_labels(Image={'S3Object': {
            'Bucket': 'kaustavbucket',
            'Name': photo}})

print(response)