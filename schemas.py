from datetime import date

from pydantic import BaseModel


# Модель для данных о зарплате
class Salary(BaseModel):
    amount: float
    next_increase: date


# Модель для данных сотрудника
class Employee(BaseModel):
    username: str
    password: str
    salary: Salary


# Модель для токена
class Token(BaseModel):
    access_token: str
    token_type: str
