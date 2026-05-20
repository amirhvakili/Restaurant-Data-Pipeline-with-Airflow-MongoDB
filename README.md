# restaurant-etl-pipeline

## Project Overview

This project is an ETL (Extract, Transform, Load) data pipeline built using Apache Airflow, Python, Pandas, and MongoDB.

The pipeline processes restaurant data from a CSV file, performs data cleaning and transformation, loads the processed data into MongoDB for further analysis and reporting, and finally identifies high-density restaurant cities using the transformed dataset.

This project demonstrates practical skills in:

- Data Engineering
- ETL Pipeline Development
- Workflow Orchestration using Apache Airflow
- Data Cleaning and Transformation
- MongoDB Integration
- Python Automation

---

## Tech Stack

- Python
- Apache Airflow
- Pandas
- MongoDB
- NumPy
- CSV Data Processing

---

## Project Structure

```text
RESTAURANTPROJECT/
│
├── dags/
│   └── restaurant_pipeline_dag.py
│
├── data/
│   └── Restaurants.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── high_density_cities.py
│   └── load_mongodb.py
│
├── airflow.cfg
├── requirements.txt
├── README.md
└── .gitignore
