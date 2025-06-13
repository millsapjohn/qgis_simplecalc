from qgis.PyQt.QtWidgets import QDockWidget, QMainWindow
from qgis.PyQt.QtCore import Qt
from .calc_dock import CalcDock


class SimpleCalcPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGuit(self):
        self.dock = CalcDock(self.iface)
        self.iface.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock)

    def unload(self):
        self.iface.removeDockWidget(self.dock)
        self.dock.deleteLater()
