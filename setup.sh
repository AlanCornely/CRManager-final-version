#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv venv

echo "Installing requirements into venv..."
./venv/bin/pip install -r requirements.txt

echo "Starting Server..."
exec ./venv/bin/python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
