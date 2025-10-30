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
        self.ui.GraphicView4.setLayout(self.layout)
        self.layout.addWidget(self.canvas)

    def bezier(self, t, points): # metoda de calcul bezier cuadratica
        if len(points) != 3:
            raise ValueError("Ai nevoie de exact 3 puncte pentru o curba Bezier cuadratica.")
        x = (1 - t)**2 * points[0][0] + 2 * (1 - t) * t * points[1][0] + t**2 * points[2][0]
        y = (1 - t)**2 * points[0][1] + 2 * (1 - t) * t * points[1][1] + t**2 * points[2][1]
        return x, y

    def animate(self):
        if len(self.points) != 3:
            QMessageBox.critical(self.ui.centralwidget, "Eroare", "Ai nevoie de exact 3 puncte pentru o curba Bezier cuadratica.") # exceptie pentru numarul gresit de puncte
            return

        t_values = np.linspace(0, 1, 100)
        bezier_points = np.array([self.bezier(t, self.points) for t in t_values]) # initializare puncte bezier

        self.ax.clear()
        self.ax.scatter([p[0] for p in self.points], [p[1] for p in self.points], color='red', label='Puncte de Control')
        self.ax.legend()

        def update(frame): # animatie
            self.ax.clear()  # clear la axa la fiecare frame
            self.ax.scatter([p[0] for p in self.points], [p[1] for p in self.points], color='red', label='Puncte de Control')
            self.ax.plot(bezier_points[:frame, 0], bezier_points[:frame, 1], 'b-')
            self.ax.legend() # legenda
            self.canvas.draw() # desenare pe canva

        animation = FuncAnimation(self.fig, update, frames=len(t_values), interval=15, repeat=False)
        self.canvas.draw()

    def reset(self): # resetare
        self.points.clear()
        self.ax.clear()
        self.canvas.draw()