from ion_client import Client
from os import environ


def test_client():
    client = Client(username=environ["ION_USERNAME"], password=environ["ION_PASSWORD"])
    users = client.json("/users")
    assert "email" in users
