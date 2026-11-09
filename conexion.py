from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///reservas.db"    

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind= engine)


