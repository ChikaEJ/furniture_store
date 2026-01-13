class UserAlreadyExists(Exception):
    message = 'User already exists.'

class DatabaseUnavailable(Exception):
    message = 'Database unavailable.'
