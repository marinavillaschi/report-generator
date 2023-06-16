import boto3
import json
from botocore.exceptions import ClientError


def upload_to_s3(bucket: str, key: str, data_to_upload) -> str:
    """ Uploads file to S3 bucket """

    s3 = boto3.resource("s3")

    try:
        response = s3.Bucket(bucket).Object(key).put(Body=json.dumps(data_to_upload))
        response_date = response["ResponseMetadata"]["HTTPHeaders"]["date"]
        print(f"file uploaded to S3 successfully on {response_date}!")

    except ClientError as e:
        print(e)
        raise e

    return response_date
