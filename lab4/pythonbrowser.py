from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys

from pathlib import Path


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("GONE.dust's Web Browser")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo_path = str(Path(__file__).parent / "GONEdust_128.jpg")
        logo.setPixmap(QPixmap(logo_path))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 2.1"))
        layout.addWidget(QLabel("Copyright GONE.dust"))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)
        
        back_path = str(Path(__file__).parent / "arrow-180.png")
        back_btn = QAction(QIcon(back_path), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_path = str(Path(__file__).parent / "arrow-000.png")
        next_btn = QAction(QIcon(next_path), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_path = str(Path(__file__).parent / "arrow-circle-315.png")
        reload_btn = QAction(QIcon(reload_path), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_path = str(Path(__file__).parent / "home.png")
        home_btn = QAction(QIcon(home_path), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()  # Yes, really!
        httpsicon_path = str(Path(__file__).parent / "arrow-180.png")
        self.httpsicon.setPixmap(QPixmap(httpsicon_path))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_path = str(Path(__file__).parent / "cross-circle.png")
        stop_btn = QAction(QIcon(stop_path), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        file_menu = self.menuBar().addMenu("&File")

        nex_tab_path = str(Path(__file__).parent / "ui-tab--plus.png")
        new_tab_action = QAction(QIcon(nex_tab_path), "New Tab", self)
        new_tab_action.setStatusTip("Open a new tab")
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        file_menu.addAction(new_tab_action)

        open_file_path = str(Path(__file__).parent / "disk--arrow.png")
        open_file_action = QAction(QIcon(open_file_path), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_path = str(Path(__file__).parent / "disk--pencil.png")
        save_file_action = QAction(QIcon(save_file_path), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_path = str(Path(__file__).parent / "printer.png")
        print_action = QAction(QIcon(print_path), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        help_menu = self.menuBar().addMenu("&Help")

        about_path = str(Path(__file__).parent / "question.png")
        about_action = QAction(QIcon(about_path), "About GONE.dust's Web Browser", self)
        about_action.setStatusTip("Find out more about GONE.dust's Web Browser") 
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_mozarella_path = str(Path(__file__).parent / "lifebuoy.png")
        navigate_mozarella_action = QAction(QIcon(navigate_mozarella_path),
                                            "GONE.dust's Web Browser Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to GONE.dust's Web Browser Homepage")
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)

        self.add_new_tab(QUrl('https://github.com/goner2202'), 'Homepage')

        self.show()

        self.setWindowTitle("GONE.dust's Web Browser")
        window_icon_path = str(Path(__file__).parent / "GONEdust_64.jpg")
        self.setWindowIcon(QIcon(window_icon_path))

    def add_new_tab(self, qurl=None, label="Blank"):

        if qurl is None:
            qurl = QUrl('')

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("%s - GONE.dust's Web Browser" % title)

    def navigate_mozarella(self):
        self.tabs.currentWidget().setUrl(QUrl("https://github.com/goner2202"))

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            self.tabs.currentWidget().setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = self.tabs.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.browser.print_)
        dlg.exec_()

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("https://github.com/goner2202"))

    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser=None):

        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() == 'https':
            # Secure padlock icon
            httpsicon1_path = str(Path(__file__).parent / "lock-ssl.png")
            self.httpsicon.setPixmap(QPixmap(httpsicon1_path))

        else:
            # Insecure padlock icon
            httpsicon2_path = str(Path(__file__).parent / "lock-nossl.png")
            self.httpsicon.setPixmap(QPixmap(httpsicon2_path))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
app.setApplicationName("GONE.dust's Web Browser")
app.setOrganizationName("GONE.dust")
app.setOrganizationDomain("Google.com")

window = MainWindow()

app.exec_()
