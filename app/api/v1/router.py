from fastapi import APIRouter

from app.api.v1 import contact

router = APIRouter(prefix="/api/v1", tags=["v1"])

router.include_router(contact.router)

