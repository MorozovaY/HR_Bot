from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String, Text

engine = create_engine('sqlite:///mydb.db')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    phone = Column(Integer(), unique=True)
    cv = Column(Text)
    access = Column(String)

    def __repr__(self):
        return f'<User {self.name} {self.email}>'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)