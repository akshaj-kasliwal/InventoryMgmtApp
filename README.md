
![image](https://github.com/akshaj-kasliwal/InventoryMgmtApp/assets/71369241/c995d992-d03f-4c1d-b1bb-a72e9c112112)


# STEPS TO RUN:

1/ Run Models.py to setup the postgres table in postgres database
2/ After the database is set up, run the data_loader.py script to load the data:
    Use the correct raw data path in the input


# Key Components
## Backend (FastAPI):
- **main.py**: Set up the FastAPI app, routes, and API endpoints.
- **dependencies.py**: Manage dependencies like database sessions.
- **data_loader.py**: Load data from CSV using Polars, validate it, and insert it into PostgreSQL.
- **query.py**: Handle database queries to fetch inventory data based on item_id.

## Frontend:
- Basic HTML pages enhanced with CSS for styling and JavaScript for asynchronous data fetching.

## Database (PostgreSQL):
- Use SQLAlchemy ORM for database interactions.
- Models representing the inventory data.

## Deployment:
- Dockerize the application using Docker and Docker Compose for easy deployment and scaling.

## Development Steps
1. **Set up the development environment**: Define Python environment, dependencies, and necessary tooling.
2. **Database modeling and setup**: Design the database schema and set up PostgreSQL.
3. **Backend API development**: Develop FastAPI application to handle requests and serve data.
4. **Data loading pipeline**: Create scripts to load and validate data using Polars.
5. **Frontend development**: Build a simple interface to display data.
6. **Testing**: Write unit tests and integration tests for both the backend and frontend.
7. **Containerization**: Dockerize the application for deployment.


## Structure

![image](https://github.com/akshaj-kasliwal/InventoryMgmtApp/assets/71369241/15f94d74-aaea-4a8f-97c7-439dc43ca9c7)

