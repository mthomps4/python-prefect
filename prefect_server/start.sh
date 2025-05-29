#!/bin/bash

# Start Prefect server in the background
prefect server start --host 0.0.0.0 &

# Wait for the server to be ready
echo "Waiting for Prefect server to be ready..."
until curl -s http://localhost:4200/api/health > /dev/null; do
    sleep 1
done
echo "Prefect server is ready!"

# Deploy flows
echo "Setting up work pool and deploying flows..."
python setup.py

# Keep the container running
tail -f /dev/null