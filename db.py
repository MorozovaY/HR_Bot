from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Text

import settings

engine = create_engine(settings.DB_PATH)
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
    role = Column(Integer, default=0)
    
    def __repr__(self):
        return f'<User {self.name} {self.email}>'


class Role(Base):
	__tablename__ = "role"

	id = Column(Integer, primary_key=True)
	role = Column(String)

	def __repr__(self):
		return f"<role {self.role}>"

#Чтобы добавить колонку в любую таблицу, теперь можно добавить колонку и данные команды в консоли:
#alembic revision --autogenerate -m "comment"
#alembic upgrade head

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
