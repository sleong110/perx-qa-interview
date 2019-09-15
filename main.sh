#/bin/bash

export PATH=$PATH:$PWD/driver
source ./venv/bin/activate
pytest -v
