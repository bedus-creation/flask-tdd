from tests.test_case import TestCase


class TestHomePage(TestCase):
    def test_home_page_is_accessible_to_public(self, client):
        response = client.get('/')
        assert "200 OK" == response.status
