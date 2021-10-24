from pydantic import BaseModel


class Teacher(BaseModel):
    first_name: str
    last_name: str
    age: int
    subject: str
    experience: int = 0
    degree: str
    salary: int
