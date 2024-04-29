# STEPS TO RUn:

1/ Run Models.py to setup the postgress tbale in postgres database
2/ After the database is set up, run the data_loader.py script to load the data:
    Use correct raw data path in the inpout


# Key Components
# Backend (FastAPI):
# main.py: Setup the FastAPI app, routes, and API endpoints.
# dependencies.py: Manage dependencies like database sessions.
# data_loader.py: Load data from CSV using Polars, validate it, and insert it into PostgreSQL.
# query.py: Handle database queries to fetch inventory data based on item_id.
# Frontend:
# Basic HTML pages enhanced with CSS for styling and JavaScript for asynchronous data fetching.
# Database (PostgreSQL):
# Use SQLAlchemy ORM for database interactions.
# Models representing the inventory data.
# Deployment:
# Dockerize the application using Docker and Docker Compose for easy deployment and scaling.


# Development Steps
# 1/ Set up the development environment - Define Python environment, dependencies, and necessary tooling.
# 2/ Database modeling and setup - Design the database schema and set up PostgreSQL.
# 3/ Backend API development - Develop FastAPI application to handle requests and serve data.
# 4/ Data loading pipeline - Create scripts to load and validate data using Polars.
# 5/ Frontend development - Build a simple interface to display data.
# 6/ Testing - Write unit tests and integration tests for both backend and frontend.
# 7/ Containerization - Dockerize the application for deployment.


# inventory_app/
# │
# ├── backend/               # All backend code
# │   ├── api/               # FastAPI application files
# │   │   ├── main.py        # FastAPI app setup and routes
# │   │   └── dependencies.py  # Database session management and other dependencies
# │   │
# │   ├── models/            # Database models
# │   │   └── models.py      # SQLAlchemy ORM models
# │   │
# │   ├── services/          # Business logic and data handling
# │   │   ├── data_loader.py # Handles loading and validating CSV data to database
# │   │   └── query.py       # Database queries
# │   │
# │   └── config/            # Configuration files
# │       └── settings.py    # Configuration settings
# │
# ├── frontend/              # Frontend web application
# │   ├── static/            # CSS, JavaScript files
# │   └── templates/         # HTML templates
# │
# ├── tests/                 # Test suite for the application
# │   ├── backend/
# │   └── frontend/
# │
# ├── scripts/               # Utility scripts, like setup or deployment scripts
# │   └── init_db.py         # Script for initializing the database
# │
# └── docker-compose.yml     # Docker configuration for local development




