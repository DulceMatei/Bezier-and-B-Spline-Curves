import numpy as np
from scipy import interpolate
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QVBoxLayout, QMessageBox
import matplotlib.pyplot as plt

class BSplineAnimation:
    def __init__(self, ui): # initializare graf si puncte
        self.ui = ui
        self.points = []
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.layout = QVBoxLayout(self.ui.GraphicView3)
        self.ui.GraphicView3.setLayout(self.layout)
        self.layout.addWidget(self.canvas)

    def animate(self):
        if len(self.points) < 4:
            QMessageBox.critical(self.ui.centralwidget, "Eroare", "Ai nevoie de 4 puncte pentru o curba B-Spline.") # exceptie pentru prea putine puncte
            return

        x = np.array([point[0] for point in self.points]) # asignam x
        y = np.array([point[1] for point in self.points]) # asignam y

        tck, u = interpolate.splprep([x, y], k=3, s=0) # metoda calcul b-spline pentru tip cubic // s = 0 => curba care trece prin toate punctele de control, daca s era mai mare curba era mai neteda
 
        def update(frame): # animatie
            u_new = np.linspace(u.min(), frame, 10)
            out = interpolate.splev(u_new, tck)
            self.ax.clear()
            self.ax.scatter(x, y, color='red', label='Puncte de Control')
            self.ax.plot(out[0], out[1], 'b-', label='Curba B-Spline')
            self.ax.legend()
            self.canvas.draw() # desenare pe canva

        animation = FuncAnimation(self.fig, update, frames=np.linspace(u.min(), u.max(), 45), interval=20, repeat=False)
        self.canvas.draw()

    def reset(self): # resetare
        self.points.clear()
        self.ax.clear()
        self.canvas.draw()