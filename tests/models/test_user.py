import pytest

from src.models.user import NewUserRequest


@pytest.fixture
def base_user_dict():
    return dict(
        email='User@Email.com',
        username='UseR',
        name='test user',
        birthday='2000-01-01',
        gender='Masculine',
        password='12345678',
        confirm_password='12345678'
    )


def test_should_create_request_correctly_and_treat_data_to_fit_in_db(base_user_dict):
    request = NewUserRequest(**base_user_dict)
    assert 'confirm_password' not in request.dict().keys()
    assert base_user_dict['password'] != request.password
    assert request.username == 'user'
    assert request.name == 'Test User'
    assert request.email == 'user@email.com'


def test_should_raise_an_error_for_different_passwords(base_user_dict):
    base_user_dict['confirm_password'] = '87654321'

    with pytest.raises(ValueError):
        NewUserRequest(**base_user_dict)


def test_should_raise_an_error_for_password_with_less_than_eight_characters(base_user_dict):
    base_user_dict['password'] = '12345'
    base_user_dict['confirm_password'] = '12345'

    with pytest.raises(ValueError):
        NewUserRequest(**base_user_dict)


def test_should_raise_an_error_for_invalid_email(base_user_dict):
    base_user_dict['email'] = 'user'

    with pytest.raises(ValueError):
        NewUserRequest(**base_user_dict)


def test_should_raise_an_error_for_empty_username(base_user_dict):
    base_user_dict['username'] = ''

    with pytest.raises(ValueError):
        NewUserRequest(**base_user_dict)


def test_should_raise_an_error_for_username_with_less_than_four_characters(base_user_dict):
    base_user_dict['username'] = 'ana'

    with pytest.raises(ValueError):
        NewUserRequest(**base_user_dict)


def test_should_raise_an_error_for_empty_name(base_user_dict):
    base_user_dict['name'] = ''

    with pytest.raises(ValueError):
        NewUserRequest(**base_user_dict)
