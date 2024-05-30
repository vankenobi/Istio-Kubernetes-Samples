from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def sayHello():
    return {"message": "Hello, World! : Version 2.0"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)