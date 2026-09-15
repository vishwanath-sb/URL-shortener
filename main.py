from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class URLRequest(BaseModel):
    url:str

url_mapping = {}
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
    return {"message" : "URL shortener"}

@app.post("/shorten")
def shorten_url(request: URLRequest):
    global counter

    # Generate short ID
    short_id = base62_encode(counter)

    # Store mapping
    url_mapping[short_id] = request.url

    # Increment counter for next URL
    counter += 1

    return {
        "short_id": short_id,
        "url": request.url
    }