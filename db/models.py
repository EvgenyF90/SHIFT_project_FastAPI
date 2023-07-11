from sqlalchemy import (MetaData, Table, Column,
                        Integer, String, ForeignKey)


metadata = MetaData()

salary = Table(
    'salary',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('amount', Integer, nullable=False),
    Column('next_increase', String)
)


employee = Table(
    'employee',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column('salary_id', Integer, ForeignKey('salary.id'))
)
