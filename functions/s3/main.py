from decouple import config

from services import s3_downloader

LAKE_BUCKET_NAME = config("LAKE_BUCKET_NAME")


def lambda_handler(event, context):
    print("New data in S3: ready to process it!")

    key = event['Records'][0]['s3']['object']['key']

    data = s3_downloader.get_s3_object(LAKE_BUCKET_NAME, key)

    #TODO:
    # process data and generate report

    # send email

    print(type(data))
