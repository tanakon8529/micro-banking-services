#!/bin/bash

# Ensure the script is being executed with Bash
if [ -z "$BASH_VERSION" ]; then
  echo "This script must be run with Bash" >&2
  exit 1
fi

# Print the current shell being used (for debugging)
echo "Current shell: $SHELL"

# Create and activate virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements if not already installed
if [ ! -f "venv/requirements.installed" ]; then
  echo "Installing requirements..."
  pip install -r share/requirements.txt
  touch venv/requirements.installed
fi

# Ensure the tests directory exists
if [ ! -d "apis/tests" ]; then
  echo "Tests directory 'apis/tests' not found!"
  exit 1
fi

# Run standalone tests
echo "Running standalone tests..."
python3 -m unittest discover -s apis/tests -p '*_tests.py'

echo "All tests completed."
