from app.crud.base_crud import BaseCRUD
from app.models.furniture import Furniture


class FurnitureCRUD(BaseCRUD):
    pass

furniture_crud = FurnitureCRUD(Furniture)