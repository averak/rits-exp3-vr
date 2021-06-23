from pydantic import BaseModel

from core.model.book_model import BookModel


class BooksResponse(BaseModel):
    books: list[BookModel]
