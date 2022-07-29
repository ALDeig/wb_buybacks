import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tgbot.services.db_connection import Base


class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    username = sa.Column(sa.String(), nullable=True)
    subscribe = sa.Column(sa.Date(), nullable=True)
    tracking_id = relationship("Tracking")


class Tracking(Base):
    __tablename__ = "tracking"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.ForeignKey("users.id", ondelete="CASCADE"))
    product_id = sa.Column(sa.Integer, unique=False)
    count = sa.Column(sa.Integer)
