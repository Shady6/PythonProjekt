from length import *

_metricValue = ""
_imperialValue = ""
_isMetricToImperial = True
valueToConvert = 0


def CalculateConversion(metricValue, imperialValue, isMetricToImperial, valueText):
    SaveValues(metricValue, imperialValue, isMetricToImperial, valueText)

    result = 0
    if (_isMetricToImperial):
        yards = MetricToYards()
        result = YardsToImperialDestination(yards)
    else:
        meters = ImperialToMeters()
        result = MetersToMetricDestination(meters)

    print(result)

def SaveValues(metricValue, imperialValue, isMetricToImperial, valueText):
    global _metricValue
    _metricValue = metricValue
    global _imperialValue
    _imperialValue = imperialValue
    global _isMetricToImperial
    _isMetricToImperial = isMetricToImperial
    global valueToConvert
    valueToConvert = float(valueText) # convert this shit to numerical        

def MetricToYards():
    meters = valueToConvert

    if _metricValue == "milimetr":
        meters = mm_to_m(valueToConvert)
    elif _metricValue == "centymetr":
        meters = cm_to_m(valueToConvert)    
    elif _metricValue == "kilometr":
        meters = km_to_m(valueToConvert) 

    result = m_to_yd(meters)
    return result

def YardsToImperialDestination(yards):  
    result = yards  
    if _imperialValue == "cal":
        result = yd_to_in(yards)
    elif _imperialValue == "stopa":
        result = yd_to_ft(yards)     
    elif _imperialValue == "pręt":
        result = yd_to_rd(yards)    
    elif _imperialValue == "łańcuch":
        result = yd_to_ch(yards)    
    elif _imperialValue == "furlong":
        result = yd_to_fur(yards) 
    elif _imperialValue == "mila":
        result = yd_to_mi(yards)   
    return result         

def ImperialToMeters():
    yards = valueToConvert

    if _imperialValue == "cal":
        yards = in_to_yd(valueToConvert)
    elif _imperialValue == "stopa":
        yards = ft_to_yd(valueToConvert)     
    elif _imperialValue == "pręt":
        yards = rd_to_yd(valueToConvert)    
    elif _imperialValue == "łańcuch":
        yards = ch_to_yd(valueToConvert)    
    elif _imperialValue == "furlong":
        yards = fur_to_yd(valueToConvert) 
    elif _imperialValue == "mila":
        yards = mi_to_yd(valueToConvert)        

    result = yd_to_m(meters)
    return result

def MetersToMetricDestination(meters):
    result = valueToConvert

    if _metricValue == "milimetr":
        meters = m_to_mm(meters)
    elif _metricValue == "centrymetr":
        meters = m_to_cm(meters)    
    elif _metricValue == "kilometr":
        meters = m_to_km(meters) 
    
    return result

