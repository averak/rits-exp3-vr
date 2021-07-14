from pydantic import BaseModel


class BookModel(BaseModel):
    title: str
    author: str
    description: str
    detail_url: str
    image_url: str
