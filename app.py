from fastapi import FastAPI

from routes import routers

app = FastAPI()

for router in routers:
    app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
