from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class UserType(Base):
    __tablename__ = 'user_type'
    id = Column(Integer, primary_key=True)
    user_type = Column(Text, unique=True)
    users = relationship("User", back_populates="user_type")

class  User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_type_id = Column(Integer, ForeignKey('user_type.id'))
    name = Column(Text, nullable=False)
    user_type = relationship("UserType", back_populates="users")
