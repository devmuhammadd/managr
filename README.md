# Managr

Welcome to the Managr!

### Directory Structure

```
├── client/     # Frontend codebase in Next
└── server/      # Backend codebase in Python
```

## Functionalities

### Authentication

Users are required to log in to access and manage tickets, ensuring secure access to the system.

### User and Rights Management

Different access rights are assigned based on user roles, maintaining control over system permissions.

## Technical Stack & Requirements

### Backend

- **Framework:** Python FastAPI
- **Database:** PostgreSQL
- **Logging/Error Handling:** Comprehensive logging system and sophisticated error handling
- **Database Queries:** Use of Prepared Statements and parameterized queries
- **ORM:** Utilizing SQLAlchemy for efficient database abstraction
- **Transaction Management:** Ensures data integrity through robust transaction handling
- **Validation:** Input data validation for accuracy
- **Sanitization:** Cleaning inputs to prevent XSS and other security threats

### Frontend

- **Framework:** NextJs (JavaScript)

## Special Notes

### ORM

Efficient and maintainable database communication is ensured through the use of SQLAlchemy.
