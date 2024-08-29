from pydantic import BaseModel


class SignUp_l(BaseModel):
    name: str
    username: str
    role: str
    password: str

class User_l(BaseModel):
    username: str
    password: str
