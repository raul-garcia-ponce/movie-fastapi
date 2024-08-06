import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


sqlitename = 'movie.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
datebaseUrl = f"sqlite:///{os.path.join(base_dir,sqlitename)}"

engine = create_engine(datebaseUrl, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
