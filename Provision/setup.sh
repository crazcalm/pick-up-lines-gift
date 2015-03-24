#! /usr/bin/env bash

# update the machine
apt-get update -y

# installing/upgrading pip
apt-get install python-pip python-dev build-essential -y
pip install --upgrade pip

# personal installs
apt-get install fish -y
apt-get install sl -y
apt-get install tree -y
