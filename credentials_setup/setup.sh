
#!/bin/bash

#########################################################################################
# Script Name: setup.sh                                                                 #    
# Description: Register Twitter Developer credentials to tweets project                 #
#########################################################################################

export TWEETS_CREDENTIAL_PATH=$(pwd)/twitter/resources/conf.yaml
python $(pwd)/credentials_setup/setup.py
