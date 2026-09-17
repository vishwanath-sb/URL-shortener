from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from services.url_service import create_short_url, find_original_url


router = APIRouter()


class URLRequest(BaseModel):
    url: str


@router.post("/shorten")
def shorten_url(request: URLRequest):

    short_id = create_short_url(request.url)

    return {
        "short_id": short_id,
        "short_url": f"http://127.0.0.1:8000/{short_id}",
        "original_url": request.url
    }


@router.get("/{short_id}")
def redirect_url(short_id: str):

    url = find_original_url(short_id)

    if url is None:
        raise HTTPException(
            status_code=404,
            detail="short url not found"
        )

    return RedirectResponse(
        url=url,
        status_code=307
    )