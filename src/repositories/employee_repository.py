from typing import List

from models.models import Employee
from models.schemas.employee import EmployeeSchema


class EmployeeRepository:

    def get_all(self, db) -> List[Employee]:
        return db.query(Employee).all()

    def get_by_id(self, db, _id: int) -> Employee:
        return db.query(Employee).filter(Employee.id == _id).first()

    def create(self, db, employee: EmployeeSchema):
        entity = Employee(**employee.dict())
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity
