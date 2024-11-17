from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def root():
    return {"message": "Вы вошли как администратор"}
@app.get("/user/{user_id}")
async def welcome(user_id: int):
    return {"message": "Вы вошли как пользователь № {user_id}"}
@app.get("/user/{username}/{age}")
async def welcome(username: str, age:int):
    return {"message": "Информация о пользователе. Имя: {username}, Возраст: {age}"}


