from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models.contact import ContactSubmission
from app.schemas.contact import ContactCreate, ContactRead

router = APIRouter(tags=["contact"])


@router.post("/contact", response_model=ContactRead, status_code=status.HTTP_201_CREATED)
def create_contact(contact_data: ContactCreate, db: Session = Depends(get_db)):
    db_contact = ContactSubmission(
        name=contact_data.name,
        email=contact_data.email,
        message=contact_data.message,
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.get("/contact/{id}", response_model=ContactRead)
def get_contact(id: int, db: Session = Depends(get_db)):
    contact = db.query(ContactSubmission).filter(ContactSubmission.id == id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

