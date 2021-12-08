import os
import tempfile

import pytest
from bootstrap import create_app


class TestCase:
    @pytest.fixture
    def client(self):
        db_fd, db_path = tempfile.mkstemp()
        app = create_app()

        with app.test_client() as client:
            yield client

        os.close(db_fd)
        os.unlink(db_path)
