from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    name="Get All companies",
)
async def all_companies():
    return "All companies"


@router.get(
    "/{company_id}/",
    status_code=status.HTTP_200_OK,
    name="Get Company by Id",
)
async def get_company(company_id: int):
    return "Ok"
