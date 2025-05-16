from fastapi import FastAPI
import uvicorn
from routes.auth import router as auth_router

app = FastAPI(title="Todos REST API")
app.include_router(auth_router, prefix="/auth", tags=['auth'])

@app.get('/')
def get_root():
    return {"message": "Welcome to Todos REST API"}





if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)