import json
import logging
import boto3 #this lib is to interact with AWS services from python apps, on this case for S3


#setting logging part

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    #log the raw event
    logger.info("Event: " + json.dumps(event))

    #process each record within the event
    for record in event['Records']:
        #extract bucket name and file key from the event
        bucket_name = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']

        #log each key and bucket name to cloudwatch
        logger.info(f"New file uploaded: {file_key} in bucket {bucket_name}")

    return {
        'statusCode': 200,
        'body': json.dumps('processed s3 upload event sucess!')
    }

