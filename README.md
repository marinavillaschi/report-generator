# Report Generator Project

Generating reports on a schedule is a need for many industries. It's a repetitive task that can be time consuming and subject to human error.

This is the problem I'm gonna be solving with this project.

Automating report generation saves employees time and assures all reports are produced the same safe and tested way avoiding human error and guaranteeing data and report quality. This way the employees can focus their time and attention on other more important matters.

## Project Description

This project has two main cores:

### 1. Cron based data fetcher lambda service

AWS Lambda service that runs on a schedule to fetch data from external API and upload it to an S3 bucket.

### 2. Event based report generator lambda service

AWS Lambda service that runs based on the event of new data landing on the S3 bucket that will trigger a glue crawler so that our data is available to be queried from aws Athena.


### In a nutshell:

We have data from the [CoinGecko API](https://www.coingecko.com/pt) comming in daily to an AWS S3 bucket in csv format.

<img src="https://github.com/marinavillaschi/report-generator/blob/main/assets/S3_bucket_snapshot.png" alt="S3_bucket_snapshot" width="650">

As soon as this data comes into the bucket, it triggers an AWS Glue Crawler.

<img src="https://github.com/marinavillaschi/report-generator/blob/main/assets/glue_crawler_snapshot.png" alt="glue_crawler_snapshot" width="650">

This crawler crawls the data and creates/updates a glue database and table.

<img src="https://github.com/marinavillaschi/report-generator/blob/main/assets/glue_database_snapshot.png" alt="glue_database_snapshot" width="650">

<img src="https://github.com/marinavillaschi/report-generator/blob/main/assets/glue_table_snapshot.png" alt="glue_table_snapshot" width="650">

Once this data is catalogued by AWS Glue it can be queried from AWS Athena.

<img src="https://github.com/marinavillaschi/report-generator/blob/main/assets/athena_snapshot.png" alt="athena_snapshot" width="650">


### TODO:

- ~~Create glue crawler on template to run everytime new data comes in S3 to create/update glue database~~  OK!

- ~~Set up Athena for reading data from S3 using database created by crawler~~  OK!

- Create dashboard to feed from data using Athena



## Author 

[Marina Villaschi](https://www.linkedin.com/in/marinavillaschi/?locale=en_US)

## Acknowledgements 
[CoinGecko API](https://www.coingecko.com/pt/api) for the data provided.

