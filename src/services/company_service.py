from typing import List
from uuid import uuid4

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from factories.companies_factory import CompanyFactory
from models.models import Company
from models.schemas.company import NewCompanySchema, PatchCompanySchema
from repositories.company_repository import CompanyRepository


class CompanyService:
    @classmethod
    async def single_creator(self, db: Session) -> Company:
        """Creates a single mock company"""
        new_company = CompanyFactory(db)
        return new_company.company

    @classmethod
    async def bulk_creator(self, db: Session, n: int) -> List[Company]:
        """Creates n new mock companies"""
        new_companies = list()
        for _ in range(n):
            new_companies.append(await CompanyService.single_creator(db))
        return new_companies

    @classmethod
    async def get_all(self, db: Session) -> List[Company]:
        companies = await CompanyRepository.get_all(db)
        if not companies:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Companies not found")
        return companies

    @classmethod
    async def get_by_id(self, id: str, db: Session) -> Company:
        return await CompanyRepository.get_by_id(id, db)

    @classmethod
    async def edit_company(self, id: str, request: PatchCompanySchema, db: Session) -> Company:
        company: Company = await CompanyRepository.get_by_id(id, db)
        for (k, v) in request.dict().items():
            if v:
                setattr(company, k, v)
        await CompanyRepository.patch(company, db)
        return company

    @classmethod
    async def new_company(self, request: NewCompanySchema, db: Session) -> Company:
        req = request.dict()
        req["id"] = str(uuid4())
        company = Company(**req)
        await CompanyRepository.create(company, db)
        return company

    @classmethod
    async def delete_company(self, id: str, db: Session) -> None:
        await CompanyRepository.delete(id, db)
