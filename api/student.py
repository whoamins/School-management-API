from typing import List
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from db.db import students, database
from models.student import Student

router = APIRouter()


@router.get('/', include_in_schema=False)
async def index():
    return RedirectResponse(url='/docs')


@router.get('/get-students/', response_model=List[Student])
async def get_students():
    query = students.select()
    return await database.fetch_all(query)


@router.get('/get-students-by-group/{group}', response_model=List[Student])
async def get_students_by_group(group: str):
    query = students.select().where(students.c.group == group)
    return await database.fetch_all(query)


@router.get('/get-students-by-age/{age}', response_model=List[Student])
async def get_students_by_age(age: int):
    query = students.select().where(students.c.age == age)
    return await database.fetch_all(query)


@router.post('/create-student/', response_model=Student)
async def create_student(student: Student):
    query = students.insert().values(first_name=student.first_name, last_name=student.last_name, age=student.age, group=student.group)
    last_record = await database.execute(query)

    return {**student.dict(), "id": last_record}


@router.delete("/delete-student/{student_id}")
async def delete_student(student_id: int):
    query = students.delete().where(students.c.id == student_id)
    await database.execute(query)

    return {"info": "Student deleted", "status_code": 204}
