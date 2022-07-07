# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QPushButton, QGraphicsView, \
     QCheckBox, QProgressBar, QPlainTextEdit, QTreeView, QSystemTrayIcon, QAction, QMenu
from PySide2.QtCore import QFile
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader


class Widget(QMainWindow):  # QMainWindow ???
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        self.setWindowTitle('Stock problem')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self._createMenuBar()
        self.inExecution = False
        #
        # Get all UI elements
        #
        self.Canvas = self.findChild(QGraphicsView, 'Canvas')
        self.StepBox = self.findChild(QCheckBox, 'StepBox')
        self.ProgressBar = self.findChild(QProgressBar, 'progressBar')
        self.LogConsole = self.findChild(QPlainTextEdit, 'LogConsole')
        # UI buttons
        self.MaximizeBtn = self.findChild(QPushButton, 'MaximizeBtn')
        self.ExitBtn = self.findChild(QPushButton, 'ExitBtn')
        self.TrayBtn = self.findChild(QPushButton, 'TrayBtn')
        self.StepBtn = self.findChild(QPushButton, 'StepBtn')
        self.RunBtn = self.findChild(QPushButton, 'RunBtn')
        # menu buttons
#        self.FileBtn = self.findChild(QPushButton, 'FileBtn')
#        self.SaveBtn = self.findChild(QPushButton, 'SaveBtn')
#        self.HelpBtn = self.findChild(QPushButton, 'HelpBtn')

        self.StepBox = self.findChild(QCheckBox, 'StepBox')
        #
        # Add functionality
        #
        self.ExitBtn.clicked.connect(self.close)
        self.TrayBtn.clicked.connect(self.showMinimized)
        self.MaximizeBtn.clicked.connect(self.maximize)
        self.RunBtn.clicked.connect(self.testfunc)
#        self.FileBtn.clicked.connect(self.Menu_file)
#        self.HelpBtn.clicked.connect(self.Menu_Help)


    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
        path = os.fspath(Path(__file__).resolve().parent / "dialog.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.Dialog = loader.load(ui_file, self)
        ui_file.close()

    def maximize(self):
        if not self.isMaximized():
            self.showMaximized()
        else:
            self.showNormal()

    def appendStringToLog(self, str):
        self.LogConsole.appendPlainText(str)

    def clearLog(self):
        self.LogConsole.clear()

    def setProgress(self, percentage):
        self.ProgressBar.setValue(percentage)

    def testfunc(self):
        self.Dialog.exec_()
        if not self.inExecution:  # start execution
            if self.StepBox.isChecked():
                self.StepBtn.setFlat(False)
                self.RunBtn.setText('Finish')
            self.inExecution = True
            # run alg
            self.setProgress(50)
        else:  # stop execution
            self.RunBtn.setText('Run')
            self.inExecution = False
            self.StepBtn.setFlat(True)
            self.setProgress(0)

    def _createMenuBar(self):
#        menubar = self.menuBar()
        fileMenu = self.menuBar().addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import file', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        saveMenu = self.menuBar().addMenu('Save')
        helpMenu = self.menuBar().addMenu('Help')
        self.setGeometry(300, 300, 300, 200)
        self.show()
#    def Menu_Save(self):
#        menubar = self.menuBar()
#        saveMenu = menubar.addMenu('Save')

#    def Menu_Help(self):
#        menubar = self.menuBar()
#        menubar.addMenu('Help')


#        dlg = Dialog()
#        loader = QUiLoader()
#        path = os.fspath(Path(__file__).resolve().parent / "dialog.ui")
#        ui_file = QFile(path)
#        ui_file.open(QFile.ReadOnly)
#        dlg = loader.load(ui_file)
#        ui_file.close()
#        dlg.exec_()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
#    dlg = Dialog()
#    dlg.show()
    widget.show()
#    widget.setFixedSize(widget.size())
    sys.exit(app.exec_())