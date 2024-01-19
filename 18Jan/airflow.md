# AirFlow

Airflow made by AirBNB.

Used to sequentialize sequence of tasks.

it also helps in automating workflow.

```
workflow here is, a series of tasks.
```

## characters of Airflow


Scalable
-
-

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



# Apache Airflow

Apache Airflow, initially developed by Airbnb, is a robust open-source platform designed for orchestrating complex workflows. It excels in the sequentialization and automation of tasks within a workflow. Here's a comprehensive guide to the key aspects of Apache Airflow.

## Purpose and Workflow

The primary purpose of Airflow is to manage workflows, which are essentially sequences of tasks. These tasks could range from simple data operations to complex ETL (Extract, Transform, Load) processes. 

## Key Characteristics of Airflow

### Scalable
- Airflow's scalability is a standout feature, accommodating various workloads and task complexities.

### Dynamic
- The platform supports multiple pipelines, allowing for the creation of dynamic and flexible workflows.

### Extensible
- Airflow can seamlessly integrate with various tools and technologies, making it highly extensible.

### Elegant
- Leveraging Jinja, a templating engine, Airflow enhances code readability and presentation, particularly in documentation and code blocks.

## Features

- **Python Integration:** Airflow utilizes standard Python, making it accessible to Python users and promoting code reuse.

- **User-Friendly Interface:** The platform provides a user-friendly interface for designing and monitoring workflows.

- **API Integration:** Well-integrated with numerous APIs, Airflow facilitates interactions with various services.

- **Open Source:** Airflow is open-source, providing users with flexibility and avoiding licensing constraints.

## Use Cases

- **ETL Pipeline:** Airflow is widely employed for building robust ETL pipelines, ensuring efficient data processing.

- **MLOps (Machine Learning Operations):** It plays a crucial role in orchestrating tasks related to machine learning model deployment and monitoring.

- **Operational Analytics:** Airflow supports the automation of analytical processes, enhancing operational efficiency.

## Airflow Terminology

### Core Concepts

- **DAG (Directed Acyclic Graph):** Represents the data flow in the form of a graph.

- **DAG Run:** Execution of a DAG, either triggered manually or through automation.

- **Task:** A single unit of work within a workflow, designed to be independent.

- **Task Instance:** The instantiation of a task at a specific point in time, triggered by a task.

### Operators in Airflow

Operators are essential components attached to each task in a workflow. Primary operator categories include:
- **Action Operator:** Functionally oriented operators.
- **Transfer Operator:** Facilitates data movement between different points.
- **Sensor Operator:** Monitors events as independent entities.

### Workflow Components

- **Webserver:** Provides a user interface for designing and monitoring workflows.

- **Scheduler:** Orchestrates task execution based on defined dependencies and schedules.

- **Database:** Stores metadata related to workflows, tasks, and their status.

- **Executor:** Executes the actual operations defined in tasks.

- **Triggerer:** Initiates workflow execution based on predefined triggers.

- **Worker:** Responsible for executing tasks on worker nodes.

### Most Frequently Used Operators

- **PythonOperator:** Executes a Python function within a task.

- **BashOperator:** Executes a bash script as part of a task.

- **KubernetesPodOperator:** Runs a task defined as a Docker image in a Kubernetes Pod.

- **SnowflakeOperator:** Executes queries against a Snowflake database.

### Understanding the Graph

- **DAG:** Represents the flow of data, ensuring a structured and organized workflow.

- **Worker Node:** Executes tasks defined in the workflow.

- **Task Run:** Initiation of a task or execution of an executor.

- **Scheduler:** Manages the scheduling of tasks based on predefined dependencies.

### Q. default vs non default operators.

### Terminologies for interview
- graph - dag
- worker node - task execution
- task run - initiation of task/executor
- scheduler - scheduling of tasks

