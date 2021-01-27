from sqlalchemy import (
    Column,
    Integer,
    Text
)

from .meta import Base


class CreditModel(Base):
    __tablename__ = 'credits'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)  # взятая в кредит сумма
    client_id = Column(Text)  # имя заказчика
    percent = Column(Integer)  # годовой процент
    validity = Column(Text)  # срок погашения
