# models.py
# Define your database tables here as Python classes.
# Each class = one table. Each attribute = one column.
#
# Example:
#
# from sqlalchemy import String, Integer
# from sqlalchemy.orm import Mapped, mapped_column
# from app.database import Base
#
# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String, nullable=False)
#
# Tables are created automatically on app startup (see main.py).