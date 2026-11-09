import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_PATH = "banco.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo = False)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

def init_db():
    from src.models.character import Character, CharGrowth
    from src.models.gclass import GClass, GClassGrowth

    banco_existe = os.path.exists(DB_PATH)

    Base.metadata.create_all(bind=engine) #cria as tabelas

    if not banco_existe:
        dados_iniciais()

def dados_iniciais():
    session = SessionLocal()

    try:
        #importar modelos
        #inserir objetos iniciais
        from src.models.character import Character, CharGrowth
        from src.models.gclass import GClass, GClassGrowth
        import src.database.datalist as d

        session.add_all(d.characters)
        session.add_all(d.char_growths)
        session.add_all(d.classes)
        session.add_all(d.class_growths)

        session.commit()
        print("database successfully created and populated")

    except Exception as e:
        session.rollback()
        print(f"error on database population: {e}")

    finally:
        session.close()