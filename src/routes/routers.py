from fastapi import APIRouter

from controllers import company_controllers

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(company_controllers.router, tags=["Companies"], prefix="/companies")
