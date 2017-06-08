"""Module to create database tables."""

from sqlalchemy import (create_engine, Column, Integer, String)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rooms(Base):
    """Table to hold information about the rooms."""

    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_name = Column(String(20), nullable=False, unique=True)
    room_type = Column(String(20), nullable=False)
    no_of_occupants = Column(Integer, nullable=False)


class People(Base):
    """Table to hold information about staff and Fellows."""

    __tablename__ = 'people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)
    category = Column(String(10), nullable=False)
    wants_acc = Column(String(5), nullable=False, default='False')


class Allocations(Base):
    """Table to hold information about staff and Fellows."""

    __tablename__ = 'allocations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)
    office_allocated_to = Column(String(20), nullable=True)
    living_allocated_to = Column(String(20), nullable=True)


def create_db(db_name):
    """Create a db with tables defined in the classes above."""
    engine = create_engine('sqlite:///' + db_name)
    Base.metadata.create_all(engine)
    return engine
