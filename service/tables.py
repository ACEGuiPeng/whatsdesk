__author__ = 'Raj'

from sqlalchemy import Column, Integer, String, TEXT
from service.base import Base
Base = Base.base


class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    body = Column(TEXT)
    from_id = Column(String(255))
    to_id = Column(String(255))
    notify = Column(String(255))
    participant_id = Column(String(255))
    is_out = Column(String(2))
    is_group = Column(String(2))
    is_media = Column(String(2))
    timestamp = Column(String(255))
    status = Column(String(2))


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    jid = Column(String(255))
    name = Column(TEXT)
    contact_image = Column(String(255))
    status_message = Column(String(255))
    status = Column(String(2))
    is_group = Column(String(2))
    is_online = Column(String(2))
    last_seen = Column(String(255))


class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    jid = Column(String(255))
    phone_number = Column(String(255))
    country_code = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    status_message = Column(String(255))
    password = Column(String(255))
    status = Column(String(2))
