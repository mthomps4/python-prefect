# Prefect Spike

## High Level Overview

                     ┌────────────┐
     API Request ──▶ │  FastAPI   │
                     └────┬───────┘
                          │
                          ▼
                 Trigger Prefect Flow
                          │
                          ▼
              ┌─────────────────────┐
              │   Prefect Orion     │◀── UI/CLI
              │   (API & UI server) │
              └────────┬────────────┘
                       │
                       ▼
             ┌─────────────────────┐
             │  Prefect Agent      │
             │ (runs your flows)   │
             └─────────────────────┘
                       │
                       ▼
                 Run ETL Tasks
                 ┌────────────┐
                 │   MSSQL    │◀─ Source/Target DB
                 └────────────┘

## Layout

your_project/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── routes/
│   │   └── etl.py       # API route to trigger flows
│   └── services/
│       └── prefect.py   # Prefect client integration
├── flows/
│   └── etl_flow.py      # Prefect flow & tasks
├── prefect/
│   ├── docker-compose.yml  # Prefect Orion server + agent
│   └── prefect.env         # Environment config
├── requirements.txt
└── README.md

## Installation

### Prerequisites

- [asdf](https://asdf-vm.com/) for Python version management
- [Docker](https://www.docker.com/) and Docker Compose for Prefect services

### Setup Python Environment

```bash
# Install Python plugin for asdf if not already installed
asdf plugin add python

# Install Python 3.11 (or your preferred version)
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
# Navigate to prefect directory
cd prefect

# Start Prefect services (Orion + Agent)
docker-compose up -d
```

## Deployment

- FastAPI API service to trigger or query flows Docker container or app server
- Prefect Orion UI/API to register and monitor flows Docker container
- Prefect Agent Executes your flows Docker container (can be in same docker-compose)
