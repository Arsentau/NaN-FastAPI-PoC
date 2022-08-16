from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    name="Get all employees",
)
async def get_all_employees():
    return "All employees:"


@router.get(
    "/{company_id}/",
    status_code=status.HTTP_200_OK,
    name="Get employee by Id",
)
async def get_employee(company_id: int):
    return "Ok"
