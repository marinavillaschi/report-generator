# Report Generator Project

Generating reports on a schedule is a need for many industries. It's a repetitive task that can be time consuming and subject to human error.

This is the problem I'm gonna be solving with this project.

Automating report generation saves employees time and assures all reports are produced the same safe and tested way avoiding human error and guaranteeing data and report quality. This way the employees can focus their time and attention on other more important matters.

## Table of contents:

1. [Project Description](#description)
2. [Installation](#installation)
3. [Results](#results)
4. [Author](#author)
5. [Acknowledgements](#acknowledgements)

## Project Description <a name="description"></a>

This project has two main cores:

### 1. Cron based data fetcher lambda service

AWS Lambda service that runs on a schedule to fetch data from external API and upload it to an S3 data lake landing zone (raw).

### 2. Event based report generator lambda service

AWS Lambda service that runs based on the event of new data landing on the raw zone of the S3 data lake that will trigger a glue crawler so that our data is available to be queried from aws Athena.

### TODO:

- Create glue crawler on template to run everytime new data comes in S3 to create/update glue database

- Set up Athena for reading data from S3 using database created by crawler

- Create dashboard to feed from data using Athena


<!-- ### Passo a passo do serviço:

1. Acessa o banco de dados e busca as transações da tabela `balances` da conta informada (`account_id`) na data informada (`date`).

2. Com os `type_id`s das transações encontradas, busca os dados nas demais tabelas de interesse, de acordo com o tipo de transação.

3. Une todos esses dados e exporta o arquivo .csv final.



This project is composed of the following steps:

1. Data cleaning

    Preparation of the data provided.

2. Customer Segmentation Report

    Attribute analysis of established customers and the general population in order to create customers segments and be able to identify people of interest within the population.

3. Classification Model

    The previous analysis will be used to predict what individuals will respond to the marketing campaing so that the company can focus on them instead of the entire population. [PyCaret](https://pycaret.gitbook.io/docs/) library will be used for this task! -->


## Installation <a name="installation"></a>

--


<!-- There's no need to install any libraries to run this code on the Anaconda environment. The code should run with no issues using Python versions 3.*. -->


## Results <a name="results"></a>

--

<!-- Each notebook holds one step of the project. They were developed with markdown cells in such a way that it's easy to follow and the conclusions are drawn as it goes.

Also, a blog post of the finding is available [here](https://pandascouple.medium.com/how-to-power-customer-acquisition-marketing-campaings-8ea879f41eca). -->


## Author <a name="author"></a>

[Marina Villaschi](https://www.linkedin.com/in/marinavillaschi/?locale=en_US)

## Acknowledgements <a name="acknowledgements"></a>

[CoinGecko API](https://www.coingecko.com/pt/api) for the data provided.

