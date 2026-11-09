import sys
from PySide6.QtWidgets import QApplication
from src.database.connection import init_db
#from src.views.carregar_view import MainView
from src.views import main_view

if __name__ == "__main__":

    #create and fill database
    init_db()

    #opens pyside6 interface
    app = QApplication(sys.argv)

    window = main_view.MainWindow()
    window.show()

    print("app initiated")

    window.select_char()
    window.select_gclass()

    sys.exit(app.exec())