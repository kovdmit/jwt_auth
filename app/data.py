from utils import get_password_hash


USERS_DATA = {
    'admin': {'username': 'admin', 'password': get_password_hash('pw')},
}
