from fastapi import APIRouter, Depends
from sqlalchemy import select

from pixelwars3.core.database import get_session
from pixelwars3.user.models import VerifiedUser
from pixelwars3.user.schemas import VerifiedUserPydantic, azure_scheme

router = APIRouter()


@router.get("/", response_model=list[VerifiedUserPydantic])
async def get_verified_users(
    session=Depends(get_session), _=Depends(azure_scheme)
):
    q = await session.execute(select(VerifiedUser))
    return q.scalars().all()
