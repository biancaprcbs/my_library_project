from sqlalchemy.orm import Session

from . import models, schemas

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book_by_id(db: Session, id: int):
    return db.query(models.Book).filter(models.Book.id == id).first()

def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.titulo == title).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    #db_book = models.Book(titulo = book.titulo, genero = book.genero, autor_a_ = book.autor_a_)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, id: int, book: schemas.Book):
    db_book = get_book_by_id(db=db, id=id)
    db_book.titulo = book.titulo
    db_book.genero = book.genero
    db_book.autor_a_ = book.autor_a_
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book: schemas.Book):
    db.delete(book)
    db.commit()
    return {"message": "Livro removido com sucesso!"}

