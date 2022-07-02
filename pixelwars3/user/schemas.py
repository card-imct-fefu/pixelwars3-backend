from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
from pydantic import BaseModel

from pixelwars3.core.settings import settings


class VerifiedUserBasePydantic(BaseModel):
    email: str


class VerifiedUserPydantic(VerifiedUserBasePydantic):
    id: int

    class Config:
        orm_mode = True


class VerifiedUserInCreatePydantic(VerifiedUserBasePydantic):
    pass


class VerifiedUserInUpdatePydantic(VerifiedUserBasePydantic):
    pass


azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id=settings.app_client_id,
    tenant_id=settings.tenant_id,
    scopes={
        f'api://{settings.app_client_id}/user_impersonation': 'user_impersonation',
    },
)
