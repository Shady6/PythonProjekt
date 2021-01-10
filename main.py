from tkinter import *
from volume_converter import VolumeConverter
from weight_converter import WeightConverter
from length_converter import LengthConverter
from interface import AddConversionPanel

window = Tk()
window.geometry("600x400")

# pozmieniać convertery
AddConversionPanel(window, "Długości", VolumeConverter())
AddConversionPanel(window, "Wagi", WeightConverter())
AddConversionPanel(window, "Objętości", LengthConverter())

window.mainloop()