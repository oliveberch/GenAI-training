# Apache Airflow

Apache Airflow, initially developed by Airbnb, is a robust open-source platform designed for orchestrating complex workflows. 

It is used in the sequentialization and automation of tasks within a workflow.

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



### Q. default vs non default operators.

-  operators are building blocks that define individual tasks within a Directed Acyclic Graph (DAG). 

**Default Operators or Built-in Operators:**

built-in or default operators cover a wide range of common use cases. These are ready to use without additional installation or configuration.

Examples of Default Operators:

- BashOperator: Executes a Bash command.
- PythonOperator: Calls an arbitrary Python function.
- EmailOperator: Sends an email.
- HttpSensor: Waits for an HTTP endpoint to return a response.
- DummyOperator: Represents a no-op task (useful for testing and structure).

**Non-Default Operators Custom or Third-Party Operators:**

those that are not part of the built-in set and are typically developed by the user or the community.

Examples of Non-Default Operators:

- Custom operators developed by your team for domain-specific tasks.
- Third-party operators obtained from external sources or libraries.


### Terminologies for interview

- **DAG:** Represents the flow of data, ensuring a structured and organized workflow.

- **Worker Node:** Executes tasks defined in the workflow.

- **Task Run:** Initiation of a task or execution of an executor.

- **Scheduler:** Manages the scheduling of tasks based on predefined dependencies.


# Apache Aiflow App Overview

## DAG

### DAG status

- Active: Currently operational and processing tasks.
- Paused: User-controlled pause state, halting DAG execution.
- Failed: Halted due to errors encountered during execution.
- Restart: Initiating DAG execution from the beginning.
- Re-scheduling: Re-executing the DAG based on the defined schedule.

### DAG options

- Shutdown: Gracefully stopping and terminating the DAG.
- Trigger: Manually triggering the execution of the DAG.
- Delete DAG: Removing the DAG and associated metadata.

## Cluster Activity


## Dataset


## Security


## Browse


## Admin


### AirFlow Connections

| Conn Id                     | Conn Type             |
| --------------------------- | --------------------- |
| airflow_db                  | mysql                 |
| aws_default                 | aws                   |
| azure_batch_default         | azure_batch           |
| azure_cosmos_default        | azure_cosmos          |
| azure_data_explorer_default | azure_data_explorer   |
| azure_data_lake_default     | azure_data_lake       |
| azure_default               | azure                 |
| cassandra_default           | cassandra             |
| databricks_default          | databricks            |
| dingding_default            | http                  |
| drill_default               | drill                 |
| druid_broker_default        | druid                 |
| druid_ingest_default        | druid                 |
| elasticsearch_default       | elasticsearch         |
| emr_default                 | emr                   |
| facebook_default            | facebook_social       |
| fs_default                  | fs                    |
| ftp_default                 | ftp                   |
| google_cloud_default        | google_cloud_platform |
| hive_cli_default            | hive_cli              |
| hiveserver2_default         | hiveserver2           |
| http_default                | http                  |
| impala_default              | impala                |
| kafka_default               | kafka                 |
| kubernetes_default          | kubernetes            |
| kylin_default               | kylin                 |
| leveldb_default             | leveldb               |
| livy_default                | livy                  |
| local_mysql                 | mysql                 |
| metastore_default           | hive_metastore        |
| mongo_default               | mongo                 |
| mssql_default               | mssql                 |
| mysql_default               | mysql                 |
| opsgenie_default            | http                  |
| oracle_default              | oracle                |
| oss_default                 | oss                   |
| pig_cli_default             | pig_cli               |
| pinot_admin_default         | pinot                 |
| pinot_broker_default        | pinot                 |
| postgres_default            | postgres              |
| presto_default              | presto                |
| redis_default               | redis                 |
| redshift_default            | redshift              |
| salesforce_default          | salesforce            |
| segment_default             | segment               |
| sftp_default                | sftp                  |
| spark_default               | spark                 |
| sqlite_default              | sqlite                |
| sqoop_default               | sqoop                 |
| ssh_default                 | ssh                   |
| tableau_default             | tableau               |
| tabular_default             | tabular               |
| trino_default               | trino                 |
| vertica_default             | vertica               |
| wasb_default                | wasb                  |
| webhdfs_default             | hdfs                  |
| yandexcloud_default         | yandexcloud           |






## Reference:

https://airflow.apache.org/docs/apache-airflow/2.1.1/dag-run.html

https://airflow.apache.org/docs/apache-airflow/2.1.1/dag-run.html