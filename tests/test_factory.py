import oliver


def test_config():
    assert not oliver.create_app().testing
    assert oliver.create_app('testing').testing


def test_home(client):
    response = client.get("/welcome")
    assert response.data == b"Welcome to Oliver"
