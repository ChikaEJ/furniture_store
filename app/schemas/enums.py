from enum import Enum


class FurnitureCategory(str, Enum):
    TABLE = "table"
    CHAIR = "chair"
    SOFA = "sofa"