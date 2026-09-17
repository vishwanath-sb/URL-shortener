url_mapping = {}


def save_url(short_id, original_url):
    url_mapping[short_id] = original_url


def get_url(short_id):
    return url_mapping.get(short_id)