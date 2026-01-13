from fastapi_emp.app.core.database import Base


class Furniture(Base):
    __tablename__ = "furniture"

    title: Mapped[str]