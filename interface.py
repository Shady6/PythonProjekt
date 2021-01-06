from tkinter import *
from conversionDirection import changeConversionDirectionText, isMetric
from countResult import CalculateConversion

# milimetry, centymetry, metry, kilometry
# cal, stopa, jard, pręt, łańcuch, furlong, mila

window = Tk()

metricLabel = Label(text="Wybierz jednostkę metryczną")
metricLabel.pack()

metricValue = StringVar(window)
metricValue.set("metr")
metricDropDown = OptionMenu(window, metricValue, "milimetr", "centymetr", "metr", "kilometr")
metricDropDown.pack()

imperialLabel = Label(text="Wybierz jednostkę imperialną")
imperialLabel.pack()

imperialValue = StringVar(window)
imperialValue.set("mila")
ImperialDropDown = OptionMenu(window, imperialValue, "cal", "stopa", "jard", "pręt", "łańcuch", "furlong", "mila")
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

calculateButton = Button(window, text="Oblicz", command=lambda: CalculateConversion(metricValue.get(), imperialValue.get(), isMetric(conversionDirection), valueText.get(), resultValueLabel))
calculateButton.pack()

resultLabel = Label(text="Wynik")
resultLabel.pack()

resultValueLabel = Label(text="")
resultValueLabel.pack()

window.mainloop()




