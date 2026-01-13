from sqlalchemy import Integer, DateTime, func
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session