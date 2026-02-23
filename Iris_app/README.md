# Iris Classifier Application

This repository contains a FastAPI‑based web service for working with the classic
[Iris flower dataset](https://archive.ics.uci.edu/ml/datasets/iris). The API
supports multiple features designed to demonstrate CRUD operations, machine
learning predictions, and sentiment analysis.

## Key Features

* **Machine Learning Prediction** – a simple logistic regression model trained on
the Iris dataset provides species predictions.
* **CRUD Endpoints** – manage `Item` resources persisted in a PostgreSQL database
using SQLAlchemy models and Pydantic schemas.
* **Sentiment Analysis** – text sentiment is classified via a Hugging Face
Transformers pipeline.
* **Database Migrations** – Alembic is configured to apply schema changes
incrementally.
* **Docker Support** – the service and its database can be launched with
Docker‑Compose.

## Getting Started

### Prerequisites

* Python 3.10 or newer
* PostgreSQL (local or remote) or Docker (to spin up a Postgres container)
* `pip` for installing Python packages
* Optionally, `docker` and `docker-compose` if you choose containerization.

### Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iris-classifier-app.git
   cd iris-classifier-app/Iris_app
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the example environment file and configure it:
   ```bash
   cp .env.example .env
   # Edit .env to set DATABASE_URL and any other required variables
   ```
5. Initialize the database and run migrations:
   ```bash
   alembic upgrade head
   ```

### Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Navigate to `http://localhost:8000/docs` for the interactive API documentation.

### Docker

With Docker and Docker Compose installed:

```bash
docker compose up --build
```

Ensure `.env` contains the necessary variables before running.

### Testing

Execute the test suite with:

```bash
pytest
```

Unit and integration tests reside in the `tests/` directory.

### Project Structure

```
Iris_app/
├── app/                # Application code (routes, services, models, etc.)
├── alembic/            # Database migration scripts
├── tests/              # Test cases
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── README.md           # This file
```

### Environment Variables

Refer to `.env.example` for all expected settings. Key variables:

* `DATABASE_URL` – connection string for the PostgreSQL database.
* `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` – used by Docker
  Compose when spinning up the database container.

**Important:** Never commit `.env` or any file containing real secrets. The
`.gitignore` in the repository already excludes these files.

### Contributing

Contributions are welcome! Please open issues or pull requests on GitHub.

### License

This project is provided under the MIT License. See the `LICENSE` file for
details.
