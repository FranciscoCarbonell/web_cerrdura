from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Application(Model):
    __tablename__ = 'application'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    user_applications = relationship('UserApplication')

    def __repr__(self):
        return self.name


class UserApplication(Model):
    __tablename__ = 'user_application'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    application_id = Column(Integer, ForeignKey('application.id'))
    application = relationship("Application")
    devices = relationship('Device')
    user_id = Column(Integer, ForeignKey('ab_user.id'))
    user = relationship('User')

    def __repr__(self):
        return self.name


class Device(Model):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    reference = Column(String(255), nullable=False)
    user_aplication_id = Column(Integer, ForeignKey('user_application.id'))
    user_application = relationship('UserApplication')

    def __repr__(self):
        return self.name
