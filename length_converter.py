def Convert(isMetricToImperial, metricName, imperialName, value):
    if isMetricToImperial:
        return MetricToImperial(metricName, imperialName, value)
    else:
        return ImperialToMetric(metricName, imperialName, value)


def MetricToImperial(metricName, imperialName, value):
    yards = MetricToYards(value, metricName)
    result = YardsToImperialDestination(yards, imperialName)
    return result


def ImperialToMetric(metricName, imperialName, value):
    meters = ImperialToMeters(value, imperialName)
    result = MetersToMetricDestination(meters, metricName)
    return result


def MetricToYards(metricValue, metricName):
    meters = metricValue

    if metricName == "milimetr":
        meters = mm_to_m(valueToConvert)
    elif metricName == "centymetr":
        meters = cm_to_m(valueToConvert)
    elif metricName == "kilometr":
        meters = km_to_m(valueToConvert)

    result = m_to_yd(meters)
    return result


def YardsToImperialDestination(yards, imperialName):
    result = yards

    if imperialName == "cal":
        result = yd_to_in(yards)
    elif imperialName == "stopa":
        result = yd_to_ft(yards)
    elif imperialName == "pręt":
        result = yd_to_rd(yards)
    elif imperialName == "łańcuch":
        result = yd_to_ch(yards)
    elif imperialName == "furlong":
        result = yd_to_fur(yards)
    elif imperialName == "mila":
        result = yd_to_mi(yards)

    return result


def ImperialToMeters(imperialValue, imperialName):
    yards = imperialValue

    if imperialName == "cal":
        yards = in_to_yd(valueToConvert)
    elif imperialName == "stopa":
        yards = ft_to_yd(valueToConvert)
    elif imperialName == "pręt":
        yards = rd_to_yd(valueToConvert)
    elif imperialName == "łańcuch":
        yards = ch_to_yd(valueToConvert)
    elif imperialName == "furlong":
        yards = fur_to_yd(valueToConvert)
    elif imperialName == "mila":
        yards = mi_to_yd(valueToConvert)

    result = yd_to_m(yards)
    return result


def MetersToMetricDestination(meters, metricName):
    result = meters

    if metricName == "milimetr":
        result = m_to_mm(meters)
    elif metricName == "centymetr":
        result = m_to_cm(meters)
    elif metricName == "kilometr":
        result = m_to_km(meters)

    return result


####################################
def mm_to_m(x):
    return x / 1000


def cm_to_m(x):
    return x / 100


def dm_to_m(x):
    return x / 10


def km_to_m(x):
    return x * 1000


def m_to_mm(x):
    return x * 1000


def m_to_cm(x):
    return x * 100


def m_to_dm(x):
    return x / 10


def m_to_km(x):
    return x / 1000


def m_to_yd(x):
    return x * 1.0936132983377078

####################################


def mi_to_yd(x):
    return x * 1760


def fur_to_yd(x):
    return x * 220


def ch_to_yd(x):
    return x * 22


def rd_to_yd(x):
    return x * 5.5


def ft_to_yd(x):
    return x / 3


def in_to_yd(x):
    return x / 36


def yd_to_mi(x):
    return x / 1760


def yd_to_fur(x):
    return x / 220


def yd_to_ch(x):
    return x / 22


def yd_to_rd(x):
    return x / 5.5


def yd_to_ft(x):
    return x * 3


def yd_to_in(x):
    return x * 36


def yd_to_m(x):
    return x * 0.9144
