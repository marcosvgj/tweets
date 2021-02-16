

#!/bin/bash
TARGET_HOST=localhost

#########################################################################################
# Script Name: run.sh                                                                   #    
# Description: Register Twitter Developer credentials to tweets project                 #
#########################################################################################

# Setting twitter developer credentials
make configure

# Build virtual environment to this project
python3 -m venv tweets

# Load virtual environment to this project
source tweets/bin/activate

# Run Makefile that will run everything that you need to start the application.
make start

# Open UI's

x-www-browser $TARGET_HOST:8088 # Apache Superset
x-www-browser $TARGET_HOST:8080 # Spark UI
x-www-browser $TARGET_HOST:8090 # Airflow

# *Note: This pipeline was made to Unix environments.*