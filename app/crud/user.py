from app.crud.base_crud import BaseCRUD
from app.models.user import User


class UserCRUD(BaseCRUD):
    pass

user_crud = UserCRUD(User)