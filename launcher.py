from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
import subprocess
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1161, 794)
        MainWindow.setStyleSheet("color : white")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Get base path depending on if we're running as a script or exe
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS  # This is where PyInstaller extracts bundled files
        else:
            base_path = os.path.abspath(".")

        # Update paths to media files
        video_path = os.path.join(base_path, 'media', 'media.avi')
        icon_path = os.path.join(base_path, 'media', 'CANCERVGICON.PNG')

        # Main Widget Setup
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1171, 991))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(
            "background-color : rgb(40, 40, 40); border : rgba(0,0,0,0); color : white; font: 18pt 'Power Green';"
        )
        self.widget.setObjectName("widget")

        # Labels and Buttons
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(530, 80, 81, 16))
        self.label_2.setStyleSheet("background-color : rgba(0,0,0,0); font: 8pt 'MS Sans Serif'; color: white")
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(430, 20, 281, 61))
        self.label.setStyleSheet("font: 87 36pt 'Segoe UI Black'; font: bold; color : rgb(255, 255, 255); background-color : rgba(255,255,255,0)")
        self.label.setObjectName("label")

        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 1171, 991))
        self.widget_4.setStyleSheet("background-color : rgba(0,0,0,150);")
        self.widget_4.setObjectName("widget_4")
        self.widget_4.hide()

        # Buttons on the left side
        button_names = [
            "THE MANUAL", "CASE 1", "CASE 2", "CASE 3", "CASE 4", "CASE 5", 
            "CASE 6", "CASE 7", "CASE 8", "CASE 9", "CASE 10"
        ]
        
        for i, name in enumerate(button_names):
            button = QtWidgets.QPushButton(self.widget)
            button.setGeometry(QtCore.QRect(30, 120 + i*60, 301, 51))
            button.setStyleSheet("""
                QPushButton {
                    border-radius: 5px; 
                    background-color: black;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #151515;  /* Lighter color on hover */
                }
                QPushButton:pressed {
                    background-color: #101010;  /* Darker color when pressed */
                }
            """)
            button.setObjectName(f"pushButton_{i+1}")
            button.setText(name)
            if i==0:
                button.clicked.connect(self.widget_4.show)
            else:
                button.clicked.connect(lambda _, mga=i: self.run(mga))
        
        # The main video widget area (widget_2)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(340, 120, 791, 651))
        self.widget_2.setStyleSheet("background-color : rgba(0,0,0,90); border-radius : 10px;")
        self.widget_2.setObjectName("widget_2")

        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(350, 360, 771, 401))
        self.widget_3.setStyleSheet("background-color : rgba(0,0,0,90); border-radius : 10px;")
        self.widget_3.setObjectName("widget_2")

        # Video widget inside widget_2
        self.videoWidget = QtMultimediaWidgets.QVideoWidget(self.widget_3)
        self.videoWidget.setGeometry(QtCore.QRect(10, 10, 751, 381))  # Adjusted to fit within widget_2
        self.videoWidget.setStyleSheet("border-radius: 10px; border-color: rgb(250,250,250); background-color: black;")
        self.videoWidget.setObjectName("videoWidget")

        # Text Browser inside widget_2
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 771, 221))
        self.textBrowser.setStyleSheet("padding: 5px;")
        self.textBrowser.setObjectName("textBrowser")

        # Create the Media Player
        self.mediaPlayer = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("media/media.avi")))

        self.videoWidget.mousePressEvent = self.toggle_video_playback
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
        label = QLabel(self.widget_4)
        pixmap = QPixmap('media/THEMANUAL.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry(292,0,577,794)

        self.close_button = QtWidgets.QPushButton(self.widget_4)
        self.close_button.setGeometry(QtCore.QRect(1101,10,50,50))
        self.close_button.setStyleSheet("""
                QPushButton {
                    background-color : rgba(250,250,250,50); 
                    color: white; 
                    border-radius: 25px; 
                    font: bold 15pt 'Power Green';
                    color: white;
                }
                QPushButton:hover {
                    background-color: rgba(250,250,250,100);
                }
            """)
        self.close_button.setObjectName("close_button")
        self.close_button.setText("X")
        self.close_button.clicked.connect(self.widget_4.hide)

    def run(self, mga):
        subprocess.run([f"sims/cancer{(mga)}.exe"], check=True)

    def toggle_video_playback(self, event):
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CANCER VG LAUNCHER"))
        MainWindow.setWindowIcon(QIcon("media/CANCERVGICON.PNG"))
        self.label_2.setText(_translate("MainWindow", "LAUNCHER"))
        self.label.setText(_translate("MainWindow", "CANCER VG"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Power Green\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><span style=\" font-family:\'Lexend\'; font-size:12pt; font-weight:696; color:#f9f9f9; background-color:transparent;\">OVERVIEW</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; color:#f9f9f9; background-color:transparent;\">Cancer cells differ from normal cells in that they can multiply and survive indefinitely, rather than following a natural life cycle of birth and death. Cancer affects both males and females equally and can impact nearly any body part, potentially spreading to other areas. This disease is not limited to humans; it can also occur in many animals. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; font-family:\'Montserrat\'; font-size:10pt; color:#f9f9f9;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; color:#f9f9f9; background-color:transparent;\">Your job is to determine the best possible treatment for any given form of cancer in the human body. While you\'ve got a high budget and lots of time, the life of these patients are in YOUR hands. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%; font-family:\'Montserrat\'; font-size:10pt; color:#f9f9f9;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; color:#f9f9f9; background-color:transparent;\">Below is a video regarding how cancer develops and what happens inside the cells (click the space below to begin).</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
