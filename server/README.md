# Managr - Backend

Welcome to the backend portion of the Managr! This section of the project focuses on providing APIs for user authentication.

## Project Overview

The backend handles the core functionalities of user authentication.

## Running the Backend Server

To run the backend server locally, follow these steps:

1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment:**

   ```bash
   source venv/bin/activate
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migration:**
   Run database migrations to ensure the latest schema is in place.

   ```bash
   alembic upgrade head
   ```

5. **Start the Backend Server:**
   Launch the server using Uvicorn with auto-reload for development.
   ```bash
   uvicorn main:app --reload
   ```

## Available Endpoints

### User Authentication

- `POST /login`: User login endpoint.
- `POST /register`: User sign up endpoint.

## Technical Stack

### Backend Framework

- **Framework:** Python FastAPI

### Database

- **Database:** PostgreSQL
- **ORM:** SQLAlchemy

### Running the Server

- **Server:** Uvicorn

### Dependencies

- All dependencies are listed in the `requirements.txt` file.

## Special Notes

- Ensure proper database configuration and connection before running the server.
- Adjust environment variables or configuration files as needed for different deployment environments.
