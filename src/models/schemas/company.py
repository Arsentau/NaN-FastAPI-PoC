from pydantic import BaseModel, EmailStr


class CompanySchema(BaseModel):
    id: str
    company_name: str
    address: str
    city: str
    state_province: str
    country: str
    zip_code: str
    email: EmailStr
    phone_number: str
    tax_id: str

    class Config:
        orm_mode = True
