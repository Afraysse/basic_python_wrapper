# tests/test_tmdbwrapper.py

from tmdbwrapper import TV
from pytest import fixture

@fixture
def tv_keys():
    """ Returns only test data. """
    return ['id', 'origin_country', 'poster_path', 'name', 'overview',
            'popularity', 'backdrop_path', 'first_air_date', 'vote_count',
            'vote_average']

def test_tv_info(tv_keys):
    """ Test to make sure API call will get TV show info. """
    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should appear in the response."
    assert set(tv_keys).issubset(response.keys()), "All keys should be in the response."
