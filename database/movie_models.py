from datetime import datetime
from sqlalchemy import Table, Column
from sqlalchemy import Integer, ForeignKey, String, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()
movies_metadata = Base.metadata

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    film_length = Column(Integer, nullable=False)
    status_id = Column(Integer(), ForeignKey('movie_status.id'))
    cover_path = Column(String(255))
    year = Column(Integer(), nullable=False)
    description = Column(String(255))
    film_director_id = Column(Integer(), ForeignKey('film_directors.id'))
    genre_id = Column(Integer(), ForeignKey('genres.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def repr(self):
        return '%r' % self.title

class Film_director(Base):
    __tablename__ = "film_directors"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def repr(self):
        return '%r' % self.id

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key = True)
    name = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    def repr(self):
        return '%r' % self.name

class MovieStatus(Base):
    __tablename__ = "movie_status"
    id = Column(Integer, primary_key = True)
    name = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
