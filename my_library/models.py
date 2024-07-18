from sqlalchemy import Column, Integer, String

from .database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    genero = Column(String)
    autor_a_ = Column(String)