from src.models.character import Character, CharGrowth
from src.models.gclass import GClass, GClassGrowth

characters = [
            Character(name="Eshmel", title="The Promised One", gender='F'), #gender set as female for pegasus access, i don't yet know if there's male exclusive classes

            #Ribeira Winds
            Character(name="Cai", title='Test', gender='M'),
            Character(name="Tialla", title='Test', gender='F'),
            Character(name="Peter", title='Test', gender='M'),
            Character(name="Ultand", title='Test', gender='F'),

            #Fiery Mane
            Character(name="Bertrand", title='Test', gender='M'),
            Character(name="Gaitz", title='Test', gender='M'),
            Character(name="Jester", title='Test', gender='M'),
            Character(name="Goliath", title='Test', gender='M'),
            Character(name="Dante", title='Test', gender='F'),

            #House Lamine
            Character(name="Dietrich", title='Test', gender='M'),
            Character(name="Fabio", title='Test', gender='M'),
            Character(name="Esmeralda", title='Test', gender='F'),
            Character(name="Mikaela", title='Heroic Redblade', gender='F'),

            #Linaria Dewdrops
            Character(name="Orchel", title='Test', gender='F'),
            Character(name="Diego", title='Test', gender='M'),
            Character(name="Loretta", title='Test', gender='F'),
            Character(name="Seteth", title='Test', gender='M'),
            Character(name="Ninae", title='Test', gender='F'),

            #Megaira's Beacon
            Character(name="Theodora", title='Test', gender='F'),
            Character(name="Bonaventure", title='Test', gender='M'),
            Character(name="Tobias", title='Test', gender='M'),
            Character(name="Lilian", title='Test', gender='F'),
            Character(name="Lysander", title='Soldier of Saramis', gender='M'),

            #Tale of the Moon
            Character(name="Talimun", title='Test', gender='M'),
            Character(name="Ursula", title='Test', gender='F'),
            Character(name="Ludia", title='Test', gender='F'),
            Character(name="Simon", title='Test', gender='M'),
            Character(name="Fianna", title='Test', gender='F'),

            #Rose Tempest
            Character(name="Leda", title='Rose of Caelin', gender='F'),
            Character(name="Buccar", title='Demon Bear of Baphos', gender='M'),
            Character(name="Sirocco", title='Test', gender='M'),
            Character(name="Olympia", title='Blue Rose of Caelin', gender='F'),
            Character(name="Mu", title='Daughter of Mikaela', gender='F'),

            #Pale Raven's Bridal Party
            Character(name="Anatolia", title='Test', gender='F'),
            Character(name="Sha Lan", title='Test', gender='F'),
            Character(name="Nezha", title='Test', gender='M'),
            Character(name="Dadao", title='Test', gender='M'),
            Character(name="Halvin", title='Test', gender='F'),

            #Promised One's Army
            Character(name="Hong Hua", title='Test', gender='F'),
            Character(name="Troy", title='Test', gender='F'),

            #Others
            Character(name="Guzran", title='The Unkillable', gender='M'),
            Character(name="Yang Jie", title='Test', gender='M'),
            Character(name="Io", title='Test', gender='M'),
            Character(name="Peppe", title='Test', gender='M'),
            Character(name="Noctula", title='Test', gender='F'),
            Character(name="Sofia", title='Peckish Priest', gender='F'),
            Character(name="Catania", title='Test', gender='F'),
            Character(name="Nydine", title='Test', gender='F'),
            Character(name="Zarcone", title='Test', gender='M'),
            Character(name="Majide", title='Test', gender='M'),
            Character(name="Benditz", title='Test', gender='M'),
            Character(name="Inyoni", title='Test', gender='F'),
            Character(name="Jasmine", title='Test', gender='F'),
            Character(name="Alexandra", title='Silver Maiden', gender='F'),
            Character(name="Nuzzuo", title='Test', gender='M'),
            Character(name="Centurio", title='Test', gender='M'),
            Character(name="Aswan", title='Test', gender='F'),
            Character(name="Nathan", title='Catoblepas', gender='M'),
            Character(name="Creek", title='Pantere', gender='M'),
            Character(name="Kiroc", title='The Rukh', gender='M'),
            Character(name="Klapka", title='Test', gender='M'),
            Character(name="Tahonia", title='Test', gender='F')
        ]

char_growths = [
            CharGrowth(id=1 , ghp=50, gstr=45, gmag=45, gspd=45, gdex=45, gdef=35, gres=35, glck=40, gcha=50), #Bird

            #Ribeira Winds
            CharGrowth(id=2 , ghp=45, gstr=45, gmag=40, gspd=45, gdex=45, gdef=35, gres=35, glck=40, gcha=40), #Cai
            CharGrowth(id=3 , ghp=30, gstr=25, gmag=45, gspd=35, gdex=40, gdef=20, gres=40, glck=50, gcha=45), #Tialla
            CharGrowth(id=4 , ghp=40, gstr=35, gmag=20, gspd=45, gdex=60, gdef=30, gres=25, glck=35, gcha=30), #Peter
            CharGrowth(id=5 , ghp=45, gstr=40, gmag=40, gspd=35, gdex=40, gdef=35, gres=45, glck=55, gcha=50), #Ultand

            #Fiery Mane
            CharGrowth(id=6 , ghp=50, gstr=55, gmag=15, gspd=45, gdex=50, gdef=45, gres=20, glck=30, gcha=50), #Bertrand
            CharGrowth(id=7 , ghp=50, gstr=50, gmag=20, gspd=40, gdex=45, gdef=45, gres=25, glck=40, gcha=45), #Gaitz
            CharGrowth(id=8 , ghp=40, gstr=35, gmag=15, gspd=60, gdex=45, gdef=35, gres=25, glck=40, gcha=40), #Jester
            CharGrowth(id=9 , ghp=55, gstr=60, gmag=5 , gspd=15, gdex=30, gdef=50, gres=20, glck=35, gcha=20), #Goliath
            CharGrowth(id=10, ghp=30, gstr=30, gmag=45, gspd=40, gdex=40, gdef=20, gres=40, glck=45, gcha=30), #Dante

            #House Lamine
            CharGrowth(id=11, ghp=50, gstr=45, gmag=30, gspd=50, gdex=60, gdef=40, gres=30, glck=50, gcha=60), #Dietrich
            CharGrowth(id=12, ghp=40, gstr=25, gmag=50, gspd=35, gdex=40, gdef=30, gres=45, glck=35, gcha=30), #Fabio
            CharGrowth(id=13, ghp=55, gstr=55, gmag=20, gspd=35, gdex=35, gdef=45, gres=25, glck=35, gcha=30), #Esmeralda
            CharGrowth(id=14, ghp=50, gstr=45, gmag=30, gspd=40, gdex=35, gdef=40, gres=25, glck=30, gcha=40), #Mikaela

            #Linaria Dewdrops
            CharGrowth(id=15, ghp=30, gstr=60, gmag=45, gspd=10, gdex=20, gdef=60, gres=60, glck=20, gcha=60), #Cat
            CharGrowth(id=16, ghp=45, gstr=40, gmag=20, gspd=45, gdex=60, gdef=35, gres=20, glck=35, gcha=30), #Diego
            CharGrowth(id=17, ghp=35, gstr=35, gmag=35, gspd=55, gdex=40, gdef=30, gres=40, glck=30, gcha=30), #Loretta
            CharGrowth(id=18, ghp=45, gstr=45, gmag=30, gspd=40, gdex=45, gdef=40, gres=35, glck=30, gcha=50), #Seteth
            CharGrowth(id=19, ghp=45, gstr=45, gmag=35, gspd=35, gdex=45, gdef=35, gres=45, glck=50, gcha=40), #Ninae

            #Megaira's Beacon
            CharGrowth(id=20, ghp=70, gstr=50, gmag=30, gspd=40, gdex=40, gdef=40, gres=30, glck=30, gcha=50), #Theodora
            CharGrowth(id=21, ghp=35, gstr=35, gmag=45, gspd=40, gdex=50, gdef=30, gres=40, glck=35, gcha=40), #Bonaventure
            CharGrowth(id=22, ghp=55, gstr=60, gmag=15, gspd=25, gdex=30, gdef=45, gres=20, glck=40, gcha=35), #Tobias
            CharGrowth(id=23, ghp=35, gstr=35, gmag=30, gspd=40, gdex=55, gdef=30, gres=35, glck=50, gcha=25), #Lilian
            CharGrowth(id=24, ghp=45, gstr=40, gmag=25, gspd=50, gdex=35, gdef=40, gres=25, glck=30, gcha=30), #Lysander

            #Tale of the Moon
            CharGrowth(id=25, ghp=45, gstr=40, gmag=45, gspd=40, gdex=45, gdef=35, gres=40, glck=60, gcha=50), #Talimun
            CharGrowth(id=26, ghp=40, gstr=35, gmag=35, gspd=50, gdex=50, gdef=35, gres=30, glck=40, gcha=45), #Ursula
            CharGrowth(id=27, ghp=40, gstr=35, gmag=20, gspd=55, gdex=45, gdef=30, gres=20, glck=30, gcha=30), #Ludia
            CharGrowth(id=28, ghp=50, gstr=50, gmag=20, gspd=35, gdex=40, gdef=40, gres=25, glck=50, gcha=35), #Simon
            CharGrowth(id=29, ghp=30, gstr=35, gmag=55, gspd=30, gdex=40, gdef=20, gres=45, glck=25, gcha=40), #Fianna

            #Rose Tempest
            CharGrowth(id=30, ghp=40, gstr=35, gmag=35, gspd=65, gdex=50, gdef=30, gres=35, glck=25, gcha=55), #Leda
            CharGrowth(id=31, ghp=50, gstr=50, gmag=20, gspd=25, gdex=40, gdef=45, gres=20, glck=30, gcha=35), #Buccar
            CharGrowth(id=32, ghp=40, gstr=40, gmag=40, gspd=45, gdex=50, gdef=35, gres=35, glck=50, gcha=45), #Sirocco
            CharGrowth(id=33, ghp=35, gstr=35, gmag=50, gspd=35, gdex=35, gdef=30, gres=40, glck=40, gcha=40), #Olympia
            CharGrowth(id=34, ghp=30, gstr=30, gmag=5 , gspd=30, gdex=30, gdef=20, gres=10, glck=10, gcha=20), #Mu (without aptitude)

            #Pale Raven's Bridal Party
            CharGrowth(id=35, ghp=40, gstr=35, gmag=50, gspd=50, gdex=45, gdef=35, gres=40, glck=40, gcha=50), #Anatolia
            CharGrowth(id=36, ghp=35, gstr=30, gmag=45, gspd=35, gdex=50, gdef=30, gres=45, glck=35, gcha=40), #Sha Lan
            CharGrowth(id=37, ghp=45, gstr=45, gmag=25, gspd=45, gdex=50, gdef=35, gres=25, glck=30, gcha=25), #Nezha
            CharGrowth(id=38, ghp=50, gstr=55, gmag=20, gspd=30, gdex=35, gdef=45, gres=20, glck=25, gcha=30), #Dadao
            CharGrowth(id=39, ghp=35, gstr=35, gmag=30, gspd=45, gdex=60, gdef=30, gres=25, glck=40, gcha=35), #Halvin

            #Promised One's Army
            CharGrowth(id=40, ghp=40, gstr=30, gmag=45, gspd=45, gdex=45, gdef=30, gres=45, glck=30, gcha=40), #Hawk Tuah
            CharGrowth(id=41, ghp=40, gstr=45, gmag=45, gspd=50, gdex=40, gdef=30, gres=30, glck=30, gcha=30), #Troy

            #Others
            CharGrowth(id=42, ghp=45, gstr=45, gmag=20, gspd=50, gdex=45, gdef=35, gres=20, glck=45, gcha=30), #Guzran
            CharGrowth(id=43, ghp=50, gstr=30, gmag=40, gspd=35, gdex=35, gdef=30, gres=40, glck=40, gcha=25), #Yang Jie
            CharGrowth(id=44, ghp=45, gstr=40, gmag=25, gspd=35, gdex=45, gdef=40, gres=25, glck=35, gcha=35), #Io
            CharGrowth(id=45, ghp=30, gstr=30, gmag=25, gspd=60, gdex=45, gdef=30, gres=30, glck=45, gcha=30), #Peppe
            CharGrowth(id=46, ghp=50, gstr=45, gmag=20, gspd=45, gdex=40, gdef=40, gres=20, glck=35, gcha=30), #Noctula
            CharGrowth(id=47, ghp=35, gstr=30, gmag=45, gspd=30, gdex=40, gdef=25, gres=40, glck=30, gcha=40), #Sofia
            CharGrowth(id=48, ghp=35, gstr=35, gmag=35, gspd=55, gdex=50, gdef=30, gres=35, glck=40, gcha=45), #Catania
            CharGrowth(id=49, ghp=45, gstr=40, gmag=30, gspd=45, gdex=40, gdef=30, gres=25, glck=35, gcha=35), #Nydine
            CharGrowth(id=50, ghp=40, gstr=30, gmag=20, gspd=35, gdex=60, gdef=30, gres=25, glck=30, gcha=15), #Zarcone
            CharGrowth(id=51, ghp=65, gstr=50, gmag=15, gspd=20, gdex=30, gdef=40, gres=10, glck=25, gcha=5 ), #Majide
            CharGrowth(id=52, ghp=50, gstr=35, gmag=20, gspd=35, gdex=50, gdef=35, gres=25, glck=30, gcha=35), #Benditz
            CharGrowth(id=53, ghp=40, gstr=50, gmag=20, gspd=35, gdex=40, gdef=40, gres=30, glck=40, gcha=30), #Inyoni
            CharGrowth(id=54, ghp=50, gstr=40, gmag=20, gspd=30, gdex=45, gdef=45, gres=25, glck=40, gcha=45), #Jasmine
            CharGrowth(id=55, ghp=30, gstr=35, gmag=35, gspd=55, gdex=45, gdef=30, gres=40, glck=50, gcha=50), #Alexandra
            CharGrowth(id=56, ghp=50, gstr=50, gmag=15, gspd=55, gdex=45, gdef=20, gres=15, glck=25, gcha=35), #Nuzzuo
            CharGrowth(id=57, ghp=45, gstr=45, gmag=25, gspd=40, gdex=50, gdef=50, gres=30, glck=30, gcha=30), #Centurio
            CharGrowth(id=58, ghp=40, gstr=35, gmag=10, gspd=40, gdex=50, gdef=30, gres=15, glck=30, gcha=20), #Aswan
            CharGrowth(id=59, ghp=55, gstr=60, gmag=15, gspd=25, gdex=60, gdef=45, gres=15, glck=25, gcha=30), #Nathan
            CharGrowth(id=60, ghp=45, gstr=50, gmag=15, gspd=60, gdex=50, gdef=35, gres=20, glck=30, gcha=35), #Creek
            CharGrowth(id=61, ghp=55, gstr=40, gmag=15, gspd=55, gdex=50, gdef=30, gres=15, glck=30, gcha=25), #Kiroc
            CharGrowth(id=62, ghp=40, gstr=40, gmag=10, gspd=25, gdex=45, gdef=50, gres=15, glck=25, gcha=35), #Klapka
            CharGrowth(id=63, ghp=65, gstr=50, gmag=5 , gspd=20, gdex=40, gdef=45, gres=35, glck=20, gcha=40), #Tahonia
        ]

classes = [
            #Base
            GClass(name="Noble/Commoner", color='Base', skills=255),

            #Beginner
            GClass(name="Gladiator", tier='Beginner', color='Red', skills=149),
            GClass(name="Hunter", tier='Beginner', color='Yellow', skills=137),
            GClass(name="Soldier", tier='Beginner', color='Green', skills=647),
            GClass(name="Ornius Rider", tier='Beginner', color='Blue', skills=1287),
            GClass(name="Diviner", tier='Beginner', color='Purple', skills=245),

            #Specialty
            GClass(name="Myrmidon", tier='Specialty', color='Red', skills=131),
            GClass(name="Brigand", tier='Specialty', color='Red', skills=149),
            GClass(name="Pugilist", tier='Specialty', color='Red', skills=144),

            GClass(name="Archer", tier='Specialty', color='Yellow', skills=136),
            GClass(name="Rogue", tier='Specialty', color='Yellow', skills=137),

            GClass(name="Armored Knight", tier='Specialty', color='Green', skills=647),
            GClass(name="Light Cavalry", tier='Specialty', color='Green', skills=263),
            GClass(name="Charioteer", tier='Specialty', color='Green', skills=264),

            GClass(name="Armored Ornius Rider", tier='Specialty', color='Blue', skills=1287),
            GClass(name="Wing Soldier", tier='Specialty', color='Blue', skills=1027),

            GClass(name="Shaman", tier='Specialty', color='Purple', skills=241),
            GClass(name="Priest", tier='Specialty', color='Purple', skills=244),

            #Advanced
            GClass(name="Shido", tier='Advanced', color='Red', skills=131),
            GClass(name="Dancer", tier='Advanced', color='Red', skills=137),
            GClass(name="Warrior", tier='Advanced', color='Red', skills=149),
            GClass(name="Blacksmith", tier='Advanced', color='Red', skills=164),

            GClass(name="Sniper", tier='Advanced', color='Yellow', skills=136),
            GClass(name="Forest Knight", tier='Advanced', color='Yellow', skills=265),
            GClass(name="Ranger", tier='Advanced', color='Yellow', skills=137),

            GClass(name="Guardian", tier='Advanced', color='Green', skills=194),
            GClass(name="Dreadnought", tier='Advanced', color='Green', skills=646),
            GClass(name="Bardinger", tier='Advanced', color='Green', skills=263),
            GClass(name="Cataphract", tier='Advanced', color='Green', skills=775),
            GClass(name="Elephant Rider", tier='Advanced', color='Green', skills=263),

            GClass(name="Caladrius", tier='Advanced', color='Blue', skills=1319),
            GClass(name="Dragoon", tier='Advanced', color='Blue', skills=1031),

            GClass(name="Ovate", tier='Advanced', color='Purple', skills=241),
            GClass(name="Bishop", tier='Advanced', color='Purple', skills=244),
            GClass(name="Troubadour", tier='Advanced', color='Purple', skills=352),

            #Master
            GClass(name="Swordmaster", tier='Master', color='Red', skills=131),
            GClass(name="High Savant", tier='Master', color='Red', skills=289),
            GClass(name="Battlemaster", tier='Master', color='Red', skills=149),
            GClass(name="War Monk", tier='Master', color='Red', skills=208),

            GClass(name="Bow Adept", tier='Master', color='Yellow', skills=136),
            GClass(name="Bow Knight", tier='Master', color='Yellow', skills=265),
            GClass(name="Shadow Seeker", tier='Master', color='Yellow', skills=137),

            GClass(name="Sentinel", tier='Master', color='Green', skills=194),
            GClass(name="Castle Knight", tier='Master', color='Green', skills=646),
            GClass(name="Orichaldia", tier='Master', color='Green', skills=263),
            GClass(name="Great Knight", tier='Master', color='Green', skills=775),

            GClass(name="Celestial Trooper", tier='Master', color='Blue', skills=1027),
            GClass(name="Bau Lord", tier='Master', color='Blue', skills=1031),

            GClass(name="Druid", tier='Master', color='Purple', skills=177),
            GClass(name="Wiseman", tier='Master', color='Purple', skills=212),
            GClass(name="Valkyrium", tier='Master', color='Purple', skills=352),

            #Divine
            GClass(name="The Blade", tier='Divine', color='Red', skills=131),
            GClass(name="The Apsara", tier='Divine', color='Red', skills=137),
            GClass(name="The Eternal", tier='Divine', color='Red', skills=149),
            GClass(name="The Godhand", tier='Divine', color='Red', skills=208),

            GClass(name="The Calamity", tier='Divine', color='Yellow', skills=137),

            GClass(name="The Trident", tier='Divine', color='Green', skills=194),
            GClass(name="The Cavalier", tier='Divine', color='Green', skills=263),

            GClass(name="The Avatar", tier='Divine', color='Purple', skills=245),
        ]

class_growths = [
            GClassGrowth(id=1), #Noble/Commoner

            #Beginner
            GClassGrowth(id=2 , ghp=10, gstr=10), #Gladiator
            GClassGrowth(id=3 , ghp=10, gspd=10, gdex=10), #Hunter
            GClassGrowth(id=4 , ghp=10, gstr=5, gspd=-5, gdex=5, gdef=10), #Soldier
            GClassGrowth(id=5 , ghp=10, gspd=10, gres=5, glck=5), #Ornius Rider
            GClassGrowth(id=6 , ghp=5, gstr=-5, gmag=15, gdex=5, gdef=-5, gres=10), #Diviner

            #Specialty
            GClassGrowth(id=7 , ghp=10, gspd=15, gdex=10, glck=5, gcha=5), #Myrmidon
            GClassGrowth(id=8 , ghp=15, gstr=15, gmag=-5, gspd=5, gdef=5, gcha=5), #Brigand
            GClassGrowth(id=9 , ghp=15, gstr=10, gmag=-5, gspd=10, gdex=5, gdef=10, gcha=5), #Pugilist

            GClassGrowth(id=10, ghp=10, gspd=10, gdex=15, gdef=5, glck=5, gcha=5), #Archer
            GClassGrowth(id=11, ghp=10, gspd=15, gdex=10, gres=5, glck=5), #Rogue

            GClassGrowth(id=12, ghp=10, gstr=10, gmag=-5, gspd=-5, gdex=5, gdef=25, gres=-5, gcha=5), #Armored Knight
            GClassGrowth(id=13, ghp=10, gstr=5, gmag=-5, gspd=5, gdef=5, glck=5, gcha=10), #Light Cavalry
            GClassGrowth(id=14, ghp=10, gstr=5, gmag=-5, gspd=-5, gdex=15, gdef=10, glck=5, gcha=10), #Charioteer

            GClassGrowth(id=15, ghp=10, gmag=-5, gspd=10, gdex=5, gdef=10, glck=5, gcha=5), #Armored Ornius Rider
            GClassGrowth(id=16, ghp=10, gmag=5, gdex=5, gdef=5, gres=5, glck=5, gcha=10), #Wing Soldier

            GClassGrowth(id=17, ghp=5, gstr=-5, gmag=15, gspd=10, gdex=10, gdef=-10, gres=10, glck=10), #Shaman
            GClassGrowth(id=18, ghp=5, gstr=-5, gmag=10, gspd=5, gdex=5, gdef=-10, gres=15, glck=15, gcha=10), #Priest

            #Advanced
            GClassGrowth(id=19, ghp=10, gstr=5, gspd=15, gdex=10, gres=-5, glck=5, gcha=5), #Shido
            GClassGrowth(id=20, ghp=15, gstr=5, gspd=25, gdex=10, gres=5, glck=10, gcha=20), #Dancer
            GClassGrowth(id=21, ghp=20, gstr=20, gmag=-5, gdef=5, gres=-5, gcha=5), #Warrior
            GClassGrowth(id=22, ghp=15, gstr=10, gmag=10, gdex=5, gdef=10, gres=10, gcha=5), #Blacksmith

            GClassGrowth(id=23, ghp=10, gstr=5, gspd=10, gdex=20, gdef=5, gres=5, glck=5, gcha=5), #Sniper
            GClassGrowth(id=24, ghp=10, gstr=5, gspd=10, gdex=10, gdef=5, gres=5, glck=5, gcha=5), #Forest Knight
            GClassGrowth(id=25, ghp=10, gstr=5, gspd=15, gdex=15, gres=10, glck=15), #Ranger

            GClassGrowth(id=26, ghp=10, gstr=10, gdex=5, gdef=10, gres=15, glck=5, gcha=5), #Guardian
            GClassGrowth(id=27, ghp=15, gstr=15, gmag=-5, gspd=-10, gdex=5, gdef=30, gres=-10, gcha=5), #Dreadnought
            GClassGrowth(id=28, ghp=10, gstr=10, gmag=-5, gdef=5, gres=10, glck=5, gcha=10), #Bardinger
            GClassGrowth(id=29, ghp=15, gstr=15, gmag=-5, gspd=-10, gdef=10, gres=-5, gcha=5), #Cataphract
            GClassGrowth(id=30, ghp=20, gstr=10, gmag=-5, gspd=-10, gdex=20, gdef=15, gres=-5, glck=5, gcha=10), #Elephant Rider

            GClassGrowth(id=31, ghp=15, gmag=10, gspd=10, gdex=5, gdef=10, gres=10, glck=5, gcha=5), #Caladrius
            GClassGrowth(id=32, ghp=15, gstr=5, gspd=5, gdef=10, gres=10, glck=10, gcha=5), #Dragooner

            GClassGrowth(id=33, ghp=10, gstr=-5, gmag=20, gspd=-5, gdex=15, gdef=-10, gres=15, glck=10), #Ovate
            GClassGrowth(id=34, ghp=10, gstr=-5, gmag=15, gdex=5, gdef=-10, gres=20, glck=20, gcha=10), #Bishop
            GClassGrowth(id=35, ghp=10, gmag=15, gdex=5, gdef=5, gres=15, glck=15, gcha=10), #Troubadour

            #Master
            GClassGrowth(id=36, ghp=15, gstr=10, gspd=20, gdex=15, glck=5, gcha=5), #Swordmaster
            GClassGrowth(id=37, ghp=10, gstr=15, gmag=15, gspd=10, gdex=5, gdef=5, gres=5, glck=5, gcha=5), #High Savant
            GClassGrowth(id=38, ghp=25, gstr=25, gmag=-5, gspd=5, gdex=-5, gdef=10, gres=-5, glck=-5, gcha=5), #Battlemaster
            GClassGrowth(id=39, ghp=15, gstr=10, gspd=15, gdef=5, gres=15, glck=5, gcha=5), #War Monk

            GClassGrowth(id=40, ghp=15, gstr=5, gspd=15, gdex=20, gdef=5, gres=5, glck=5, gcha=5), #Bow Adept
            GClassGrowth(id=41, ghp=10, gstr=10, gspd=15, gdex=10, gdef=5, glck=5, gcha=5), #Bow Knight
            GClassGrowth(id=42, ghp=15, gstr=5, gspd=25, gdex=15, gres=10, glck=15), #Shadow Seeker

            GClassGrowth(id=43, ghp=15, gstr=15, gspd=5, gdex=5, gdef=10, gres=15, glck=5, gcha=5), #Sentinel
            GClassGrowth(id=44, ghp=25, gstr=20, gmag=-5, gspd=-15, gdex=5, gdef=30, gres=-10, gcha=5), #Castle Knight
            GClassGrowth(id=45, ghp=15, gstr=15, gmag=-5, gspd=5, gdef=5, gres=5, glck=5, gcha=10), #Orichaldia
            GClassGrowth(id=46, ghp=20, gstr=20, gmag=-5, gspd=-10, gdef=15, gres=-10, gcha=5), #Great Knight

            GClassGrowth(id=47, ghp=15, gstr=5, gmag=-5, gspd=10, gdex=5, gdef=5, gres=15, glck=15, gcha=10), #Celestial Trooper
            GClassGrowth(id=48, ghp=15, gstr=5, gspd=5, gdef=10, gres=10, glck=10, gcha=5), #Bau Lord

            GClassGrowth(id=49, ghp=10, gstr=-5, gmag=30, gspd=10, gdex=15, gdef=-10, gres=20, glck=10), #Druid
            GClassGrowth(id=50, ghp=10, gstr=-5, gmag=20, gspd=5, gdef=-10, gres=25, glck=20, gcha=10), #Wiseman
            GClassGrowth(id=51, ghp=10, gmag=15, gspd=5, gdex=5, gdef=5, gres=10, glck=15, gcha=10), #Valkyrium

            #Divine
            GClassGrowth(id=52, ghp=15, gstr=10, gmag=10, gspd=20, gdex=20, gdef=5, gres=5, glck=5, gcha=10), #The Blade
            GClassGrowth(id=53, ghp=15, gstr=5, gmag=10, gspd=25, gdex=15, gdef=5, gres=5, glck=10, gcha=30), #The Apsara
            GClassGrowth(id=54, ghp=30, gstr=30, gspd=10, gdef=15, gcha=10), #The Eternal
            GClassGrowth(id=55, ghp=15, gstr=10, gmag=10, gspd=15, gdex=5, gdef=10, gres=15, glck=5, gcha=10), #The Godhand

            GClassGrowth(id=56, ghp=15, gstr=5, gmag=15, gspd=25, gdex=20, gdef=5, gres=15, glck=15, gcha=5), #The Calamity

            GClassGrowth(id=57, ghp=15, gstr=15, gmag=5, gspd=10, gdex=10, gdef=15, gres=15, glck=5, gcha=10), #The Trident
            GClassGrowth(id=58, ghp=20, gstr=15, gmag=5, gspd=10, gdex=10, gdef=15, gres=10, glck=5, gcha=15), #The Cavalier

            GClassGrowth(id=59, ghp=10, gstr=-5, gmag=30, gspd=10, gdex=5, gdef=-5, gres=30, glck=20, gcha=10), #The Avatar
        ]