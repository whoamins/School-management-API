from typing import List
from fastapi import FastAPI
from starlette.responses import RedirectResponse

import api.student
from db.db import database, students
from models.student import Student


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(api.student.router, prefix='/students', tags=['Students'])
