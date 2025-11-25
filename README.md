# Company Website - FastAPI Backend

FastAPI + PostgreSQL backend with static HTML/CSS/JS frontend.

## Quick Start

```bash
# Setup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt

# Configure
cp .env.example .env
# Edit .env with your PostgreSQL credentials

# Run
uvicorn app.main:app --reload
```

**Endpoints:**
- Website: http://127.0.0.1:8000/
- Health: http://127.0.0.1:8000/healthz
- API Docs: http://127.0.0.1:8000/docs

## API

- `POST /api/v1/contact` - Create contact submission
- `GET /api/v1/contact/{id}` - Get contact by ID

## Testing

```bash
pytest
```

## Project Structure

```
app/
├── main.py           # FastAPI app
├── core/settings.py  # Config
├── api/v1/           # API routes
├── db/               # Database models & session
└── schemas/          # Pydantic schemas
ui/                   # Static files
tests/                # Tests
```

## Requirements

- Python 3.11+
- PostgreSQL
- `.env` file with `DATABASE_URL`

Tables are auto-created on startup. No migrations needed.
