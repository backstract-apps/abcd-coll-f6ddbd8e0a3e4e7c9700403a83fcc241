from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/persons/')
def get_all_persons( user_name: str , db: Session = Depends(get_db)):
    return service.get_all_persons(db , user_name)

@router.get('/persons/rollnumber')
def get_persons_by_rollnumber(rollnumber: int, full_name: str, db: Session = Depends(get_db)):
    return service.get_persons_by_rollnumber(db, rollnumber, full_name)

@router.post('/persons/')
def create_persons(rollnumber: str, fullname: str, age: str, profession: str, name: str, ducument_id: int, db: Session = Depends(get_db)):
    return service.create_persons(db, rollnumber, fullname, age, profession, name, ducument_id)

@router.put('/persons/rollnumber/')
def update_persons_by_rollnumber(rollnumber: str, fullname: str, age: str, profession: str, address: str, db: Session = Depends(get_db)):
    return service.update_persons_by_rollnumber(db, rollnumber, fullname, age, profession, address)

@router.delete('/persons/rollnumber')
def delete_persons_by_rollnumber(rollnumber: int, deletion_method: str, db: Session = Depends(get_db)):
    return service.delete_persons_by_rollnumber(db, rollnumber, deletion_method)

@router.get('/addresses/')
def get_all_addresses( rollnumber: int, address_filter: str , db: Session = Depends(get_db)):
    return service.get_all_addresses(db , rollnumber, address_filter)

@router.get('/addresses/id')
def get_addresses_by_id(id: int, address_type: str, db: Session = Depends(get_db)):
    return service.get_addresses_by_id(db, id, address_type)

@router.post('/addresses/')
def create_addresses(id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str, postal_address: str, db: Session = Depends(get_db)):
    return service.create_addresses(db, id, street, city, state, country, postal_code, created_at, updated_at, postal_address)

@router.put('/addresses/id/')
def update_addresses_by_id(id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str, credit_address: str, db: Session = Depends(get_db)):
    return service.update_addresses_by_id(db, id, street, city, state, country, postal_code, created_at, updated_at, credit_address)

@router.delete('/addresses/id')
def delete_addresses_by_id(id: int, address_permanent: str, db: Session = Depends(get_db)):
    return service.delete_addresses_by_id(db, id, address_permanent)

