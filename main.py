from fastapi import FastAPI, Path


app = FastAPI()

# TODO: Connect with db.
# TODO: Add more endpoints
# TODO: Add validation for input values
# TODO: Add error handlers

students = {
    1: {
        "name": "John Doe",
        "age": 18,
        "class": "4650"
    }
}


@app.get('/')
def index():
    return {
        "name": "First_name"
    }


@app.get('/get_student_by_id/{student_id}')
def get_student(student_id: int = Path(None, description="ID of the student you want to get", gt=0)):
    return students[student_id]


@app.get('/get_student_by_name/')
def get_student(student_name: str):
    for student_id in students:
        if students[student_id]["name"] == student_name:
            return students[student_id]

    return {"Error": "Student was not found"}
