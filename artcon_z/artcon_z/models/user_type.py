from artcon_z.models.meta import Base, user_pwd_context, relationship
from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Integer,
    Text,
    )

class UserType(Base):
    __tablename__ = 'user_type'
    id = Column(Integer, primary_key=True)
    user_type = Column(Text, unique=True)
    users = relationship("User", back_populates="user_type")
