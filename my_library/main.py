from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Bem-vindo(a)! - Biblioteca Infinito Particular"}


@app.post("/books/", response_model=schemas.Book)
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db, title=book.titulo)
    if db_book:
        raise HTTPException(status_code=400, detail="Livro já registrado!")
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=list[schemas.Book])
async def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{id}", response_model=schemas.Book)
async def read_book(id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db=db, id=id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    return db_book

@app.put("/books/{id}", response_model=schemas.Book)
async def update_book(id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db=db, id=id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    return crud.update_book(db=db, id=id, book=book)

@app.delete("/books/{id}", status_code=status.HTTP_200_OK)
async def delete_book(id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db=db, id=id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    return crud.delete_book(db=db, book=db_book)