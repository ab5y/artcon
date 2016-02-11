import datetime #<- will be used to set default dates on models
from artcon_z.models.meta import Base, user_pwd_context, relationship
from pyramid.security import Allow
from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Integer,
    Text,
    Unicode,     #<- will provide Unicode field
    UnicodeText, #<- will provide Unicode text field
    DateTime,    #<- time abstraction field
    )

class  User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    user_type_id = Column(Integer, ForeignKey('user_type.id'), nullable=False)
    name = Column(Text, nullable=False)
    email = Column(String(64), nullable=False)
    password = Column(String(300), nullable=False)
    # last_logged = Column(DateTime, default=datetime.datetime.utcnow)
    user_type = relationship("UserType", back_populates="users")

    def __init__(self, name, email, user_type_id):
        self.name = name
        self.email = email
        self.user_type_id = user_type_id

    def validate_password(self, password):
        ok, new_hash = user_pwd_context.verify_and_update(password, self.password)
        if ok:
            if new_hash:
                enc_insert_password(password)
        return ok

    def enc_insert_password(self, password):
        self.password = user_pwd_context.encrypt(password)

    def __repr__(self):
        return "<User(nickname = '%s', password = '%s', email = '%s')>" % (self.nickname, self.password, self.email)

    @property
    def __acl__(self):
        return [(Allow, self.id, 'edit')]