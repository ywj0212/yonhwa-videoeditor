# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledMhTDhg.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread, Signal, QStandardPaths)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget, QFileDialog)

import worker
from utils import is_valid_time_str, time_str_to_seconds

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 320)
        MainWindow.setMinimumSize(QSize(400, 320))
        MainWindow.setMaximumSize(QSize(400, 320))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 270, 381, 23))
        self.progressBar.setValue(0)
        self.rPlaylist = QRadioButton(self.centralwidget)
        self.rPlaylist.setObjectName(u"rPlaylist")
        self.rPlaylist.setGeometry(QRect(10, 10, 99, 20))
        self.rPlaylist.setChecked(True)
        self.rJapanese = QRadioButton(self.centralwidget)
        self.rJapanese.setObjectName(u"rJapanese")
        self.rJapanese.setGeometry(QRect(120, 10, 99, 20))
        self.hr = QFrame(self.centralwidget)
        self.hr.setObjectName(u"hr")
        self.hr.setGeometry(QRect(10, 30, 381, 16))
        self.hr.setFrameShape(QFrame.Shape.HLine)
        self.hr.setFrameShadow(QFrame.Shadow.Sunken)
        self.bStart = QPushButton(self.centralwidget)
        self.bStart.setObjectName(u"bStart")
        self.bStart.setGeometry(QRect(320, 160, 71, 32))
        self.bStart.setCheckable(False)
        self.bStart.setAutoDefault(False)
        self.bOpenMusic = QPushButton(self.centralwidget)
        self.bOpenMusic.setObjectName(u"bOpenMusic")
        self.bOpenMusic.setGeometry(QRect(10, 41, 101, 31))
        self.bOpenImage = QPushButton(self.centralwidget)
        self.bOpenImage.setObjectName(u"bOpenImage")
        self.bOpenImage.setGeometry(QRect(10, 81, 101, 31))
        self.lMusicPath = QLabel(self.centralwidget)
        self.lMusicPath.setObjectName(u"lMusicPath")
        self.lMusicPath.setGeometry(QRect(120, 40, 271, 31))
        self.lImagePath = QLabel(self.centralwidget)
        self.lImagePath.setObjectName(u"lImagePath")
        self.lImagePath.setGeometry(QRect(120, 80, 271, 31))
        self.lStartTime = QLabel(self.centralwidget)
        self.lStartTime.setObjectName(u"lStartTime")
        self.lStartTime.setGeometry(QRect(10, 120, 101, 31))
        self.lStartTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lEndTime = QLabel(self.centralwidget)
        self.lEndTime.setObjectName(u"lEndTime")
        self.lEndTime.setGeometry(QRect(200, 120, 101, 31))
        self.lEndTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tStartTime = QPlainTextEdit(self.centralwidget)
        self.tStartTime.setObjectName(u"tStartTime")
        self.tStartTime.setGeometry(QRect(110, 120, 81, 31))
        self.tEndTime = QPlainTextEdit(self.centralwidget)
        self.tEndTime.setObjectName(u"tEndTime")
        self.tEndTime.setGeometry(QRect(310, 120, 81, 31))
        self.tLog = QPlainTextEdit(self.centralwidget)
        self.tLog.setObjectName(u"tLog")
        self.tLog.setGeometry(QRect(10, 200, 381, 71))
        self.tLog.setReadOnly(True)
        self.bOpenSaveDest = QPushButton(self.centralwidget)
        self.bOpenSaveDest.setObjectName(u"bOpenSaveDest")
        self.bOpenSaveDest.setGeometry(QRect(10, 160, 101, 31))
        self.lSavePath = QLabel(self.centralwidget)
        self.lSavePath.setObjectName(u"lSavePath")
        self.lSavePath.setGeometry(QRect(120, 160, 191, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.bOpenMusic.clicked.connect(MainWindow.open_bgm_dialog)
        self.bOpenImage.clicked.connect(MainWindow.open_img_dialog)
        self.bStart.clicked.connect(MainWindow.start_encoding)
        self.bOpenSaveDest.clicked.connect(MainWindow.open_save_dialog)

        self.bStart.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Yonhwa Video Editor", None))
        self.rPlaylist.setText(QCoreApplication.translate("MainWindow", u"\ud50c\ub808\uc774\ub9ac\uc2a4\ud2b8", None))
        self.rJapanese.setText(QCoreApplication.translate("MainWindow", u"\uc77c\ubcf8\uc5b4 \uc5b4\ud718", None))
        self.bStart.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.bOpenMusic.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc6d0 \ud30c\uc77c \uc5f4\uae30", None))
        self.bOpenImage.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ud30c\uc77c \uc5f4\uae30", None))
        self.lMusicPath.setText(QCoreApplication.translate("MainWindow", u"No File", None))
        self.lImagePath.setText(QCoreApplication.translate("MainWindow", u"No File", None))
        self.lStartTime.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791 \uc2dc\uac04(x:xx)", None))
        self.lEndTime.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc \uc2dc\uac04(x:xx)", None))
        self.bOpenSaveDest.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc800\uc7a5 \uc704\uce58", None))
        self.lSavePath.setText(QCoreApplication.translate("MainWindow", u"No Folder", None))
    # retranslateUi

    def open_bgm_dialog(self):
        # 기본 데스크탑 경로 가져오기
        desktop = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        path = QFileDialog.getOpenFileName(
            parent=self, 
            caption='음원 파일 경로', 
            dir=desktop,
            filter='*.mp3 *.wav *.ogg *.flac'
        )
        if not path[0]:
            return
        self.lMusicPath.setText(path[0])

    def open_img_dialog(self):
        desktop = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        path = QFileDialog.getOpenFileName(
            parent=self, 
            caption='이미지 파일 경로', 
            dir=desktop,
            filter='*.png'
        )
        if not path[0]:
            return
        self.lImagePath.setText(path[0])

    def open_save_dialog(self):
        desktop = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        path = QFileDialog.getExistingDirectory(
            parent=self, 
            caption='파일 저장 경로',
            dir=desktop
        )
        if not path:
            return
        self.lSavePath.setText(path)

    def start_encoding(self):
        ty = 0
        if self.rPlaylist.isChecked():
            ty = 0
        elif self.rJapanese.isChecked():
            ty = 1
        else:
            self.tLog.setPlainText("예상치 못한 에러: 유효하지 않은 출력 타입")
            return
        
        bgm_path: str = self.lMusicPath.text()
        img_path: str = self.lImagePath.text()

        if not os.path.exists(bgm_path):
            self.tLog.setPlainText("음원 파일이 존재하지 않습니다!")
            return
        if not os.path.exists(img_path):
            self.tLog.setPlainText("이미지 파일이 존재하지 않습니다!")
            return
        
        start_time_str: str = self.tStartTime.toPlainText()
        end_time_str: str = self.tEndTime.toPlainText()

        if not is_valid_time_str(start_time_str):
            self.tLog.setPlainText("시작 시간 형식이 올바르지 않습니다!")
            return
        if not is_valid_time_str(end_time_str):
            self.tLog.setPlainText("종료 시간 형식이 올바르지 않습니다!")
            return

        start_time: int = time_str_to_seconds(start_time_str)
        end_time: int = time_str_to_seconds(end_time_str)

        save_path: str = self.lSavePath.text()
        if not os.path.exists(save_path):
            self.tLog.setPlainText("저장 경로가 올바르지 않습니다!")
            return

        self.thread = QThread()
        self.worker = worker.Worker()
        self.worker.set_value(ty, bgm_path, img_path, start_time, end_time, save_path)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.finish_encoding)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.set_progress_bar)
        self.thread.start()

        self.tLog.setPlainText("인코딩 중... 잠시만 기다려주세요")
        
    def finish_encoding(self, res):
        self.tLog.setPlainText(res)

    def set_progress_bar(self, progress):
        self.progressBar.setValue(progress)
