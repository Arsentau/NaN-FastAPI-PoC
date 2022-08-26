from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from models.schemas.company import CompanySchema
from services.company_service import CompanyService

router = APIRouter()


@router.get(
    "/mock-company",
    status_code=status.HTTP_201_CREATED,
    name="Create and get mock company",
    response_model=CompanySchema
)
async def mock_company_creator(db: Session = Depends(get_db)):
    return CompanyService.bulk_reactor(db)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    name="Get all companies"
)
async def get_all_companies(db: Session = Depends(get_db)):
    return CompanyService.get_all(db)


@router.get(
    "/{company_id}/",
    status_code=status.HTTP_200_OK,
    name="Get Company by Id",
)
async def get_company(company_id: str):
    return "Ok"
