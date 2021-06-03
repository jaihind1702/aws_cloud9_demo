import boto3

client = boto3.client('rekognition')

response = client.detect_labels(
    Image = {
        'S3Object': {
            'Bucket' :'cloud9n',
            'Name' : 'Marvel.jpeg'
        },
    },
)

print(response)