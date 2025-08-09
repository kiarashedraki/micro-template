# FastAPI Blueprint - Microservice Template

A scalable FastAPI microservice template following clean architecture principles and best practices.

## 🚀 Features

- **Clean Architecture**: Organized folder structure with domain, ports, and adapters
- **Environment Configuration**: Pydantic Settings with `.env` support
- **Health Check**: Built-in health endpoint for monitoring
- **Docker Support**: Containerized deployment with Docker Compose
- **Testing**: Pre-configured pytest setup with example tests
- **Logging**: Structured logging configuration
- **Poetry**: Modern Python dependency management

## 📁 Project Structure

```
fastapi-blueprint/
├── pyproject.toml          # Poetry configuration
├── .env.example           # Environment variables template
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
├── app/
│   ├── core/              # Configuration, logging, constants
│   │   ├── config.py      # Pydantic Settings
│   │   └── logging.py     # Logging configuration
│   ├── api/               # API routes (versioned)
│   │   └── v1/
│   │       └── routes_health.py  # Health check endpoint
│   ├── domain/            # Business logic (future)
│   ├── ports/             # Interfaces (future)
│   ├── adapters/          # Implementations (future)
│   └── main.py            # FastAPI app factory
└── tests/
    └── test_health.py     # Health endpoint tests
```

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.9+
- Poetry (recommended) or pip

### Local Development

1. **Clone and setup**:

   ```bash
   git clone <your-repo>
   cd fastapi-blueprint
   cp .env.example .env
   ```

2. **Install dependencies**:

   ```bash
   poetry install
   ```

3. **Run the application**:

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

4. **Test the setup**:
   ```bash
   curl http://127.0.0.1:8000/api/v1/health
   poetry run pytest
   ```

### Docker Development

```bash
docker compose up --build
```

## 📋 API Endpoints

- **Health Check**: `GET /api/v1/health`
  - Returns service status and timestamp
- **API Documentation**: `GET /docs` (Swagger UI)
- **ReDoc Documentation**: `GET /redoc`

## 🧪 Testing

Run tests with:

```bash
poetry run pytest
```

Run with coverage:

```bash
poetry run pytest --cov=app
```

## 🔧 Configuration

Environment variables are managed through `.env` files and Pydantic Settings:

- `APP_NAME`: Application name
- `APP_ENV`: Environment (local, dev, prod)
- `API_V1_STR`: API version prefix
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)

## 🐳 Docker

The project includes production-ready Docker configuration:

- Multi-stage build for optimization
- Poetry for dependency management
- Health checks included
- Environment variable support

## 📝 Next Steps

This template is ready for:

- Database integration (add to `adapters/`)
- Message broker setup
- Authentication & authorization
- API rate limiting
- Monitoring and observability
- Additional business logic in `domain/`

## 🎯 FastAPI Blueprint Series

This is **Chapter 2** of the FastAPI Blueprint series:

1. Architecture & Planning
2. **Project Setup & Environment** (this chapter)
3. Core FastAPI Structure (coming next)
4. Database Integration
5. Authentication & Security
6. Testing & Quality Assurance

---

✅ **Chapter 2 Completion Checklist**

- [x] Poetry configuration with dependencies
- [x] `.env` and `.env.example` created
- [x] `Settings` class reads environment variables
- [x] App loads configs and logging from `.env`
- [x] Dockerfile + docker-compose.yml tested locally
- [x] `/health` endpoint reachable at `http://localhost:8000/api/v1/health`
- [x] Tests passing
- [x] Clean project structure ready for extension
