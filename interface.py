from tkinter import *
from conversionDirection import changeConversionDirectionText, isMetric
# from countResult import CalculateConversion
from volume_converter import VolumeConverter

# milimetry, centymetry, metry, kilometry
# cal, stopa, jard, pręt, łańcuch, furlong, mila

window = Tk()

metricLabel = Label(text="Wybierz jednostkę metryczną")
metricLabel.pack()

metricOptionsList = VolumeConverter.metricUnitNames
metricValue = StringVar(window)
metricValue.set(VolumeConverter.metricUnitNames[0])
metricDropDown = OptionMenu(window, metricValue, *metricOptionsList)
metricDropDown.pack()

imperialLabel = Label(text="Wybierz jednostkę imperialną")
imperialLabel.pack()

imperialOptionsList = VolumeConverter.imperialUnitNames
imperialValue = StringVar(window)
imperialValue.set(VolumeConverter.imperialUnitNames[0])
ImperialDropDown = OptionMenu(window, imperialValue, *imperialOptionsList)
ImperialDropDown.pack()

conversionDirection = Label(text="metryczne -> imperialne")
conversionDirection.pack()   

conversionDirectionButton = Button(window, text="Zmień kierunek konwersji", command=lambda: changeConversionDirectionText(conversionDirection))
conversionDirectionButton.pack()

valueLabel = Label(text="Podaj wartość")
valueLabel.pack()

valueText = StringVar()
valueTextBox = Entry(textvariable=valueText)
valueTextBox.pack()

volumeConverter = VolumeConverter()
calculateButton = Button(window, text="Oblicz", command=lambda: volumeConverter.ConvertAndFillResultLabel(isMetric(conversionDirection), metricValue.get(), imperialValue.get(), valueText.get(), resultValueLabel))
calculateButton.pack()

resultLabel = Label(text="Wynik")
resultLabel.pack()

resultValueLabel = Label(text="")
resultValueLabel.pack()

window.mainloop()




