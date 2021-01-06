# imperial to metric

def oz_to_ml(x):
    return x * 28.413


def gill_to_oz(x):
    return x * 5


def cup_to_oz(x):
    return x * 5 * 2


def pt_to_oz(x):
    return x * 5 * 2 * 2


def qt_to_oz(x):
    return x * 2 * 5 * 2 * 2


def gal_to_oz(x):
    return x * 4 * 2 * 5 * 2 * 2


def ml_to_l(x):
    return x * 0.001


def ml_to_m(x):
    return x * 0.000001


# metric to imperial

def m_to_ml(x):
    return x * 1000000


def l_to_ml(x):
    return x * 1000

def ml_to_oz(x):
    return x / 28.413

def oz_to_gill(x):
    return x / 5


def oz_to_cup(x):
    return x / 5 / 2


def oz_to_pt(x):
    return x / 5 / 2 / 2


def oz_to_qt(x):
    return x / 2 / 5 / 2 / 2


def oz_to_gal(x):
    return x / 4 / 2 / 5 / 2 / 2

