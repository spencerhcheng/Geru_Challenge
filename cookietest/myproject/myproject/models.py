from pyramid.security import Allow, Everyone
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Page(Base):
    """
    Attributes and functions for Page class
    """
    __tablename__ = 'access'
    uid = Column(Integer, primary_key=True)
    session_identifier = Column(Text)
    accessed_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    page = Column(Text)

    def __init__(self, session_identifier, page):
        """
        Instantiation of new Page class
        """
        self.session_identifier = session_identifier
        self.page = page

class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass
