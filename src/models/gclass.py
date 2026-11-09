from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from src.database.connection import Base

class GClassTiers(Enum):
    Base = 'Base'
    Beginner = 'Beginner'
    Specialty = 'Specialty'
    Advanced = 'Advanced'
    Master = 'Master'
    Divine = 'Divine'

class GClassColors(Enum):
    Base = 'Base'
    Red = 'Gladiators'
    Yellow = 'Hunters'
    Green = 'Soldiers'
    Blue = 'Fliers'
    Purple = 'Mages'


#GClass name is for 'Game Class', since the word 'class' is a keyword in python and most other languages.
class GClass(Base):
    __tablename__ = "gclasses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    tier = Column(SQLEnum(GClassTiers), nullable=False, default=GClassTiers.Base)
    color = Column(SQLEnum(GClassColors), nullable=False, default=GClassColors.Base)
    skills = Column(Integer, nullable=False, default=1) #bitmask for defining available weapons and class move type(s)

    growths = relationship("GClassGrowth", back_populates="gclass", uselist=False) #testing this tidbit

    def __repr__(self):
        return f"<GClass(id={self.id}, nome='{self.name}')>"


class GClassGrowth(Base):
    __tablename__ = "gclass_growths"

    id = Column(Integer, ForeignKey("gclasses.id"), primary_key=True)

    #putting a g before the stats to represent 'growth', might do something with bases later so idk
    ghp = Column(Integer, nullable=True, default=None)
    gstr = Column(Integer, nullable=True)
    gmag = Column(Integer, nullable=True)
    gspd = Column(Integer, nullable=True)
    gdex = Column(Integer, nullable=True)
    gdef = Column(Integer, nullable=True)
    gres = Column(Integer, nullable=True)
    glck = Column(Integer, nullable=True)
    gcha = Column(Integer, nullable=True)

    gclass = relationship("GClass", back_populates="growths")

    def __repr__(self):
        return f"<GClassGrowth(id={self.id}, ghp={self.ghp}, gstr={self.gstr}, gmag={self.gmag}, gspd={self.gspd}," +\
        f"gdex={self.gdex}, gdef={self.gdef}, gres={self.gres}, glck={self.glck}, gcha={self.gcha})>"

