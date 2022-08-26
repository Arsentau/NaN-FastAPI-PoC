from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.models import Company


class CompanyRepository:
    @classmethod
    def get_all(self, db: Session) -> List[Company]:
        try:
            return db.query(Company).all()
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Oops, we couldn't connect to the db, please try again later"
            )

    def get_by_id(self, db: Session, _id: str) -> Company:
        return db.query(Company).filter(Company.id == _id).first()

    @classmethod
    def bulk_create(self, db: Session, company: Company):
        try:
            db.add(company)
            db.commit()
            db.refresh(company)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Oops, we couldn't connect to the db, please try again later"
            )
