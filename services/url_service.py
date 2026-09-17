from storage.url_storage import save_url, get_url


CHARACTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

counter = 1


def base62_encode(number):
    if number == 0:
        return CHARACTERS[0]

    result = []

    while number:
        remainder = number % 62
        result.append(CHARACTERS[remainder])
        number = number // 62

    return ''.join(reversed(result))


def create_short_url(original_url):
    global counter

    short_id = base62_encode(counter)

    save_url(short_id, original_url)

    counter += 1

    return short_id


def find_original_url(short_id):
    return get_url(short_id)