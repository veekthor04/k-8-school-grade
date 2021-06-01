# coding-challenge
Coding Challenge

## project description
Your project must be done accordingly to microservice principle. Create 4 microservices: PostgreSQL Database, Redis, Celery Worker and REST API server(based on FastAPI). Your project must be runnable with docker-compose.

### project goals
1. https://catalog.data.gov/dataset/2015-2016-demographic-data-grades-k-8-school based on this dataset create database schema. To create database schema use SQLAlchemy.
2. https://catalog.data.gov/dataset/2015-2016-demographic-data-grades-k-8-school dataset must be loaded into database in celery task when system is bootstrapped. When docker containers are created for the first time, celery must run a boostrap task that will download dataset and insert it into database.
3. Expose REST API and allow to filter dataset, design some filters of Your choice, for example: category, race or sex. But feel free to propose others too. The REST API needs to return filtered dataset and link to chart.
4. When REST API will be used, a celery task must be scheduled which will create a chart with plotly. Chart must be saved on the disk, information about it saved ot database.
5. Expose an endpoint which will return chart created with plotly(IMAGE), endpoint has to use the id returned by REST API.
6. Create a Diagram/Blueprint representing Your system implementation.
7. Create unit tests.
8. Create integration test. You must test this scenario: Your REST API is used, celery task is executed, You must make sure that chart image is available. 

## project data
Use this dataset https://catalog.data.gov/dataset/2015-2016-demographic-data-grades-k-8-school. 

## technologies that must include
1. Python3.8 or higher
2. FastAPI
3. Docker and docker-compose
4. Plotly
5. Celery
6. Redis
7. PostgreSQL
8. SQLAlchemy
9. Pydantic
