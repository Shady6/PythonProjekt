from converter import Converter

####################################


def gill_to_oz(x):
    return x * 5


def cup_to_oz(x):
    return x * 10


def pt_to_oz(x):
    return x * 20


def qt_to_oz(x):
    return x * 40


def gal_to_oz(x):
    return x * 160


def ml_to_l(x):
    return x * 0.001


def ml_to_m(x):
    return x * 0.000001


def oz_to_ml(x):
    return x * 28.413


####################################

def m_to_ml(x):
    return x * 1000000


def l_to_ml(x):
    return x * 1000


def oz_to_gill(x):
    return x / 5


def oz_to_cup(x):
    return x / 10


def oz_to_pt(x):
    return x / 20


def oz_to_qt(x):
    return x / 40


def oz_to_gal(x):
    return x / 160


def ml_to_oz(x):
    return x / 28.413


class VolumeConverter(Converter):
    conversions = {"unit_A": {
        "A_to_middle_A": {
            "metr sześcienny": m_to_ml,
            "litr": l_to_ml
        },
        "middle_A_to_middle_B": ml_to_oz,
        "middle_A_to_A": {
            "metr sześcienny": ml_to_m,
            "litr": ml_to_l
        }
    },
        "unit_B": {
        "B_to_middle_B": {
            "gil": gill_to_oz,
            "kubek": cup_to_oz,
            "pinta": pt_to_oz,
            "kwarta": qt_to_oz,
            "galon": gal_to_oz
        },
        "middle_B_to_middle_A": oz_to_ml,
        "middle_B_to_B": {
            "gil": oz_to_gill,
            "kubek": oz_to_cup,
            "pinta": oz_to_pt,
            "kwarta": oz_to_qt,
            "galon": oz_to_gal
        }
    }
    }

    # pierwsza w liście jednostka to pośrednia
    imperialUnitNames = ("uncja", "gil", "kubek", "pinta", "kwarta", "galon")
    # pierwsza w liście jednostka to pośrednia
    metricUnitNames = ("mililitr", "litr", "metr sześcienny")
