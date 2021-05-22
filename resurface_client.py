import json
import re
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
from usagelogger import resurface


class ResurfaceView(QWidget):
    def setupUi(self, MainWindow, controller):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 120, 451, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.req_widget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.req_widget.setObjectName("req_widget")
        self.body = QtWidgets.QWidget()
        self.body.setObjectName("body")
        self.req_body = QtWidgets.QTextEdit(self.body)
        self.req_body.setGeometry(QtCore.QRect(0, 0, 451, 191))
        self.req_body.setObjectName("req_body")
        self.req_widget.addTab(self.body, "")
        self.headers = QtWidgets.QWidget()
        self.headers.setObjectName("headers")
        self.req_headers = QtWidgets.QTextEdit(self.headers)
        self.req_headers.setGeometry(QtCore.QRect(0, 0, 461, 201))
        self.req_headers.setObjectName("req_headers")
        self.req_widget.addTab(self.headers, "")
        self.gridLayout.addWidget(self.req_widget, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 30, 451, 86))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.uRLLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.uRLLabel.setObjectName("uRLLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uRLLabel)
        self.uRLLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.uRLLineEdit.setObjectName("uRLLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uRLLineEdit)
        self.methodLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.methodLabel.setObjectName("methodLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.methodLabel)
        self.methodCombo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.methodCombo.setObjectName("methodCombo")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.methodCombo)
        self.sendReq = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.sendReq.setObjectName("sendReq")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sendReq)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.res_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.res_widget.setGeometry(QtCore.QRect(500, 30, 361, 301))
        self.res_widget.setObjectName("res_widget")
        self.response = QtWidgets.QWidget()
        self.response.setObjectName("response")
        self.response_content = QtWidgets.QTextEdit(self.response)
        self.response_content.setGeometry(QtCore.QRect(0, 0, 351, 281))
        self.response_content.setReadOnly(True)
        self.response_content.setObjectName("response_content")
        self.res_widget.addTab(self.response, "")
        self.headers1 = QtWidgets.QWidget()
        self.headers1.setObjectName("headers1")
        self.response_header = QtWidgets.QTextEdit(self.headers1)
        self.response_header.setGeometry(QtCore.QRect(0, 0, 351, 281))
        self.response_header.setReadOnly(True)
        self.response_header.setObjectName("response_header")
        self.res_widget.addTab(self.headers1, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSetup_Host = QtWidgets.QAction(MainWindow)
        self.actionSetup_Host.setObjectName("actionSetup_Host")
        self.actionSetup_Rules = QtWidgets.QAction(MainWindow)
        self.actionSetup_Rules.setObjectName("actionSetup_Rules")
        self.menuFile.addAction(self.actionSetup_Host)
        self.menuFile.addAction(self.actionSetup_Rules)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow, controller)
        self.req_widget.setCurrentIndex(0)
        self.res_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, controller):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resurfaceio | Client"))
        MainWindow.setWindowIcon(QtGui.QIcon("./assets/resurface.ico"))

        self.req_widget.setTabText(
            self.req_widget.indexOf(self.body), _translate("MainWindow", "Body")
        )
        self.req_headers.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&quot;content-type&quot;: &quot;application/json&quot;</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">}</p></body></html>',
            )
        )
        self.req_widget.setTabText(
            self.req_widget.indexOf(self.headers), _translate("MainWindow", "Headers")
        )
        self.uRLLabel.setText(_translate("MainWindow", "URL"))
        self.methodLabel.setText(_translate("MainWindow", "Method"))
        self.methodCombo.setItemText(0, _translate("MainWindow", "GET"))
        self.methodCombo.setItemText(1, _translate("MainWindow", "POST"))
        self.methodCombo.setItemText(2, _translate("MainWindow", "GRAPHQL"))

        self.sendReq.setText(_translate("MainWindow", "Send"))
        self.sendReq.clicked.connect(controller.clicked)

        self.res_widget.setTabText(
            self.res_widget.indexOf(self.response), _translate("MainWindow", "Response")
        )

        self.res_widget.setTabText(
            self.res_widget.indexOf(self.headers1), _translate("MainWindow", "Headers")
        )
        self.menuFile.setTitle(_translate("MainWindow", "Settings"))
        self.actionSetup_Host.setText(_translate("MainWindow", "Setup Host"))
        self.actionSetup_Host.triggered.connect(
            lambda: self.showDialog(controller, "Host Name", setting_type="HOST")
        )
        self.actionSetup_Rules.setText(_translate("MainWindow", "Setup Rules"))
        self.actionSetup_Rules.triggered.connect(
            lambda: self.showDialog(controller, "Rules", setting_type="RULES")
        )

    def showDialog(self, controller, form_label=None, setting_type=None):
        text, ok = QtWidgets.QInputDialog.getText(
            self,
            "Settings",
            form_label,
            text=controller.resurface_host
            if setting_type == "HOST"
            else controller.resurface_rules,
        )
        if ok:
            if text:
                if setting_type == "HOST":
                    controller.resurface_host = str(text)
                elif setting_type == "RULES":
                    controller.resurface_rules = str(text)

    @staticmethod
    def popup(type="Info", msg=None):
        msg_ = QMessageBox()
        msg_.setWindowTitle(f"{type}")
        msg_.setText(msg)
        x = msg_.exec_()


class Controller:
    def __init__(self):
        self.view = None
        self.resurface_host = "http://localhost:4001/message"
        self.resurface_rules = "include debug"

    def start(self, view):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.view = view()
        self.view.setupUi(MainWindow, self)
        MainWindow.show()
        sys.exit(app.exec_())

    def clicked(self, text=None):
        if text:
            self.view.sendReq.setText(text)
        self.handle_submission(self.view.uRLLineEdit.text())

    def handle_submission(
        self,
        url,
        sess=None,
    ):
        if not sess:
            sess = resurface.Session(
                url=self.resurface_host, rules=self.resurface_rules
            )
        self.view.response_content.clear()
        if self.validate(url):
            method_ = self.view.methodCombo.currentText()
            headers_ = self.view.req_headers.toPlainText()

            response = None
            try:
                if method_ == "POST":
                    response = sess.post(
                        url,
                        data=self.format_data(self.view.req_body.toPlainText()),
                        headers=self.format_data(headers_),
                    )
                elif method_ == "GRAPHQL":
                    response = sess.post(
                        url,
                        json={"query": self.view.req_body.toPlainText()},
                        headers=self.format_data(headers_),
                    )

                else:
                    response = sess.get(url, headers=self.format_data(headers_))
                self.view.response_content.setText(response.text)
                self.view.response_header.setText(
                    self.format_dict_str(response.headers)
                )
            except Exception as e:
                self.view.popup(msg="Connection Error!", type="Error")

        else:
            self.view.popup(msg="Invalid URL", type="Error")

    @staticmethod
    def validate(url_data):
        if not url_data:
            return False
        regex = re.compile(
            r"^(?:http|ftp)s?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE,
        )

        return re.match(regex, url_data) is not None

    @staticmethod
    def format_data(data):
        data_ = data
        try:
            data_ = json.loads(data_)
        except Exception as e:
            print(e)

    @staticmethod
    def format_dict_str(data: dict) -> str:
        list_ = []
        for k, v in data.items():
            list_.append(f"{k}: {v}")
        return "\n".join(list_)


if __name__ == "__main__":
    c = Controller()
    c.start(ResurfaceView)
