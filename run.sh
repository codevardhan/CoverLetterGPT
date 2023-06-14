#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Error: Please provide two arguments."
    exit 1
fi

# Assign arguments to variables
arg1=$1
arg2=$2

# Activate Python environment
source env/bin/activate || {
    echo "Creating and activating Python environment..."
    python3 -m venv env
    source env/bin/activate
    python3 -m pip install -r requirements.txt
}

# Run the Python file with the arguments
python3 main.py "$arg1" "$arg2"

# Deactivate Python environment
deactivate

