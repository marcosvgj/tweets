
#!/bin/bash

#########################################################################################
# Script Name: setup.sh                                                                 #    
# Description: Register Twitter Developer credentials to tweets project                 #
#########################################################################################

export TWEETS_CREDENTIAL_PATH=$(pwd)/twitter/resources/credentials_test.yaml
python $(pwd)/credentials_setup/setup.py
