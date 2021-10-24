from pydantic import BaseModel


class Student(BaseModel):
    first_name: str
    last_name: str
    age: int
    group: str

