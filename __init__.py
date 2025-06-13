from .simplecalc import SimpleCalcPlugin


def classFactory(iface):
    return SimpleCalcPlugin(iface)
