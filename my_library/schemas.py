from pydantic import BaseModel
from pydantic import ConfigDict

class BookBase(BaseModel):
    titulo: str
    genero: str
    autor_a_: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
