from src.database.connection import SessionLocal
from src.models.character import Character, CharGrowth
from src.models.gclass import GClass, GClassGrowth

class DBController:
    def __init__(self):
        self.db = SessionLocal()

    #obtem todos os personagens
    def load_characters(self):
        return self.db.query(Character).all()

    #obtem apenas um personagem por id
    def get_character(self, char_id):
        return self.db.query(Character).filter(Character.id == char_id).first()

    def get_char_growths(self, char_id):
        return self.db.query(CharGrowth).filter(CharGrowth.id == char_id).first()

    #obtem todas as classes
    def load_gclasses(self):
        return self.db.query(GClass).all()

    #obtem apenas um personagem por id
    def get_gclass(self, gclass_id):
        return self.db.query(GClass).filter(GClass.id == gclass_id).first()

    #obtem growth rates de uma classe
    def get_gclass_growths(self, gclass_id):
        return self.db.query(GClassGrowth).filter(GClassGrowth.id == gclass_id).first()

    #fecha a conexão com o banco
    def close(self):
        self.db.close()