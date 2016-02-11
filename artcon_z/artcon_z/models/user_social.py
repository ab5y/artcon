from artcon_z.models.meta import Base, user_pwd_context, relationship
from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Integer,
    Text,
    )

class UserSocial(object):
    """docstring for UserSocial"""
    __tablename__ = 'user_social'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    social_id = Column(String(64), nullable=False, unique=True)
    nickname = Column(String(64), nullable=False)
    def __init__(self, arg):
        super(UserSocial, self).__init__()
        self.arg = arg
