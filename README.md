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
uvicorn backend.app.main:app --reload --env-file .env
```

**By default, this runs the app at: http://127.0.0.1:8000**

