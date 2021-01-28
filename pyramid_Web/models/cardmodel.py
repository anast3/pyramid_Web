from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey
)

from .meta import Base


class CardModel(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    number = Column(Text)  # номер карты
    client_id = Column(Text)  # имя заказчика
    validity = Column(Text)  # срок действия


Index('my_index', CardModel.number, unique=True, mysql_length=255)
