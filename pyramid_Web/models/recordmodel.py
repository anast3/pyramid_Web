from sqlalchemy import (
    Column,
    Index,
    Integer,
    DateTime
)

from .meta import Base


class RecordModel(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    room = Column(Integer)
    time = Column(DateTime)


Index('my_index', RecordModel.time, unique=True, mysql_length=255)
