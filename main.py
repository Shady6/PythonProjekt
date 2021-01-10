from tkinter import *
from volume_converter import VolumeConverter
from interface import AddConversionPanel

window = Tk()
window.geometry("600x400")

# pozmieniać convertery
AddConversionPanel(window, "Długości", VolumeConverter())
AddConversionPanel(window, "Wagi", VolumeConverter())
AddConversionPanel(window, "Objętości", VolumeConverter())

window.mainloop()