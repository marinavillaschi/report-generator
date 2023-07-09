import boto3

def get_s3_object(bucket: str, key: str):
    """ Uploads file to S3 bucket """

    s3 = boto3.resource("s3")

    try:
        response = s3.Bucket(bucket).Object(key).get()["Body"].read().decode("utf-8")
        # response_date = response["ResponseMetadata"]["HTTPHeaders"]["date"]
        print(f"Got data from S3 successfully!")

    except Exception as e:
        print(e)
        print(f"Error getting object {key} from bucket {bucket}. Make sure they exist and your bucket is in the same region as this function.f")
        raise e

    return response
