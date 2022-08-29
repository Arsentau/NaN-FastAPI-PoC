from uuid import uuid4

from faker import Faker
from sqlalchemy.orm import Session

from models.models import Company
from repositories.company_repository import CompanyRepository


class CompanyFactory:
    """Generates Companies in the DB"""
    def __init__(self, db: Session) -> Company:
        """Set the DB session and the quantity of companies that should be created"""
        self.db = db
        self._companies_bulk_creator()

    def _company_creator(self) -> None:
        """Creates a single fake company"""
        fake = Faker()
        new_company = Company(
            id=str(uuid4()),
            company_name=fake.company(),
            address=fake.street_address(),
            city=fake.city(),
            state_province=fake.country_code(),
            country=fake.current_country(),
            zip_code=fake.postcode(),
            time_zone="America/New_York",
            owner_name=fake.first_name_nonbinary(),
            owner_last_name=fake.last_name_nonbinary(),
            email=fake.ascii_email(),
            phone_number=fake.phone_number(),
            tax_id=fake.isbn13()
        )
        self.company = new_company

    def _companies_bulk_creator(self) -> None:
        """Bulk companies creator method"""
        self._company_creator()
        CompanyRepository.create(self.company, self.db)
