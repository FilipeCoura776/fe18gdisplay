import os
from PySide6.QtWidgets import QMainWindow, QApplication
from assets.ui.interface import Ui_MainWindow
from src.controllers.db_func import DBController
import src.controllers.calculations as calc
from PySide6.QtCore import QTimer
from src.views.radar_chart import RadarChartWidget
from src.views.effects import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dbcontroller = DBController()

        # combobox items loading
        self.load_chars()
        self.load_gclasses()

        # function connection to comboboxes
        self.ui.cbbChar.currentIndexChanged.connect(self.select_char)
        self.ui.cbbClass.currentIndexChanged.connect(self.select_gclass)

        # radar graph
        self.radar_widget = RadarChartWidget(self.ui.radar_teste)


        StyleHelper.apply_glow(self.ui.lblName, color="#ffcc00", blur_radius=15)
        StyleHelper.apply_glow(self.ui.lblTitle, color="#ffcc00", blur_radius=15)



    gclass_colors = {
        "Base": "#4d2403",
        "Red": "#ff0000",
        "Yellow": "#fffb00",
        "Green": "#00ff00",
        "Blue": "#0011ff",
        "Purple": "#ae00ff"
    }

    # area de funcoes ----------------------------------------------------------------------------------------------------

    #carregar personagens na combobox
    def load_chars(self):
        self.ui.cbbChar.clear()

        chars = self.dbcontroller.load_characters()

        for char in chars:
            self.ui.cbbChar.addItem(char.name, char.id) #addItem(texto, valor)

    #carregar classes na combobox
    def load_gclasses(self):
        self.ui.cbbClass.clear()

        gclasses = self.dbcontroller.load_gclasses()

        for gclass in gclasses:
            self.ui.cbbClass.addItem(gclass.name, gclass.id)

    def select_char(self):
        char_id = self.ui.cbbChar.currentData()

        if char_id is not None:
            char = self.dbcontroller.get_character(char_id)

            if char:
                self.ui.lblName.setText(char.name)
                self.ui.lblTitle.setText(char.title)

                self.ui.wdgPortrait.setStyleSheet(f"""
                    image: url(:/portraits/{char.name.replace(" ", "_")}.png);
                    border:0px;
                """)

                self.get_calcs(char_id, self.ui.cbbClass.currentData())

                if not calc.get_gclass_restrictions(char, self.ui.cbbClass.currentData()):
                    #print("INDISPONIVEL")
                    self.ui.wdgClassCheck.setVisible(True)
                else:
                    self.ui.wdgClassCheck.setVisible(False)

    def select_gclass(self):
        gclass_id = self.ui.cbbClass.currentData()

        if gclass_id is not None:
            gclass = self.dbcontroller.get_gclass(gclass_id)

            if gclass:
                self.ui.lblClass.setText(gclass.name)
                self.ui.lblTier.setText(gclass.tier.value)
                self.get_calcs(self.ui.cbbChar.currentData(), gclass_id)

                self.load_icons(calc.get_ranks(gclass.skills))
                
                StyleHelper.apply_glow(self.ui.lblClass, color=self.gclass_colors[gclass.color.name], blur_radius=15)

                if not calc.get_gclass_restrictions(self.dbcontroller.get_character(self.ui.cbbChar.currentData()), self.ui.cbbClass.currentData()):
                    self.ui.wdgClassCheck.setVisible(True)
                else:
                    self.ui.wdgClassCheck.setVisible(False)

    def load_icons(self, ranks: list):
        #icon (widget) list
        icons = [self.ui.icon1, self.ui.icon2, self.ui.icon3, self.ui.icon4, self.ui.icon5, self.ui.icon6, self.ui.icon7, self.ui.icon8]

        for i in range(8):
            if len(ranks) > i:
                icons[i].setStyleSheet(f"""
                image: url(:/icons/{ranks[i]}.png);
                background-color: rgb(21, 40, 46);
                """)
            else:
                icons[i].setStyleSheet(f"""
                image: url(:/icons/void.png);
                background-color: rgb(21, 40, 46);
                """)
            

    '''
    def char_change(self):
            self.debounce_timer_char.start()

    def gclass_change(self):
        self.debounce_timer_gclass.start()
    '''

    def get_calcs(self, char_id, gclass_id):
        growth_list = calc.calculate_growths(self.dbcontroller, char_id, gclass_id)

        lbl_list = [
            self.ui.lblHpGr,
            self.ui.lblStrGr,
            self.ui.lblMagGr,
            self.ui.lblSpdGr,
            self.ui.lblDexGr,
            self.ui.lblDefGr,
            self.ui.lblResGr,
            self.ui.lblLckGr,
            self.ui.lblChaGr
        ]

        total = 0
        s = []

        for i in range(9):
            lbl_list[i].setText(str(growth_list[i]))
            s.append(growth_list[i])
            total += growth_list[i]

        self.ui.lblTotalGr.setText(str(total))

        labels_atributos = ['Mag', 'Str', 'Def', 'Res', 'Lck', 'Cha', 'Dex', 'Spd']
        valores_personagem = [s[2], s[1], s[5], s[6], s[7], s[8], s[4], s[3]]
        self.radar_widget.plot_stats(labels_atributos, valores_personagem)
        
    #---------------------------------------------------------------------------------------------------------------------

    def closeEvent(self, event):
        self.dbcontroller.close()
        event.accept()
