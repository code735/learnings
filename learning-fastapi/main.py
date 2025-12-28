from fastapi import FastAPI, Path;
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
def get_student(id: int = Path(...,description="Id of the student you want view",gt=0, lt=2)):
  return students[id]