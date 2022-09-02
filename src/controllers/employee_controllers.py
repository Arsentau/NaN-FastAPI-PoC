from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from models.schemas.employee import EmployeeSchema
from services.employee_service import EmployeeService

router = APIRouter()
employee_service = EmployeeService()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    name="Get all employees",
    response_model=List[EmployeeSchema]
)
async def get_all_employees(db: Session = Depends(get_db)):
    return employee_service.get_all(db)


@router.get(
    "/{id}/",
    status_code=status.HTTP_200_OK,
    name="Get employee by Id",
)
async def get_employee(id: str, db: Session = Depends(get_db)):
    return employee_service.get_by_id(db, id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    name="Create a employee",
)
async def new_employee(employee: EmployeeSchema, db: Session = Depends(get_db)):
    return employee_service.create(employee, db)
