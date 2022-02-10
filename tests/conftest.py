import pytest

import oliver


@pytest.fixture
def app():
    app = oliver.create_app('testing')

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
