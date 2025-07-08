# echov_boiler_plate

A minimal FastAPI boilerplate project.

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or later
- `pip` (Python package manager)

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/ShanidhTech/echov_boiler_plate.git
cd echov_boiler_plate
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```


## 🏃 Running the App

**To run the FastAPI app in development mode:**

```bash
uvicorn app.main:app --reload --env-file .env
```

**Start gRPC Server:**

```bash
python app/grpc/grpc_server.py
```

**Start Consumer Worker:**

```bash
python app/workers/event_worker.py
```

## 🚀 Database Migration

1. **Start by initializing Alembic:**

```bash
alembic init alembic
```   

2. **Create and run the database migrations:**

```bash
alembic revision --autogenerate -m "<migration message>"
alembic upgrade head
```

## 🧱 gRPC Compilation

**Compile proto files:**

```bash
python -m grpc_tools.protoc \
  -I app/grpc/proto \
  --python_out=app/grpc/generated \
  --grpc_python_out=app/grpc/generated \
  app/grpc/proto/auth.proto
```

## 📤 Kafka/RabbitMQ Integration

**Publish an event (example):**

```bash
from app.broker.producer import publish_event

publish_event("user.created", {"user_id": "123", "email": "demo@site.com"})
```

**Consume using:**

```bash
python app/workers/event_worker.py
```


## 📦 Docker

**Build Image**

```bash
docker build -t auth-service .
```

**Run Container**

```bash
docker run -p 8000:8000 auth-service
```

## 📚 API Documentation

**Visit:**

```bash
http://localhost:8000/docs
```

**or**

```bash
http://localhost:8000/redoc
```

**By default, this runs the app at: http://127.0.0.1:8000**

