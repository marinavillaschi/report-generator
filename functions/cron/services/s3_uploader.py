import boto3
import json
from botocore.exceptions import ClientError
from decouple import config

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")


def upload_to_s3(bucket: str, key: str, data_to_upload) -> str:
    """ Uploads file to S3 bucket """

    s3 = boto3.resource(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

    try:
        response = s3.Bucket(bucket).Object(key).put(Body=json.dumps(data_to_upload))
        response_date = response["ResponseMetadata"]["HTTPHeaders"]["date"]
        print(f"file uploaded to S3 successfully on {response_date}!")

    except ClientError as e:
        print(e)
        return None

    return response_date
