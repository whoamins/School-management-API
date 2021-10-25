from pydantic import BaseModel, validator, Field


class TeacherIn(BaseModel):
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    age: int = Field(..., gt=20)
    subject: str = Field(..., max_length=50)
    experience: int = 0
    degree: str = Field(..., max_length=50)
    salary: int = Field(..., gt=0)


class Teacher(TeacherIn):
    id: int
