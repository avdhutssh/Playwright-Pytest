import pytest

pytest.fixture(scope="session")
def user_creds(request):
    return request.param