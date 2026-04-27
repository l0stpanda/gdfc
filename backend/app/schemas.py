# schemas.py
# Pydantic schemas define the shape of data coming IN and going OUT of your API.
# They are separate from models.py — models are about the database,
# schemas are about what the API accepts and returns.
#
# Example:
#
# from pydantic import BaseModel
#
# class UserCreate(BaseModel):   # What the frontend sends when creating a user
#     name: str
#
# class UserResponse(BaseModel): # What the API sends back
#     id: int
#     name: str
#
#     model_config = {"from_attributes": True}