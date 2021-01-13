from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import settings
from retrying_query import RetryingQuery

engine = create_engine(
    settings.DB_CONNECTION_STRING,
    pool_size=10,
    max_overflow=2,
    pool_recycle=300,
    pool_pre_ping=True,
    pool_use_lifo=True,
)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine, query_cls=RetryingQuery)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models

    Base.metadata.create_all(bind=engine)


init_db()
