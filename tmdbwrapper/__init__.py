# need to construct a dictionary object from the TMDB API
# return that via the info method
import os
import requests

TMDB_API_KEY = os.environ.get('TMDB_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if TMDB_API_KEY is None:
    raise APIKeyMissingError(
        "All Methods require an API key. See "
        "https://developers.themoviedb.org/3/getting-started/introduction "
        "for how to retrieve an authentication token from "
        "The Movie Database""
    )

session = request.Session()
session.params = {}
session.params['api_key'] = TMDB_API_KEY

from .tv import TV