import boto3

from decouple import config


GLUE_CRAWLER_NAME = config("GLUE_CRAWLER_NAME")


def start_glue_crawler():
    try:
        glue = boto3.client("glue")
        glue.start_crawler(Name=GLUE_CRAWLER_NAME)

        print("crawler started successfully!")

    except Exception as e:
        raise Exception({
            "statusCode": 500,
            "body": "FAILED starting glue crawler",
            "error": e
        })
