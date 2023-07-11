from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from db.models import employee, salary
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from connect_jwt import create_access_token, validate_token

URL_DATABASE = (f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@'
                f'{DB_HOST}:{DB_PORT}/{DB_NAME}')

engine = create_engine(URL_DATABASE)
session = Session(engine)

app = FastAPI(title='Salary')


@app.get("/")
def main_page():
    return 'Hello!'


@app.post("/get_token")
def get_token(username: str, password: str):
    # Проверка учетных данных сотрудника
    query = select(employee).where(
        employee.c.username == username, employee.c.password == password)
    user = session.execute(query).all()
    if user:
        # Генерация JWT-токена
        access_token = create_access_token(
            data={'sub': username}, expires_delta=timedelta(days=1))
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=401, detail='invalid username or password')


@app.get("/salary")
def get_salary(username: str, token: dict = Depends(validate_token)):
    print(token)
    if username == token['sub']:
        query = select(employee).where(employee.c.username == username)
        salary_id = session.execute(query).all()[0][3]
        desired_salary = select(salary).where(salary.c.id == salary_id)
        resault_salary = session.execute(desired_salary).all()[0]
        return {'count': resault_salary[1],
                'next_increase': resault_salary[2]
                }
    else:
        return '403 Forbidden'
