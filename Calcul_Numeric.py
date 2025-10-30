from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QMessageBox
from PySide6.QtGui import QIcon
from ui_Calcul_Numeric import Ui_MainWindow
from bezier_animation import BezierAnimation
from bspline_animation import BSplineAnimation

class MyMainWindow(QMainWindow):
    def __init__(self): # initializare
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Grafica pe calculator") # titlul aplicatiei

        self.points = []

        self.ui.SecondTable.setVisible(False)
        # inceput functii pentru butoane
        self.ui.Bezier_Button1.clicked.connect(self.switch_to_Bezier_Page)
        self.ui.Bezier_Button2.clicked.connect(self.switch_to_Bezier_Page)

        self.ui.Bspline_Button1.clicked.connect(self.switch_to_Bspline_Page)
        self.ui.Bspline_Button2.clicked.connect(self.switch_to_Bspline_Page)

        self.ui.Home_Button1.clicked.connect(self.switch_to_Home_Page)
        self.ui.Home_Button2.clicked.connect(self.switch_to_Home_Page)

        self.ui.Add_Button3.clicked.connect(self.add_point)
        self.ui.Reset_Button3.clicked.connect(self.reset_points)

        self.ui.Reset_Button2.clicked.connect(self.reset_points)
        self.ui.Import_Button2.clicked.connect(self.open_file_dialog)

        self.bezier_animation = BezierAnimation(self.ui)
        self.ui.Draw_Button2.clicked.connect(self.bezier_animation.animate)

        self.bspline_animation = BSplineAnimation(self.ui)
        self.ui.Draw_Button3.clicked.connect(self.bspline_animation.animate)
        # sfarsit functie pentru butoane

        self.switch_to_Home_Page()
        self.set_app_icon()
        self.ui.ComboBox.currentIndexChanged.connect(self.select_animation_method)

    def switch_to_Home_Page(self):
        print("Switching to Home Page")
        self.ui.stackedWidget.setCurrentIndex(0) # pagina home

    def switch_to_Bezier_Page(self):
        print("Switching to Bezier Page")
        self.ui.stackedWidget.setCurrentIndex(1) # pagina bezier 
        print("Current Index:", self.ui.stackedWidget.currentIndex())

    def switch_to_Bspline_Page(self):
        print("Switching to Bspline Page")
        self.ui.stackedWidget.setCurrentIndex(2) # pagina b-spline
        print("Current Index:", self.ui.stackedWidget.currentIndex())

    def set_app_icon(self):
        app_icon = QIcon(":/icons/ovidius_icon.png") # iconita colt stanga sus
        self.setWindowIcon(app_icon)

    def open_file_dialog(self): # selectarea fisierului cu pathu lui
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Selectati fisierul", "", "Toate fisierele (*.*)") # selectarea fisierului
        print("Calea fisierului selectat:", file_path)
        if file_path:
            self.read_points_from_file(file_path)
            if hasattr(self, 'bezier_animation'):
                self.bezier_animation.points = self.points

    def add_point(self): # adaugarea punctelor
        try:
            x, y = map(float, self.ui.Text_Button3.text().split(',')) # separa x si y la fiecare virgula
            self.points.append((x, y)) # adaugam punctele din fisier in vectorul nostru self.points
            self.ui.Text_Button3.clear()
            self.update_labels()
            self.bezier_animation.points = self.points # copiem punctele in bezier_animation
            self.bspline_animation.points = self.points # copiem punctele in bspline_animation
        except ValueError:
            QMessageBox.critical(self, "Eroare", "Format invalid. Te rog foloseste formatul 'x,y'.") # exceptie

    def reset_points(self): # stergem toate punctele si actualizam label-urile
        self.points.clear() 
        self.bezier_animation.reset()
        self.bspline_animation.reset()
        self.update_labels()

    def read_points_from_file(self, file_path): # citirea coordonatelor din fisier
        self.points.clear() # stergem punctele
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    x, y = map(float, line.strip().split(',')) # separa x si y la fiecare virgula
                    self.points.append((x, y)) # adaugam punctele din fisier in vectorul nostru self.points
            self.update_labels() # actualizam label-urile cu coordonatele
            self.bezier_animation.points = self.points # copiem punctele in bezier_animation
            self.bspline_animation.points = self.points # copiem punctele in bspline_animation
        except Exception as e:
            QMessageBox.critical(self, "Eroare", f"Citirea fisierului a esuat: {e}") # exceptie

    def select_animation_method(self, index):
        method_name = self.ui.ComboBox.currentText()
        print(f"Metoda animatiei: {method_name}")
        # selectam curba bezier de animat
        if method_name == "Cubic":
            self.current_animation = self.bezier_animation.bezier_cubic
        elif method_name == "General":
            self.current_animation = self.bezier_animation.bezier_general
        elif method_name == "Quadratic":
            self.current_animation = self.bezier_animation.bezier_quadratic

            if self.current_animation is not None:
                self.current_animation.animate(method_name.lower())
            else:
                QMessageBox.critical(self, "Eroare", "Metoda de animatie selectata nu este valida.")

    def update_labels(self): # functie de afisare a coordonatelor selectate
        coord_text = '\n'.join([f"({x}, {y})" for x, y in self.points])
        self.ui.Coordonate2.setText(coord_text)
        self.ui.Coordonate3.setText(coord_text)

    def draw(self): # animatie pentru bezier
        if self.current_animation is not None:
            self.current_animation.animate()
 
    def switch_to_Home_Page(self): # intoarcere la home page
        print("Switching to Home Page")
        self.ui.stackedWidget.setCurrentIndex(0)

    def set_app_icon(self): # iconita
        app_icon = QIcon(":/icons/ovidius_icon.png")
        self.setWindowIcon(app_icon)