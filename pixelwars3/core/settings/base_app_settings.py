from pydantic import BaseSettings

from pixelwars3.core.settings.app_env_types import AppEnvTypes


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.test

    class Config:
        env_file = ".env"
