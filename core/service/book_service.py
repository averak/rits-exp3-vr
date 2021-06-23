import requests

from core.model.book_model import BookModel
from core.api.request.books_get_request import BooksGetRequest
from core.api.response.books_response import BooksResponse


class BookService:

    BASE_URL: str = 'https://www.googleapis.com/books/v1/volumes?q=%E5%BB%BA%E7%AF%89&maxResults=40'

    def get_books(self, request_body: BooksGetRequest) -> BooksResponse:
        base_url: str = 'https://www.googleapis.com/books/v1/volumes?q=%s&maxResults=%d'

        headers = {"content-type": "application/json"}
        res = requests.get(base_url % (request_body.keyword, request_body.max_results), headers)

        books: list[BookModel] = []
        for book_item in res.json()["items"]:
            try:
                books.append(
                    BookModel(
                        title=book_item["volumeInfo"]["title"],
                        author=book_item["volumeInfo"]["authors"][0],
                        detail_url=book_item["volumeInfo"]["infoLink"],
                        image_url=book_item["volumeInfo"]["imageLinks"]["smallThumbnail"],
                    )
                )
            except Exception:
                continue

        return BooksResponse(books=books)
