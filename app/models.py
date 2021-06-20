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


class UserApplication(Model):
    __tablename__ = 'user_application'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    application = Column(Integer, ForeignKey('application.id'))
    users_application = relationship("Application")
