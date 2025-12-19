from fastapi import FastAPI;
app = FastAPI()


@app.get("/")
def home():
  return {"get": "wassup bitches"}