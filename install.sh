#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install pandas
pip install flask
bash launcher.sh