from fastapi import APIRouter, Depends

from core.service.book_service import BookService
from core.api.request.books_get_request import BooksGetRequest
from core.api.response.books_response import BooksResponse

book_service = BookService()
router = APIRouter()


@router.get('', status_code=200, response_model=BooksResponse)
async def get_books(request_body: BooksGetRequest = Depends()):
    return book_service.get_books(request_body)
