from typing import List

from sqlalchemy.orm import Session

from models.models import Employee
from repositories.employee_repository import EmployeeRepository


class EmployeeService:
    employee_repository = EmployeeRepository()

    def get_all(self, db: Session) -> List[Employee]:
        all_employees = self.employee_repository.get_all(db)
        return all_employees

    def get_by_id(self, id: str, db: Session) -> Employee:
        employee = self.employee_repository.get_by_id(db, id)
        return employee

    def create(self, employee, db: Session) -> Employee:
        employee = self.employee_repository.create(db, employee)
        return employee
