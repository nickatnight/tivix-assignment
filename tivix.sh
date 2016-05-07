#!/bin/bash

# Clone the repo and change to project root
git clone https://github.com/nickatnight/tivix-assignment.git && cd tivix-assignment

# Install all the neccessary python packages
pip install -r requirements.txt

# Run tests and deploy to local server
fab deploy_local
