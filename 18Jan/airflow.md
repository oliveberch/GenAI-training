# AirFlow

Airflow made by AirBNB.

Used to sequentialize sequence of tasks.

it also helps in automating workflow.

```
workflow here is, a series of tasks.
```

## characters of Airflow


Scalable


Dynamic
- since we use multiple pipelines
- here we can create dynamic pipeline i.e the approach is flexible and can be roll bock

Extensible
- extending and integrating with other tools and technologies

Elegant
- Jinja is a documentation approach like a web template
- beautifies code blocks

## features of AirFlow

- use of standard python
- use of interface
- well integrated with lot of apis
- easy to use- for any python user
- opensoource - not licensed

```
pipeline: small act of data filteration and operation
```

## usecases of AirFlow

- ETL pipeline

- MLOps: 

- Operational Analytics

## Airflow terminology

### core concepts

DAG: a graph which shows data flow 

DAG run: execution of DAG either manually or automated

Task: single unit of work that is executed, that are independent

Task instance: starting of a taks, specific point of trigger of task

### operators in airflow

there should be an operator attached to each task in a workflow

**primary operator categories:**

Action operator: functional in nature
Transer operator: movement in data from one point to another
Sensor operator: event happening as an entity

### Components of workflow

- webserver
- scheduler
- database
- executor

- triggerer
- worker

### Operators

[check deatils]

most frequently used Airflow operators:

PythonOperator: Executes a Python function.

BashOperator: Executes a bash script.

KubernetesPodOperator: Executes a task defined as a Docker image in a Kubernetes Pod.

SnowflakeOperator: Executes a query against a Snowflake database.

Q. default vs non default operators.

graph - dag
worker node - task execution
task run - initiation of task/executor
scheduler.