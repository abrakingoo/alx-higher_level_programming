#!/usr/bin/python3
"""
 a python file that contains the class definition
 of a State and an instance Base = declarative_base():
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Sequence, Integer, String


Base = declarative_base


class State(Base):
    """
    class definition of a State and an instance Base = declarative_base()
    """

    __tablename__ = 'states'

    id = column(Integer, Sequence('my_sequence'), primary_key=True,
                nullable=False)

    name = column(String(128), nullable=False)
