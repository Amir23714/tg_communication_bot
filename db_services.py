from db_config import Message, get_db
from db_config import Message, Groups


def get_message(message_id: str):
    db = next(get_db())
    return db.query(Message).filter(Message.message_id == message_id).first()


def create_message(message_id: str):
    db = next(get_db())

    message = Message(message_id=message_id, spammed=True)
    db.add(message)
    db.commit()
    db.refresh(message)


def get_groups():
    db = next(get_db())
    return db.query(Groups).all()


def create_group(group_link: str):
    db = next(get_db())

    group = Groups(group_link=group_link)
    db.add(group)
    db.commit()
    db.refresh(group)
