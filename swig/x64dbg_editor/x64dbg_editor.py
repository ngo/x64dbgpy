#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by Storm Shadow www.techbliss.org

print ''' ###################################################
 #              Author Storm Shadow                # 
 #                   Hotkeys                       # 
 #         NewFile:            Ctrl+N              #
 #         OpenFile:           Ctrl+O              #
 #         SaveFile:           Ctrl+S              #
 #         RunScript:          Ctrl+E              #
 #         Undo:               Ctrl+Z              #
 #         Redo:               Ctrl+Y              #
 #         SelectALL:          Ctrl+A              #
 #         Paste:              Ctrl+V              #
 #         ResetFolding:       Ctrl+R              #
 #         CircleFolding:      Ctrl+C              #
 #         PlainFolding:       Ctrl+P              #
 #         Xdbg64 Home:        Ctrl+W              #
 #         Irc:                Ctrl+I              #
 #         x64dbgPythonGit:    Ctrl+G              #
 #         Author:             Ctrl+B              #
 ###################################################
 #              x64dbg python Editor               #
 ###################################################
'''

import sys
import re
import os
from os import path
import sys
dn = os.getcwd()
sys.path.insert(0, os.getcwd() + r'\\plugins\\x64dbg_editor\\icons')
sys.path.insert(0, os.getcwd() + r'\\plugins\\x64dbg_editor')
sys.path.insert(0, dn)
apifolder = dn + r'\\plugins\\x64dbg_editor'

import PyQt5
from PyQt5 import QtCore, QtGui, Qsci, QtWidgets
from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciAPIs, \
    QsciScintillaBase
from PyQt5.QtGui import QFont, QFontMetrics, QColor, QTextCursor
from PyQt5.QtWidgets import QMainWindow
try:
    import ico
except ImportError:
    import icons.ico

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text,
                disambig, _encoding)

except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8('MainWindow'))
        MainWindow.resize(640, 480)
        self.vindu = QtWidgets.QWidget(MainWindow)
        self.vindu.setStyleSheet(_fromUtf8('notusedasyet'))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.filename = ''
        self.vindu.setObjectName(_fromUtf8('vindu'))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.vindu)
        app_icon = QtGui.QIcon()
        app_icon.addFile(':/ico/ico.png', QtCore.QSize(16, 16))
        MainWindow.setWindowIcon(app_icon)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8('verticalLayout'))
        self.codebox = Qsci.QsciScintilla(self.vindu)
        self.codebox.setToolTip(_fromUtf8(''))
        self.codebox.setWhatsThis(_fromUtf8(''))
        self.codebox.setAutoFillBackground(False)
        self.codebox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.codebox.setObjectName(_fromUtf8('codebox'))
        self.verticalLayout.addWidget(self.codebox)
        MainWindow.setCentralWidget(self.vindu)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName(_fromUtf8('toolBar'))

        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.toolBar.addSeparator()

        # first action Newfile
        self.toolBar.newAction = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/new.png'), 'New',
                              self.toolBar)
        self.toolBar.newAction.setStatusTip('Clear TextBox or make new document.'
                )
        self.toolBar.newAction.setShortcut('Ctrl+N')
        self.toolBar.newAction.triggered.connect(self.newfile)

        # second Action OpenFile
        self.toolBar.secondAction = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/open.png'), 'Open',
                              self.toolBar)
        self.toolBar.secondAction.setStatusTip('Create a new document from scratch.'
                )
        self.toolBar.secondAction.setShortcut('Ctrl+O')
        self.toolBar.secondAction.triggered.connect(self.open)

        # action 3 save file
        self.toolBar.Action3 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/save.png'), 'Save',
                              self.toolBar)
        self.toolBar.Action3.setStatusTip('Save Your File.')
        self.toolBar.Action3.setShortcut('Ctrl+S')
        self.toolBar.Action3.triggered.connect(self.savefile)

        # action 4 run file
        self.toolBar.Action4 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/run32.png'),
                              'Run To Debugger', self.toolBar)
        self.toolBar.Action4.setStatusTip('Run your file within debugger.'
                )
        self.toolBar.Action4.setShortcut('Ctrl+E')
        self.toolBar.Action4.triggered.connect(self.runto)

        # action 4 run file on windows
        # action 6 undo
        self.toolBar.Action6 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/undo.png'), 'Undo',
                              self.toolBar)
        self.toolBar.Action6.setStatusTip('Undo.')
        self.toolBar.Action6.setShortcut('Ctrl+Z')
        self.toolBar.Action6.triggered.connect(self.codebox.undo)

        # action 7 redo
        self.toolBar.Action7 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/redo.png'), 'Redo',
                              self.toolBar)
        self.toolBar.Action7.setStatusTip('Redo.')
        self.toolBar.Action7.setShortcut('Ctrl+Y')
        self.toolBar.Action7.triggered.connect(self.codebox.redo)

        # action8 rerset Folding
        self.toolBar.Action8 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/align-justify.png'),
                              'Reset Folding', self.toolBar)
        self.toolBar.Action8.setStatusTip('Reset Folding.')
        self.toolBar.Action8.setShortcut('Ctrl+R')
        self.toolBar.Action8.triggered.connect(self.nofoldingl)

        # actions9 CircledTreeFoldStyle
        self.toolBar.Action9 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/bullet.png'),
                              'Circled Tree Folding', self.toolBar)
        self.toolBar.Action9.setStatusTip('Circled Tree Folding.')
        self.toolBar.Action9.setShortcut('Ctrl+C')
        self.toolBar.Action9.triggered.connect(self.Circledfold)

        # actions10 plainFoldStyle
        self.toolBar.Action10 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/number.png'),
                              'Plain Folding', self.toolBar)
        self.toolBar.Action10.setStatusTip('Plain Folding')
        self.toolBar.Action10.setShortcut('Ctrl+P')
        self.toolBar.Action10.triggered.connect(self.plainfold)

        # web baby
        self.toolBar.Action11 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/web.png'),
                              'Goto x64dbg homepage', self.toolBar)
        self.toolBar.Action11.setStatusTip('Home of x64dbg')
        self.toolBar.Action11.setShortcut('Ctrl+W')
        self.toolBar.Action11.triggered.connect(self.webopen)

        # irc
        self.toolBar.Action12 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/irc.png'),
                              'Open x64dbg IRC', self.toolBar)
        self.toolBar.Action12.setStatusTip('Talk about x64dbg on irc')
        self.toolBar.Action12.setShortcut('Ctrl+I')
        self.toolBar.Action12.triggered.connect(self.ircopen)

        # github Python
        self.toolBar.Action14 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/github.png'),
                              'Open git python', self.toolBar)
        self.toolBar.Action14.setStatusTip('Open git python')
        self.toolBar.Action14.setShortcut('Ctrl+G')
        self.toolBar.Action14.triggered.connect(self.gitopen)

        # auther me :)
        self.toolBar.Action15 = \
            QtWidgets.QAction(QtGui.QIcon(':/ico/auth.png'), 'Author',
                              self.toolBar)
        self.toolBar.Action15.setStatusTip('Author')
        self.toolBar.Action15.setShortcut('Ctrl+B')
        self.toolBar.Action15.triggered.connect(self.Author)

        # actions
        self.toolBar.addAction(self.toolBar.newAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.secondAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action4)

        # self.toolBar.addSeparator()
        # For now global run isent here
        # self.toolBar.addAction(self.toolBar.Action5)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action6)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action7)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action8)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action9)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action10)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action11)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action12)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action14)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolBar.Action15)

        # self.toolBar.addSeparator()
        # self.toolBar.addAction(self.toolBar.Action16)
        # font
        skrift = QFont()
        skrift.setFamily('Consolas')
        skrift.setFixedPitch(True)
        skrift.setPointSize(12)
        self.codebox.setFont(skrift)

        # python style
        lexer = QsciLexerPython(self.codebox)

        # api test not working
        api = Qsci.QsciAPIs(lexer)
        API_FILE = apifolder + '\\python.api'

        # in case editor is run outside x64dbg
        API_FILE2 = dn + '\\python.api'
        api.load(API_FILE)
        api.load(API_FILE2)
        api.prepare()
        self.codebox.setAutoCompletionThreshold(1)
        self.codebox.setAutoCompletionThreshold(6)
        self.codebox.setAutoCompletionThreshold(8)
        self.codebox.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)
        lexer.setDefaultFont(skrift)
        self.codebox.setLexer(lexer)
        self.codebox.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1,
                                   'Consolas')

        # line numbers
        fontmetrics = QFontMetrics(skrift)
        self.codebox.setMarginsFont(skrift)
        self.codebox.setMarginWidth(0, fontmetrics.width('0000') + 6)
        self.codebox.setTabWidth(4)

        # brace
        self.codebox.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.codebox.setCaretLineBackgroundColor(QColor('#ffe4e4'))

        # auto line tab =4
        self.codebox.setAutoIndent(True)

        # scrollbar
        self.codebox.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate('MainWindow',
                                  'x64dbg Script Editor', None))
        self.toolBar.setWindowTitle(_translate('MainWindow', 'toolBar',
                                    None))

    # functions fo actions
    def newfile(self):
        self.codebox.clear()

    def open(self):
        self.path = QtCore.QFileInfo(self.filename).path()

        # Get filename and show only .writer files
        (self.filename, _) = \
            QtWidgets.QFileDialog.getOpenFileName(self.vindu,
                'Open File', self.path,
                'Python Files (*.py *.pyc *.pyw)', '')

        if self.filename:
            with open(self.filename, 'r') as self.file:
                self.codebox.setText(self.file.read())
        os.chdir(str(self.path))

    def savefile(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        (self.filename, _) = \
            QtWidgets.QFileDialog.getSaveFileName(self.vindu, 'Save as'
                , self.path, 'Python Files (*.py *.pyc *.pyw)')
        if self.filename:
            self.savetext(self.filename)
        os.chdir(str(self.path))

    def savetext(self, fileName):
        textout = self.codebox.text()
        file = QtCore.QFile(fileName)
        if file.open(QtCore.QIODevice.WriteOnly):
            QtCore.QTextStream(file) << textout
        else:
            QtWidgets.QMessageBox.information(self.vindu,
                    'Unable to open file', file.errorString())
        os.chdir(str(self.path))

    def runto(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        g = globals()
        os.chdir(str(self.path))
        script = str(self.codebox.text())
        try:
            exec (script, g)
            QtGui.QCloseEvent()
        except ImportError:
            os.chdir(str(self.path))
            os.path.join(os.path.expanduser('~'),
                         os.path.expandvars(str(self.path)))
            sys.path.insert(0, str(self.path))
            exec (script, g)
            QtGui.QCloseEvent()
        except Exception, e:
            print str(e)
            QtGui.QCloseEvent()

    def nofoldingl(self):
        self.codebox.setFolding(QsciScintilla.NoFoldStyle)

    def Circledfold(self):
        self.codebox.setFolding(QsciScintilla.CircledTreeFoldStyle)

    def plainfold(self):
        self.codebox.setFolding(QsciScintilla.PlainFoldStyle)

    def webopen(self):
        import webbrowser
        webbrowser.open('http://x64dbg.com')

    def ircopen(self):
        import webbrowser
        webbrowser.open('http://webchat.freenode.net/?channels=x64dbg')

    def gitopen(self):
        import webbrowser
        webbrowser.open('https://github.com/x64dbg/x64dbgpy')

    def Author(self):
        import webbrowser
        webbrowser.open('https://twitter.com/zadow28')

class MyWindow(QtWidgets.QMainWindow):
    '''
    we have to ask user for quiting so we can change back to root dir
    '''
    def closeEvent(self, event):
        os.chdir(dn)
        print '''
 ###################################################
 #              Author Storm Shadow                # 
 #                   Thx To                        #
 #                  Tomer Zait                     #
 #                   mrexodia                      #
 #      Follow x64dbg python project on Github     #
 ###################################################
 #              x64dbg python Editor               #
 ###################################################
'''
        os.chdir(dn)
        event.accept()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])
    MainWindow = MyWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
