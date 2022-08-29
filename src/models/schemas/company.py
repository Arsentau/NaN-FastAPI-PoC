from typing import Optional

from pydantic import BaseModel, EmailStr


class CompanySchema(BaseModel):
    id: str
    company_name: str
    address: str
    address_line_2: Optional[str]
    city: str
    state_province: str
    country: str
    zip_code: Optional[str]
    time_zone: Optional[str]
    owner_name: Optional[str]
    owner_last_name: Optional[str]
    email: EmailStr
    phone_number: Optional[str]
    tax_id: str

    class Config:
        orm_mode = True


class NewCompanySchema(BaseModel):
    company_name: str
    address: str
    address_line_2: Optional[str]
    city: str
    state_province: str
    country: str
    zip_code: Optional[str]
    time_zone: Optional[str]
    owner_name: Optional[str]
    owner_last_name: Optional[str]
    email: EmailStr
    phone_number: Optional[str]
    tax_id: str


class PatchCompanySchema(BaseModel):
    company_name: str | None
    address: str | None
    address_line_2: str | None
    city: str | None
    state_province: str | None
    country: str | None
    zip_code: str | None
    time_zone: str | None
    owner_name: str | None
    owner_last_name: str | None
    email: EmailStr | None
    phone_number: str | None
    tax_id: str | None
