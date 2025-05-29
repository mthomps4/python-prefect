# #!/bin/bash

# # Wait for Prefect server to be ready
# echo "Waiting for Prefect server to be ready..."
# until curl -s http://prefect-server:4200/api/health > /dev/null; do
#     sleep 5
# done
# echo "Prefect server is ready!"

# # Wait for work pool to be created
# echo "Waiting for work pool to be ready..."
# until prefect work-pool ls | grep -q "default"; do
#     sleep 5
# done
# echo "Work pool is ready!"

# # Set the work pool name explicitly
# export PREFECT_WORK_POOL_NAME=default

# # Start the worker with explicit work pool name
# exec prefect worker start --pool default