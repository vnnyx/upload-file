
from celery import Celery
from dotenv import load_dotenv
import boto3, os

load_dotenv()

# Configure your AWS credentials
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')
BROKER_HOST = os.getenv('BROKER_HOST')

app = Celery('tasks', broker=BROKER_HOST)

@app.task
def upload_to_s3(file_content , key):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    s3.put_object(Body=file_content, Bucket=BUCKET_NAME, Key=key)