import logging
from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from factories.companies_factory import CompanyFactory
from models.models import Company
from repositories.company_repository import CompanyRepository

logger = logging.getLogger(__name__)


class CompanyService:
    @classmethod
    def get_all(self, db: Session) -> List[Company]:
        companies = CompanyRepository.get_all(db)
        if not companies:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Companies not found")
        return companies

    @classmethod
    def bulk_reactor(self, db: Session) -> Company:
        new_company = CompanyFactory(db)
        return new_company.company
