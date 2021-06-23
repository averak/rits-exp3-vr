from pydantic import BaseModel


class BooksGetRequest(BaseModel):
    keyword: str
    max_results: int
