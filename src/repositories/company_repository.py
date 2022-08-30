import logging
from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from exceptions.database_exceptions import DatabaseExceptions
from models.models import Company

logger = logging.getLogger(__name__)


class CompanyRepository:
    @classmethod
    async def get_all(self, db: Session) -> List[Company]:
        """Gets all company's records from the DB"""
        try:
            companies = db.query(Company).all()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error()
        if not companies:
            logger.error("There are not companies in the database yet")
            DatabaseExceptions.throw_not_found_error("Companies")
        return companies

    @classmethod
    async def get_by_id(self, id: str, db: Session) -> Company:
        """Gets a single company's records from the DB by id"""
        try:
            company = db.query(Company).filter(Company.id == id).first()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error()

        if not company:
            logger.error(f"The company_id: {id} does not exist")
            DatabaseExceptions.throw_not_found_error("Company")
        return company

    @classmethod
    async def create(self, company: Company, db: Session) -> None:
        """Creates a company record on the DB"""
        try:
            db.add(company)
            db.commit()
            db.refresh(company)
        except IntegrityError as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_db_integrity_error(e)
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error()

    @classmethod
    async def delete(self, id: str, db: Session) -> None:
        """Deletes a company record from DB"""
        company = await CompanyRepository.get_by_id(id, db)
        try:
            db.delete(company)
            db.commit()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error()

    @classmethod
    async def patch(self, company: Company, db: Session):
        """Updates a company record in DB"""
        try:
            db.add(company)
            db.commit()
        except IntegrityError as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_db_integrity_error(e)
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error()
