from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db import Base

class User(Base):
    __tablename__="users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    
    posts: Mapped['Posts'] = relationship(back_populates='author')
    
class Posts(Base):
    __tablename__="posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    author: Mapped['User'] = relationship(back_populates='posts')