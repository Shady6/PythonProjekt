from length import *

_metricValue = ""
_imperialValue = ""
_isMetricToImperial = True
valueToConvert = 0


def CalculateConversion(metricValue, imperialValue, isMetricToImperial, valueText, resultValueLabel):
    SaveValues(metricValue, imperialValue, isMetricToImperial, valueText)

    result = 0
    if (_isMetricToImperial):
        yards = MetricToYards()
        result = YardsToImperialDestination(yards)
    else:
        meters = ImperialToMeters()
        result = MetersToMetricDestination(meters)

    resultValueLabel['text'] = str(result)

def SaveValues(metricValue, imperialValue, isMetricToImperial, valueText):
    global _metricValue
    _metricValue = metricValue
    global _imperialValue
    _imperialValue = imperialValue
    global _isMetricToImperial
    _isMetricToImperial = isMetricToImperial
    global valueToConvert
    valueToConvert = float(valueText) # convert this shit to numerical        

