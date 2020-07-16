from public.index import app as testapp
import pytest


@pytest.fixture
def app():
    return testapp
