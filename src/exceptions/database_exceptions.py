from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError


class DatabaseExceptions:

    @classmethod
    def throw_internal_server_error(self) -> None:
        """Throws a generic DB error"""
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Oops, we couldn't connect to the db, please try again later"
        )

    @classmethod
    def throw_not_found_error(self, item: str) -> None:
        """Throws a Not Found DB error for an specific item"""
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{item} not found"
        )

    @classmethod
    def throw_db_integrity_error(self, e: IntegrityError):
        """Throws SqlAlchemy integrity error detail"""
        detail = ""
        if e.orig.diag.message_detail:
            detail = e.orig.diag.message_detail
        else:
            detail = str(e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail
        )
