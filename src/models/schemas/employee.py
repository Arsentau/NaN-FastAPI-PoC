from pydantic import BaseModel, EmailStr, HttpUrl


class EmployeeSchema(BaseModel):
    first_name: str
    last_name: str
    address: str
    city: str
    state_province: str
    country: str
    zip_code: str
    time_zone: str
    personal_id: str
    email: EmailStr
    phone_number: str
    is_manager: bool
    company: int
    role: str
    avatar_url: HttpUrl = "http://google.com"

    class Config:
        orm_mode = True
