FROM python:3.12.4

WORKDIR /my_book_library_project

COPY . /my_book_library_project/

RUN pip install fastapi && pip install sqlalchemy && pip install pydantic && pip install uvicorn

CMD ["fastapi", "run", "main.py", "--port", "8000"]