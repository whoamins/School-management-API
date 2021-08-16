from typing import List
from fastapi import FastAPI, Path
from db.db import database, students
from models.student import Student


app = FastAPI()


# TODO: Add more endpoints


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/students-read/', response_model=List[Student])
async def get_students():
    query = students.select()

    return await database.fetch_all(query)


@app.post('/students-create/', response_model=Student)
async def create_student(student: Student):
    query = students.insert().values(name=student.name, age=student.age, group=student.group)
    last_record = await database.execute(query)

    return {**student.dict(), "id": last_record}


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    query = students.delete().where(id == student_id)
    await database.execute(query)

    return {"info": "Post deleted", "status_code": 204}

