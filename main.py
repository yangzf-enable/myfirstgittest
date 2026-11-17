from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "你好，这是我的第一个服务"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"你好，{name}"}