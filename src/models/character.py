from enum import Enum
from sqlalchemy import Column, Integer, String, Float, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
from src.database.connection import Base

class CharGender(Enum):
    M = 'Male'
    F = 'Female'

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    title = Column(String(50), nullable=True)
    gender = Column(SQLEnum(CharGender), nullable=False, default=CharGender.M)

    growths = relationship("CharGrowth", back_populates="char", uselist=False)

    def __repr__(self):
        #representação em texto para debug
        return f"<Character(id={self.id}, nome='{self.name}', title='{self.title}', gender='{self.gender}')>"


class CharGrowth(Base):
    __tablename__ = "char_growths"

    id = Column(Integer, ForeignKey("characters.id"), primary_key=True)

    ghp = Column(Integer, nullable=True)
    gstr = Column(Integer, nullable=True)
    gmag = Column(Integer, nullable=True)
    gspd = Column(Integer, nullable=True)
    gdex = Column(Integer, nullable=True)
    gdef = Column(Integer, nullable=True)
    gres = Column(Integer, nullable=True)
    glck = Column(Integer, nullable=True)
    gcha = Column(Integer, nullable=True)

    char = relationship("Character", back_populates="growths")

    def __repr__(self):
        return f"<CharGrowth(id={self.id}, ghp={self.ghp}, gstr={self.gstr}, gmag={self.gmag}, gspd={self.gspd}, gdex={self.gdex}, gdef={self.gdef}, gres={self.gres}, glck={self.glck}, gcha={self.gcha})>"