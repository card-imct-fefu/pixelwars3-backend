from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pixelwars3.core.settings import settings
from pixelwars3.handlers import shutdown_handler, startup_handler
from pixelwars3.routes import router_v1


def get_application():
    _app = FastAPI(**settings.fastapi_kwargs)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.backend_cors_origins
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(router_v1)
    _app.add_event_handler("startup", startup_handler)
    _app.add_event_handler("shutdown", shutdown_handler)

    return _app


app = get_application()
