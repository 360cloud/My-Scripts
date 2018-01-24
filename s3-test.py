#!/usr/bin/python

import boto3
import sys
import botocore

action = sys.argv[1]
bucket_name = sys.argv[2]

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

if action == 'create-bucket':
    print ("Creating Bucket")
    s3_client.create_bucket(Bucket=bucket_name)

elif action == 'delete-bucket':
   print ("Deleting Bucket ...")
   try:
	   bucket = s3_resource.Bucket(bucket_name)
	   for keys in bucket.objects.all():
	       keys.delete()
	   bucket.delete()
   except botocore.exceptions.ClientError as e:
           print e.response['Error']['Code']

elif action == 'upload-object':
   print ( " Uploading Object ")
   s3_resource.Object(bucket_name, 'Hello.txt').put(Body=open('/tmp/hello.txt', 'r'))

else:
   print ( "No Valid Action Provided ")


