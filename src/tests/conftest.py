from mypack.data_generator import User
import pytest

@pytest.fixture
def user_class():
    return User(1)