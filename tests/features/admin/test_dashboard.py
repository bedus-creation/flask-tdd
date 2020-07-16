import os
import tempfile
import pytest
from public.app import app


class TestDashboard:
    @pytest.fixture
    def app(self):
        return app

    def test_empty_db(self, client):
        response = client.get('/admin')
        assert "200 OK" == response.status
        assert b"Hello World" == response.data
