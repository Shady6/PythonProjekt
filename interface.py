from tkinter import *
from conversion_direction import changeConversionDirectionText, isMetric
from volume_converter import VolumeConverter


def AddConversionPanel(window, unitName, converter):

    frame = Frame(window)        
    frame.pack(side="left", expand=True)

    unitLabel = Label(frame, text=f"Konwersja {unitName}")
    unitLabel.pack()

    metricLabel = Label(frame, text="Wybierz jednostkę metryczną")
    metricLabel.pack()

    metricOptionsList = converter.metricUnitNames
    metricValue = StringVar(frame)
    metricValue.set(converter.metricUnitNames[0])
    metricDropDown = OptionMenu(frame, metricValue, *metricOptionsList)
    metricDropDown.pack()

    imperialLabel = Label(frame, text="Wybierz jednostkę imperialną")
    imperialLabel.pack()

    imperialOptionsList = converter.imperialUnitNames
    imperialValue = StringVar(frame)
    imperialValue.set(converter.imperialUnitNames[0])
    ImperialDropDown = OptionMenu(frame, imperialValue, *imperialOptionsList)
    ImperialDropDown.pack()

    conversionDirection = Label(frame, text="metryczne -> imperialne")
    conversionDirection.pack()

    conversionDirectionButton = Button(frame, text="Zmień kierunek konwersji",
                                    command=lambda: changeConversionDirectionText(conversionDirection))
    conversionDirectionButton.pack()

    valueLabel = Label(frame, text="Podaj wartość")
    valueLabel.pack()

    valueText = StringVar()
    valueTextBox = Entry(frame, textvariable=valueText)
    valueTextBox.pack()

    volumeConverter = VolumeConverter()
    calculateButton = Button(frame, text="Oblicz", command=lambda:
                            converter.ConvertAndFillResultLabel(isMetric(conversionDirection),
                                                                    metricValue.get(),
                                                                    imperialValue.get(),
                                                                    valueText.get(),
                                                                    resultValueLabel
                                                                    ))
    calculateButton.pack()

    resultLabel = Label(frame, text="Wynik")
    resultLabel.pack()

    resultValueLabel = Label(frame, text="")
    resultValueLabel.pack()

