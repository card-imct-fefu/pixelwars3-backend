from sqlalchemy import Column, Integer, String

from pixelwars3.core.database import Base


class VerifiedUser(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
