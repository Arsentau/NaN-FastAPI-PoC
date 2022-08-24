from sqlalchemy import Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, String

from db.database import Base


class Company(Base):
    __tablename__ = 'company'
    id = Column(String, primary_key=True, index=True)
    company_name = Column(String)
    address = Column(String)
    address_line_2 = Column(String)
    city = Column(String)
    state_province = Column(String)
    country = Column(String)
    zip_code = Column(String)
    time_zone = Column(String)
    owner_name = Column(String)
    owner_last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    tax_id = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(String, primary_key=True, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    city = Column(String)
    state_province = Column(String)
    country = Column(String)
    zip_code = Column(String)
    time_zone = Column(String)
    personal_id = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    is_manager = Column(Boolean)
    company = Column(String, ForeignKey('company.id'))
    role = Column(String)
