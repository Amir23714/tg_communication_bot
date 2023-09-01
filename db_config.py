from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

ALCHEMY_URL = "sqlite:///replied_messages.db"

engine = create_engine(ALCHEMY_URL)

SessonLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    with SessonLocal() as session:
        yield session


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(String, index=True)
    spammed = Column(Boolean, index=True)

class Groups(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    group_link = Column(String, index=True)
