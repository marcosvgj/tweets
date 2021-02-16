

#!/bin/bash

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

# *Note: This pipeline was made to Unix environments.*