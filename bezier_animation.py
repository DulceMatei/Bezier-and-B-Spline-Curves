import numpy as np
import math
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QVBoxLayout, QMessageBox
import matplotlib.pyplot as plt

class BezierAnimation:
    def __init__(self, ui): # initializare graf si puncte
        self.ui = ui
        self.points = []
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.layout = QVBoxLayout()
        self.ui.GraphicView2.setLayout(self.layout)
        self.layout.addWidget(self.canvas)
        self.comboBox = ui.ComboBox
        

    def bezier_quadratic(self, t, points): # metoda de calcul pentru bezier cuadratic
        if len(points) != 3:
            raise ValueError("Ai nevoie de exact 3 puncte pentru o curbă Bezier cvadratică.")
        x = (1 - t)**2 * points[0][0] + 2 * (1 - t) * t * points[1][0] + t**2 * points[2][0]
        y = (1 - t)**2 * points[0][1] + 2 * (1 - t) * t * points[1][1] + t**2 * points[2][1]
        return x, y

    def bezier_cubic(self, t, points): # metoda de calcul pentru bezier cubic
        if len(points) != 4:
            raise ValueError("Ai nevoie de exact 4 puncte pentru o curbă Bezier cubică.")
        x = (1 - t)**3 * points[0][0] + 3 * (1 - t)**2 * t * points[1][0] + 3 * (1 - t) * t**2 * points[2][0] + t**3 * points[3][0]
        y = (1 - t)**3 * points[0][1] + 3 * (1 - t)**2 * t * points[1][1] + 3 * (1 - t) * t**2 * points[2][1] + t**3 * points[3][1]
        return x, y

    def bezier_general(self, t, points): # metoda de calcul pentru bezier general
        n = len(points) - 1
        x = sum(math.comb(n, k) * (1 - t)**(n - k) * t**k * points[k][0] for k in range(n + 1))
        y = sum(math.comb(n, k) * (1 - t)**(n - k) * t**k * points[k][1] for k in range(n + 1))
        return x, y

    def animate(self): # animatie pentru bezier
        bezier_type = self.comboBox.currentText().lower()  # converteste tipul de curba in litere mici
        if bezier_type not in ["cuadratic", "cubic", "general"]:
            QMessageBox.critical(self.ui.centralwidget, "Eroare", "Tipul de curba Bezier este invalid.")
            return
        # verificarea combo boxului cu tipul de curba bezier
        if bezier_type == "cuadratic" and len(self.points) != 3:
            QMessageBox.critical(self.ui.centralwidget, "Eroare", "Ai nevoie de exact 3 puncte pentru o curba Bezier cuadratica.") 
            return
        elif bezier_type == "cubic" and len(self.points) != 4:
            QMessageBox.critical(self.ui.centralwidget, "Eroare", "Ai nevoie de exact 4 puncte pentru o curba Bezier cubica.")
            return
        elif bezier_type == "general" and len(self.points) < 2:
            QMessageBox.critical(self.ui.centralwidget, "Eroare", "Ai nevoie de minim 2 puncte pentru o curba Bezier generala.")
            return

        t_values = np.linspace(0, 1, 100) 
        bezier_func = None # initializam functia bezier

        if bezier_type == "cuadratic":
            bezier_func = self.bezier_quadratic
        elif bezier_type == "cubic":
            bezier_func = self.bezier_cubic
        elif bezier_type == "general":
            bezier_func = self.bezier_general

        bezier_points = np.array([bezier_func(t, self.points) for t in t_values]) 

        def update(frame): # animatie
            self.ax.clear()  # curatare axa la fiecare frame
            self.ax.scatter([p[0] for p in self.points], [p[1] for p in self.points], color='red', label='Puncte de Control')
            self.ax.plot(bezier_points[:frame, 0], bezier_points[:frame, 1], 'b-')
            self.ax.legend() # legenda
            self.canvas.draw() # desenare pe canva

        animation = FuncAnimation(self.fig, update, frames=len(t_values), interval=15, repeat=False)
        self.canvas.draw() # desenare

    def reset(self): # resetare
        self.points.clear()
        self.ax.clear()
        self.canvas.draw()
