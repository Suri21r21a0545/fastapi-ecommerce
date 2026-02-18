from pydantic import BaseModel


# USER REGISTER SCHEMA
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"


# LOGIN SCHEMA
class Login(BaseModel):
    email: str
    password: str


# PRODUCT CREATE SCHEMA
class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int


# ADD TO CART SCHEMA
class CartAdd(BaseModel):
    product_id: int
    quantity: int
