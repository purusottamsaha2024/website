from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from app.core.settings import get_settings
from app.db.base import Base
from app.db.session import engine
from app.api.v1.router import router

settings = get_settings()

app = FastAPI(title=settings.APP_NAME)

# Include API router
app.include_router(router)

# Health endpoint
@app.get("/healthz")
def health():
    return {"status": "ok"}


# Serve static files
ui_path = Path("ui")
if ui_path.exists():
    # Mount static assets
    app.mount("/assets", StaticFiles(directory=ui_path / "assets"), name="assets")
    
    # Serve other static files (favicon, robots.txt, etc.)
    static_files = ["favicon.svg", "robots.txt", "vite.svg", "google507f1af12b8d5794.html"]
    for static_file in static_files:
        file_path = ui_path / static_file
        if file_path.exists():
            def make_handler(sf, fp):
                @app.get(f"/{sf}")
                def serve_static():
                    return FileResponse(fp)
            make_handler(static_file, file_path)
    
    # Serve index.html at root
    @app.get("/")
    def serve_index():
        index_path = ui_path / "index.html"
        if index_path.exists():
            return FileResponse(index_path)
        return {"message": "index.html not found"}


# Create tables on startup
@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

