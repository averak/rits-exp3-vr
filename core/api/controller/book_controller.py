from fastapi import APIRouter, Depends

from core.model.book_model import BookModel
from core.api.request.books_get_request import BooksGetRequest
from core.api.response.books_response import BooksResponse

router = APIRouter()


@router.get('', status_code=200, response_model=BooksResponse)
async def get_books(request: BooksGetRequest = Depends()):
    # FIXME: とりあえずモックを作成しています
    books: list[BookModel] = []
    books.append(BookModel(
        title="タイトル",
        author="著者",
        detail_url="詳細URL",
        image_url="画像URL",
    ))

    return BooksGetRequest(books=books)
