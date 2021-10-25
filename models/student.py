from pydantic import BaseModel, Field


class StudentIn(BaseModel):
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    age: int = Field(..., gt=15)
    group: str = Field(..., max_length=10)


class Student(StudentIn):
    id: int


