from typing import List
from fastapi import FastAPI, Path
from starlette.responses import RedirectResponse

from db.db import database, students
from models.student import Student


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/', include_in_schema=False)
async def index():
    return RedirectResponse(url='/docs')


@app.get('/get-students/', response_model=List[Student])
async def get_students():
    query = students.select()
    return await database.fetch_all(query)


'''
@app.get('/get-student-by-id/{student_id}', response_model=Student)
async def get_student_by_id(student_id: int):
    query = students.select().where(students.c.id == student_id)
    return await database.fetch_one(query=query)
'''


@app.post('/create-student/', response_model=Student)
async def create_student(student: Student):
    query = students.insert().values(name=student.name, age=student.age, group=student.group)
    last_record = await database.execute(query)

    return {**student.dict(), "id": last_record}


@app.delete("/delete-student/{student_id}")
async def delete_student(student_id: int):
    query = students.delete().where(id == student_id)
    await database.execute(query)

    return {"info": "Student deleted", "status_code": 204}
