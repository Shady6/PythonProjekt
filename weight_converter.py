from converter import Converter


####################################

def gr_to_mg(x):
    return x * 64.79891


def dr_to_gr(x):
    return x * 1771.8451953125002


def oz_to_gr(x):
    return x * 28349.523125000003


def lb_to_gr(x):
    return x * 453592.37000000005


def st_to_gr(x):
    return x * 6350293.180000001


def qt_to_gr(x):
    return x * 12700586.360000001


def cwt_to_gr(x):
    return x * 50802345.440000005


def t_to_gr(x):
    return x * 1016046908.8000001


def mg_to_g(x):
    return x * 0.001


def mg_to_dkg(x):
    return x * 0.0001


def mg_to_kg(x):
    return x * 0.000001


def mg_to_t(x):
    return x * 0.000000001


####################################

def t_to_mg(x):
    return x * 1000000000


def kg_to_mg(x):
    return x * 1000000


def dkg_to_mg(x):
    return x * 10000


def g_to_mg(x):
    return x * 1000


def mg_to_gr(x):
    return x / 64.79891


def gr_to_dr(x):
    return x / 1771.8451953125002


def gr_to_oz(x):
    return x / 28349.523125000003


def gr_to_lb(x):
    return x / 453592.37000000005


def gr_to_st(x):
    return x / 6350293.180000001


def gr_to_qt(x):
    return x / 12700586.360000001


def gr_to_cwt(x):
    return x / 50802345.440000005


def gr_to_t(x):
    return x / 1016046908.8000001


class WeightConverter(Converter):
    conversions = {"unit_A": {
        "A_to_middle_A": {
            "tona": t_to_mg,
            "kilogram": kg_to_mg,
            "dekagram": dkg_to_mg,
            "gram": g_to_mg
        },
        "middle_A_to_middle_B": mg_to_gr,
        "middle_A_to_A": {
            "tona": mg_to_t,
            "kilogram": mg_to_kg,
            "dekagram": mg_to_dkg,
            "gram": mg_to_g
        }
    },
        "unit_B": {
            "B_to_middle_B": {
                "tona angielska": t_to_gr,
                "cetnar": cwt_to_gr,
                "kwarter": qt_to_gr,
                "kamień": st_to_gr,
                "funt": lb_to_gr,
                "uncja": oz_to_gr,
                "dram": dr_to_gr
            },
            "middle_B_to_middle_A": gr_to_mg,
            "middle_B_to_B": {
                "tona angielska": gr_to_t,
                "cetnar": gr_to_cwt,
                "kwarter": gr_to_qt,
                "kamień": gr_to_st,
                "funt": gr_to_lb,
                "uncja": gr_to_oz,
                "dram": gr_to_dr
            }
        }
    }

    # pierwsza w liście jednostka to pośrednia
    imperialUnitNames = ("gran", "dram", "uncja", "funt", "kamień", "kwarter", "cetnar", "tona angielska")
    # pierwsza w liście jednostka to pośrednia
    metricUnitNames = ("miligram", "gram", "dekagram", "kilogram", "tona")
