from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

app = FastAPI()


class URLRequest(BaseModel):
    url: str


# In-memory storage
url_mapping = {}

# Counter for generating unique IDs
counter = 1


# Base62 characters
CHARACTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def base62_encode(number):
    if number == 0:
        return CHARACTERS[0]

    result = []

    while number:
        remainder = number % 62
        result.append(CHARACTERS[remainder])
        number = number // 62

    return ''.join(reversed(result))


@app.get("/")
def home():
    return {"message": "URL Shortener"}


@app.post("/shorten")
def shorten_url(request: URLRequest):
    global counter

    # Generate short ID
    short_id = base62_encode(counter)

    # Store mapping
    url_mapping[short_id] = request.url

    # Increment counter
    counter += 1

    return {
        "short_id": short_id,
        "url": request.url
    }


@app.get("/{short_id}")
def redirect_url(short_id: str):

    if short_id not in url_mapping:
        raise HTTPException(
            status_code=404,
            detail="short url not found"
        )

    url = url_mapping[short_id]

    return RedirectResponse(
        url=url,
        status_code=307
    )