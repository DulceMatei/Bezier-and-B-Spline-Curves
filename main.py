from PySide6.QtWidgets import QApplication
from Calcul_Numeric import MyMainWindow

import sys

# pornirea aplicatiei

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec()) 