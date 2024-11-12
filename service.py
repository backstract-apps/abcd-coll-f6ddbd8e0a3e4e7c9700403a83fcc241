from sqlalchemy.orm import Session
from typing import List

import models, schemas

def get_all_persons(db: Session , user_name: str):
      persons_all = db.query(models.Persons).all()
      res = {
        'persons_all': persons_all,
        'lakshay': user_name,
      }
      return res

# auto generated route, get a record
def get_persons_by_rollnumber(db: Session, rollnumber: int, full_name: str):
      persons_one = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
      res = {
        'persons_one': persons_one,
        'user_name': full_name,
      }
      return res

def create_persons(db: Session, rollnumber: str, fullname: str, age: str, profession: str, name: str, ducument_id: int):
      record_to_be_added = {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}
      new_persons = models.Persons(**record_to_be_added)
      db.add(new_persons)
      db.commit()
      db.refresh(new_persons)
      persons_inserted_record = new_persons
      res = {
        'persons_inserted_record': persons_inserted_record,
        'doc_id': ducument_id,
      }
      return res

def update_persons_by_rollnumber(db: Session, rollnumber: str, fullname: str, age: str, profession: str, address: str):
      record_to_update = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
      for key, value in {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      persons_edited_record = record_to_update

      res = {
        'persons_edited_record': persons_edited_record,
        'person_address': address,
      }
      return res

def delete_persons_by_rollnumber(db: Session, rollnumber: int, deletion_method: str):
      persons_deleted = None
      record_to_delete = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          persons_deleted = record_to_delete
      res = {
        'persons_deleted': persons_deleted,
        'deletion_process': deletion_method,
      }
      return res

def get_all_addresses(db: Session , rollnumber: int, address_filter: str):
      addresses_all = db.query(models.Addresses).all()
      res = {
        'addresses_all': addresses_all,
        'filter_address': address_filter,
      }
      return res

# auto generated route, get a record
def get_addresses_by_id(db: Session, id: int, address_type: str):
      addresses_one = db.query(models.Addresses).filter(models.Addresses.id == id).first()
      res = {
        'addresses_one': addresses_one,
        'type': address_type,
      }
      return res

def create_addresses(db: Session, id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str, postal_address: str):
      record_to_be_added = {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}
      new_addresses = models.Addresses(**record_to_be_added)
      db.add(new_addresses)
      db.commit()
      db.refresh(new_addresses)
      addresses_inserted_record = new_addresses
      res = {
        'addresses_inserted_record': addresses_inserted_record,
        'postal_address_id': postal_address,
      }
      return res

def update_addresses_by_id(db: Session, id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str, credit_address: str):
      record_to_update = db.query(models.Addresses).filter(models.Addresses.id == id).first()
      for key, value in {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      addresses_edited_record = record_to_update

      res = {
        'addresses_edited_record': addresses_edited_record,
        'my_credit_address': credit_address,
      }
      return res

def delete_addresses_by_id(db: Session, id: int, address_permanent: str):
      addresses_deleted = None
      record_to_delete = db.query(models.Addresses).filter(models.Addresses.id == id).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          addresses_deleted = record_to_delete
      res = {
        'addresses_deleted': addresses_deleted,
        'permanent_address_id': address_permanent,
      }
      return res

