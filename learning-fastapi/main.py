from fastapi import FastAPI;
app = FastAPI()

students = {
  1: {
    "name" : "john",
    "age" : "17",
    "class" : "12th"
  }
}

@app.get("/")
def home():
  return {"get": "wassup bitches"}

@app.get("/get-student/{id}")
def get_student(id: int):
  return students[id]