import boto3

from decouple import config


GLUE_CRAWLER_NAME = config("GLUE_CRAWLER_NAME")


def start_glue_crawler():
    try:
        glue = boto3.client("glue")

        crawler_state = glue.get_crawler(Name=GLUE_CRAWLER_NAME)['Crawler']['State']
        print(f"{GLUE_CRAWLER_NAME} state is {crawler_state}")

        if crawler_state == "READY":
            glue.start_crawler(Name=GLUE_CRAWLER_NAME)
            print(f"{GLUE_CRAWLER_NAME} started successfully!")

    except Exception as e:
        raise Exception({
            "statusCode": 500,
            "body": "FAILED starting glue crawler",
            "error": e
        })
