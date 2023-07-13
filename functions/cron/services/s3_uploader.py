import boto3
import pandas as pd
from io import StringIO
from botocore.exceptions import ClientError


def upload_to_s3(bucket: str, key: str, df_to_upload: pd.DataFrame) -> str:
    """ Uploads file to S3 bucket """

    csv_buffer = StringIO()
    df_to_upload.to_csv(csv_buffer, index=False)
    
    s3 = boto3.resource("s3")

    try:
        response = s3.Bucket(bucket).Object(key).put(Body=csv_buffer.getvalue())
        response_date = response["ResponseMetadata"]["HTTPHeaders"]["date"]
        print(f"file uploaded to S3 successfully on {response_date}!")

    except ClientError as e:
        raise e
