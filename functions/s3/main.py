from services import crawler_invoker

def lambda_handler(event, context):
    print("New data in S3: starting glue crawler...")

    crawler_invoker.start_glue_crawler()
