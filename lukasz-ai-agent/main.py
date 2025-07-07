from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Agent Lukasz AI działa 🧠"}

@app.get("/")
def read_root():
    return {"message": "Agent Lukasz AI działa  M- "}


