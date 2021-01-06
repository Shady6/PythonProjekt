metricToImperial = "metryczne -> imperialne"
imperialToMetric = "imperialne -> metryczne"


def changeConversionDirectionText(conversionDirection):
    if conversionDirection["text"] == metricToImperial:
        conversionDirection["text"] = imperialToMetric    
    else:
        conversionDirection["text"] = metricToImperial

def isMetric(conversionDirection):
    return conversionDirection["text"] == metricToImperial  