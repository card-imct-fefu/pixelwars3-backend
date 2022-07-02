from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from pixelwars3.core.settings import settings

engine = create_async_engine(settings.database_url, future=True, echo=False)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)  # type: ignore


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


async def get_session() -> AsyncSession:  # type: ignore
    async with async_session() as session:
        yield session
