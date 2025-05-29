# Prefect Spike

## High Level Overview (Future)

                     ┌────────────┐
     API Request ──▶ │  FastAPI   │
                     └────┬───────┘
                          │
                          ▼
                 Trigger Prefect Flow
                          │
                          ▼
              ┌─────────────────────┐
              │   Prefect Server    │◀── Developer Prefect Dashboard
              │ (Flows & UI server) │
              └────────┬────────────┘
                       │
                       ▼
                 Run ETL Tasks Run
                       │
                       ▼
                 ┌────────────┐
                 │  Postgres  │◀─ Source/Target DB
                 └────────────┘

## Layout

```sh
your_project/
├── api/
│   ├── main.py          # FastAPI entry point
│   ├── routes/
│   │   └── index.py     # API routes to trigger flows
│   └── utils
│   │   └── logger.py     # Shared Logger Config
│   └── Dockerfile.fastapi
├── prefect_server/
│   ├── Dockerfile.server # Prefect server configuration
│   └── prefect.env       # Environment config
├── docker-compose.yml    # All services (FastAPI, Prefect, Postgres)
└── README.md
```

## Installation

### Prerequisites

- [asdf](https://asdf-vm.com/) for Python version management
- [asdf-python](https://github.com/asdf-community/asdf-python) ASDF Python Plugin
- [Docker](https://www.docker.com/) and Docker Compose for all services

### Setup Python Environment

```bash
# Install Python plugin for asdf if not already installed
asdf plugin add python

# Install Python 3.12.2
asdf install python 3.12.2

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

### Install Dependencies

```bash
# Install project dependencies
pip install -r requirements.txt
```

### Start Prefect Services

```bash
# Start services (Orion + Agent)
docker-compose up --build
```

## ENVs

All Envs are currently in the [prefect.env](./prefect_server/prefect.env) file.
If you wish to use a local Database instead of Docker Postgres. Comment out the service in the docker-compose and change the DB URL.

## Start Scripts

When the prefect dockerfile starts, a script is ran to ensure the default worker pool and flows are served(deployed).
[prefect_server/setup.py](./prefect_server/setup.py)

## Swagger Docs

Both the Fast API and Prefect come with Swagger Docs
<http:localhost:8080/docs> (Fast API)
<http:localhost:4200/docs> (Prefect)

## Examples

### Healthcheck

```sh
curl --location --request GET 'http://localhost:8000/api/healthcheck'
```

### Logger Example

```sh
curl --location --request GET 'http://localhost:8000/api/test-log'
```

### Fast API Background Worker

This will start a "long running" process with Fast APIs background tasks

```sh
curl --location 'http://localhost:8000/api/background/process' \
--header 'Content-Type: application/json' \
--data '{ "name": "Matt" }'
```

### Fast API + Prefect Flow

Trigger a Prefect Flow with data

```sh
curl --location 'http://localhost:8000/api/hello-world' \
--header 'Content-Type: application/json' \
--data '{ "name": "Matt" }'
```

## Future Deployment

- FastAPI: API service to trigger or query flows
- Prefect: UI/API to monitor flows
