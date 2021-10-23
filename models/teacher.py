from pydantic import BaseModel


class Teacher(BaseModel):
    name: str
    age: int
    subject: str
    experience: int = 0
    degree: str
    salary: int
