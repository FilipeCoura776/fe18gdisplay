from src.database.connection import SessionLocal
from src.models.character import Character
from src.models.gclass import GClass
from src.controllers.db_func import DBController

def calculate_growths(con, char_id, gclass_id):
    c = con.get_char_growths(char_id)
    g = con.get_gclass_growths(gclass_id)

    print(c)
    print(g)

    full_growths = [
        c.ghp + (g.ghp or 0),
        c.gstr + (g.gstr or 0),
        c.gmag + (g.gmag or 0),
        c.gspd + (g.gspd or 0),
        c.gdex + (g.gdex or 0),
        c.gdef + (g.gdef or 0),
        c.gres + (g.gres or 0),
        c.glck + (g.glck or 0),
        c.gcha + (g.gcha or 0)
    ]

    # Mu aptitude -------------------
    if char_id == 34: 
        for i in range(9):
            full_growths[i] += 20
    #--------------------------------

    return full_growths

class SkillRanks:
    SWORD = 1      # 2^0  ( 1)
    SPEAR = 2      # 2^1  ( 2)
    AXE = 4        # 2^2  ( 4)
    BOW = 8        # 2^3  ( 8)
    GAUNTLET = 16  # 2^4  (16)
    BLACK = 32     # 2^5  (32) - Black Magic
    WHITE = 64     # 2^6  (64) - White Magic
    INFANTRY = 128 # 2^7  (128)
    CAVALRY = 256  # 2^8  (256)
    ARMORED = 512  # 2^9  (512)
    FLYING = 1024  # 2^10 (1024)

def get_ranks(bitmask_val: int) -> list:
    verif_order = [
        ("Sword", SkillRanks.SWORD),
        ("Spear", SkillRanks.SPEAR),
        ("Axe", SkillRanks.AXE),
        ("Bow", SkillRanks.BOW),
        ("Gauntlet", SkillRanks.GAUNTLET),
        ("Black", SkillRanks.BLACK),
        ("White", SkillRanks.WHITE),
        ("Infantry", SkillRanks.INFANTRY),
        ("Cavalry", SkillRanks.CAVALRY),
        ("Armored", SkillRanks.ARMORED),
        ("Flying", SkillRanks.FLYING),
    ]

    active_skills = []

    for key, skill in verif_order:
        if (bitmask_val & skill) != 0: # this & (bitwise) operator thingy is really fucking cool
            active_skills.append(key)

    print(active_skills)
    return active_skills