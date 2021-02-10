from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from mypack.config.utils import config_parser
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import mypack
import os

Base = declarative_base()

class Company(Base):
        __tablename__ = 'company'
        company_id = Column(Integer, primary_key=True)
        company_size = Column(String(6))
        industry = Column(String(50))

class Session(Base):
        __tablename__ = 'session'
        session_id = Column(Integer, primary_key=True)
        company_id = Column(Integer)
        created_at = Column(DateTime)

class Subscription(Base):
        __tablename__ = 'subscription'
        subscription_id = Column(Integer, primary_key=True)
        company_id = Column(Integer)
        subscription_amount = Column(Float)


def main(config_path = os.path.dirname(mypack.__file__ )+ '/config/database.ini'):
    params = config_parser(config_path)
    
    db_url = f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
    engine = create_engine(db_url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    Base.metadata.create_all(engine)


if __name__ == '__main__':
        main()