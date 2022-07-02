from fastapi.routing import APIRouter

from pixelwars3.field.api.v1 import router as field_router_v1
from pixelwars3.user.api.v1 import router as user_router_v1

router_v1 = APIRouter(prefix="/v1")
router_v1.include_router(
    prefix="/verified-user",
    tags=["verified-user"],
    router=user_router_v1,
)
router_v1.include_router(
    prefix="/field", tags=["user"], router=field_router_v1
)
