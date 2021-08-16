from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    group: str
