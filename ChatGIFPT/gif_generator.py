import os
from typing import Optional, List
from giphy_client import DefaultApi, RandomGif, Gif

api_instance = DefaultApi()


def get_gif(text: str) -> Optional[RandomGif]:
    api_response = api_instance.gifs_random_get(os.environ['GIPHY_API_KEY'], tag=text, rating='g')
    return api_response.data


def search_gifs(text: str, limit: int = 1) -> List[Gif]:
    offset = 0
    api_response = api_instance.gifs_search_get(
        os.environ['GIPHY_API_KEY'], text, limit=limit, offset=offset, rating='g', lang='en'
    )
    return api_response.data
