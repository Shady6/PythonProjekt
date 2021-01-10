from converter import Converter


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


class LengthConverter(Converter):
    conversions = {"unit_A": {
        "A_to_middle_A": {
            "kilometr": km_to_m,
            "decymetr": dm_to_m,
            "centymetr": cm_to_m,
            "milimetr": mm_to_m
        },
        "middle_A_to_middle_B": m_to_yd,
        "middle_A_to_A": {
            "kilometr": m_to_km,
            "decymetr": m_to_dm,
            "centymetr": m_to_cm,
            "milimetr": m_to_mm
        }
    },
        "unit_B": {
            "B_to_middle_B": {
                "mila": mi_to_yd,
                "furlong": fur_to_yd,
                "łańcuch": ch_to_yd,
                "pręt": rd_to_yd,
                "stopa": ft_to_yd,
                "cal": in_to_yd
            },
            "middle_B_to_middle_A": yd_to_m,
            "middle_B_to_B": {
                "mila": yd_to_mi,
                "furlong": yd_to_fur,
                "łańcuch": yd_to_ch,
                "pręt": yd_to_rd,
                "stopa": yd_to_ft,
                "cal": yd_to_in
            }
        }
    }

    # pierwsza w liście jednostka to pośrednia
    imperialUnitNames = ("jard", "cal", "stopa", "pręt", "łańcuch", "furlong", "mila")
    # pierwsza w liście jednostka to pośrednia
    metricUnitNames = ("metr", "milimetr", "centymetr", "decymetr", "kilometr")
