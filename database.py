# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

from config import DevelopementConfig


db = SQLAlchemy()
engine = create_engine(DevelopementConfig.SQlALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)
db_session = scoped_session(sessionmaker(bind=engine))
