from sqlalchemy import Column, Integer, String
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import func

from db import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    contact_number = Column(String(10), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    address = Column(String(120), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP)

    def __repr__(self):
        return '<User %r>' % (self.name)


Base.metadata.create_all(engine)
