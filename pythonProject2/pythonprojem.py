import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class Anapencere(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("ArakhisBrowser")
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setWindowIcon(QIcon("browserlogo.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.cubuk = QToolBar()
        self.cubuk.setStyleSheet("background:#900;color:white")
        self.cubuk.setFixedHeight(46)
        self.cubuk.setMovable(False)
        self.addToolBar(self.cubuk)

        self.geri= QAction("Geri",self)
        self.geri.triggered.connect(lambda: self.tab.currentWidget().back())
        self.cubuk.addAction(self.geri)


        self.ileri =QAction("İleri",self)
        self.ileri.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.cubuk.addAction(self.ileri)

        self.yenile = QAction("Yenile",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.cubuk.addAction(self.yenile)


        self.yenile = QAction("Yeni",self)
        self.yenile.triggered.connect(lambda: self.tab.currentWidget())
        self.cubuk.addAction(self.yenile)


        self.linkyeri = QLineEdit()


        self.linkyeri.returnPressed.connect(self.linkegit)



        self.cubuk.addWidget(self.linkyeri)


        self.pencere(QUrl("https://www.google.com.tr"))


    def pencere(self,url):

        brw = QWebEngineView()
        brw.setUrl(url)

        i = self.tab.addTab(brw,"HomePage")

        brw.urlChanged.connect(lambda url, brw = brw: self.linkyeriniguncelle(url,brw))

    def linkegit(self):

        u = QUrl(self.linkyeri.text())


        if u.scheme() == "":
            u.setScheme("http")


        self.tab.currentWidget().setUrl(u)

    def linkyeriniguncelle(self, u, brw =None):

        self.linkyeri.setText(u.toString())


app = QApplication(sys.argv)
main = Anapencere()
main.show()
sys.exit(app.exec_())


