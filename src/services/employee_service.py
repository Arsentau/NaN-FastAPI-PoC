import logging

from repositories.employee_repository import EmployeeRepository

logger = logging.getLogger(__name__)


class EmployeeService:
    employee_repository = EmployeeRepository()

    def get_all(self, db):
        employee = self.employee_repository.get_all(db)
        return employee

    def get_by_id(self, db, _id: int):
        employee = self.employee_repository.get_by_id(db, _id)
        return employee

    def create(self, db, employee):
        employee = self.employee_repository.create(db, employee)
        return employee
