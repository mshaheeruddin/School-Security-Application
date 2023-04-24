import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from frontend import WelcomeScreen
from LoginForm import Ui_SVA
from WelcomeScreen import Ui_WelcomeScreen
from WelcomeMain import Ui_WelcomeSSA
from verificationScreen import Ui_Verification
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel, QGraphicsPixmapItem, QGraphicsScene
import os
from database import school_db as db
from controller import QrScanning as qr
from os import path
import sqlite3
list_student = db.getStudents()
class VerificationWindow(QDialog, Ui_Verification):
    def __init__(self):
        super(VerificationWindow, self).__init__()
        self.color = "red"
        loadUi('verificationScreen.ui', self)
        self.flag = False
        self.nextButton.clicked.connect(self.display_image)
        self.nextButton.clicked.connect(self.display_qrcode)
        self.nextButton.clicked.connect(self.display_color)
        self.nextButton.clicked.connect(self.display_name)
        self.cancelButton.clicked.connect(self.verify_card)

    def verify_card(self):
        if(qr.qrscan() == True):
            self.color = "green"
            self.display_color(self.color)
        if(self.nextButton.clicked):
            self.color = "red"


    def display_name(self):
        if(len(list_student)!= 0):
            student_id = list_student[0] if len(list_student) > 0 else "None"
            self.nameMessage.setText(db.getStudentName(student_id))
            self.classMessage.setText(db.getStudentClass(student_id))
            # get the first student ID from the list of students
            if student_id:
                # call the getParentName() function with the student ID
                parent_name = db.getParentName(student_id)

                # set the text of the pickerMessage label to the parent name
                self.pickerMessage.setText(parent_name)
                if (len(list_student) != 0):
                    list_student.pop(0)
                else:
                    list_student.insert(0, "None")
            else:
                # if there are no students in the list, display an error message
                self.pickerMessage.setText("No picker found")
        else:
            self.nameMessage.setText("No Student Found")
            self.classMessage.setText("No Student Found")
            self.pickerMessage.setText("No Picker found")
    def display_color(self, color):
            color  = self.color
            image_path = os.path.join(f'../assets/{color}.png')
            if(color == "red"):
                self.statusMessage.setText("Not Ready to release")
            else:
                self.statusMessage.setText("Ready to release")
            pixmap = QPixmap(image_path)
            pixmap_scaled = pixmap.scaled(pixmap.width() // 3, pixmap.height() // 3)

            # Create a QGraphicsPixmapItem object and set the scaled pixmap
            pixmap_item = QGraphicsPixmapItem(pixmap_scaled)

            # Create a QGraphicsScene and set the pixmap item on it
            scene = QGraphicsScene()
            scene.addItem(pixmap_item)

            # Set the scene on the QGraphicsView widget
            self.lightStatus.setScene(scene)

    def display_qrcode(self):
            image_path = os.path.join('../assets/qrcode.png')
            pixmap = QPixmap(image_path)
            pixmap_scaled = pixmap.scaled(pixmap.width() // 3, pixmap.height() // 3)

            # Create a QGraphicsPixmapItem object and set the scaled pixmap
            pixmap_item = QGraphicsPixmapItem(pixmap_scaled)

            # Create a QGraphicsScene and set the pixmap item on it
            scene = QGraphicsScene()
            scene.addItem(pixmap_item)

            # Set the scene on the QGraphicsView widget
            self.qrCode.setScene(scene)

    def display_image(self):
        image_path = os.path.join('../assets/pic.png')
        pixmap = QPixmap(image_path)
        pixmap_scaled = pixmap.scaled(pixmap.width()//2 , pixmap.height()//2)

        # Create a QGraphicsPixmapItem object and set the scaled pixmap
        pixmap_item = QGraphicsPixmapItem(pixmap_scaled)

        # Create a QGraphicsScene and set the pixmap item on it
        scene = QGraphicsScene()
        scene.addItem(pixmap_item)

        # Set the scene on the QGraphicsView widget
        self.imageViewer.setScene(scene)





class WelcomeMain(QDialog, Ui_WelcomeSSA):
    def __init__(self):
        super(WelcomeMain, self).__init__()
        loadUi('WelcomeMain.ui', self)

        # Connect button clicked signal to slot
        self.releaseButton.clicked.connect(self.open_verification_screen)


    def open_verification_screen(self):
            # Hide the login screen
            self.hide()
            self.myVerificationWin = VerificationWindow()
            self.myVerificationWin.show()


class MainWindow(QDialog, Ui_SVA):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('LoginForm.ui', self)

        # Connect button clicked signal to slot
        self.pushButton.clicked.connect(self.open_welcome_screen)

    def open_welcome_screen(self):
        # Hide the login screen
        self.hide()
        self.myWelcomewin = WelcomeMain()
        self.myWelcomewin.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
