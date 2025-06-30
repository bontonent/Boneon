from PyQt6.QtGui import QEnterEvent, QIcon
import photo_order
import os
import pandas as pd
# correct where we are
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
BASE_DIR1 = BASE_DIR / "script_get"
os.chdir(BASE_DIR1)
#create all nessesary file if don't have
try:
    os.mkdir(BASE_DIR1.parent.parent/"photo")
    print("created")
except:
    print("don't need create directory photo")
try:
    pd.read_excel(BASE_DIR1.parent.parent/"art_photo.xlsx")
except:
    import PyQt6
    from PyQt6 import QtWidgets

    app = QtWidgets.QApplication([])

    error_dialog = QtWidgets.QErrorMessage()
    error_dialog.setWindowTitle("Error")
    error_dialog.showMessage("Don't have art_photo.xlsx")
    app.exec()
    print("Need VPN")
import script_pho
import script_des

df = pd.DataFrame(columns=['number'])
df.loc[len(df)] = {'number': 0}
df.loc[len(df)] = {'number': 0}
df.to_csv(BASE_DIR1.parent/'temp/num.csv')
# stop
# import script_des
# import script_pho

#Start work with QT6
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys
class MyWindow(QMainWindow):
    def __init__(self):
        self.star_photo_en = 0
        self.end_photo_en = 0
        #main
        super().__init__()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.setGeometry(200, 200, 300, 400)
        self.setWindowIcon(QIcon(str(BASE_DIR1.parent/'temp/ico.png')))
        self.setWindowTitle("Boneon")
        layout = QVBoxLayout()
        # describe first editor
        label1 = QLabel(self)
        label1.setText("Вставте в поле значення першого елементу(найменьше 0)")
        label1.setFixedHeight(12)
        #entry for first number photo
        star_photo = QLineEdit()
        star_photo.setMaxLength(3)
        star_photo.setPlaceholderText("Enter number first photo")
        star_photo.textEdited.connect(self.star_text_edited)
        # describe first editor
        label2 = QLabel(self)
        label2.setText("Вставте в поле значення останнього елементу")
        label2.setFixedHeight(10)
        # entry for end number photo
        end_photo = QLineEdit()
        end_photo.setMaxLength(3)
        end_photo.setPlaceholderText("Enter number end photo")
        end_photo.textEdited.connect(self.end_text_edited)
        #for button 1
        button1 = QPushButton("Get photo")
        button1.clicked.connect(self.Work_on_photo)
        # for button 2
        button2 = QPushButton("Get order photo")
        button2.clicked.connect(self.Work_on_order)
        # for button 3
        button3 = QPushButton("Get describe")
        button3.clicked.connect(self.Work_on_describe)
        # All element in place
        layout.addWidget(label1)
        layout.addWidget(star_photo)
        layout.addWidget(label2)
        layout.addWidget(end_photo)
        # add button
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        central_widget.setLayout(layout)
    def error_window(self, messanger):
        button = QMessageBox.critical(self,"Error", messanger, buttons = QMessageBox.StandardButton.Close)
    def information_windows(self, messanger):
        button = QMessageBox.information(self, "Information", messanger, buttons=QMessageBox.StandardButton.Close)


    def Work_on_photo(self):
        print("start work")
        end = 1
        number1 = 0 ;number2=0
        num1 = self.star_photo_en
        num2 = self.end_photo_en
        print(num1, num2)
        try:
            number1 = int(num1)
            number2 = int(num2)
            df1 = pd.DataFrame(columns=['number'])
            df1.loc[len(df1)] = {'number': number1}
            df1.loc[len(df1)] = {'number': number2}
            df1.to_csv(BASE_DIR1.parent / 'temp/num.csv')
            if (number1 >= number2) | (number1 < 0):
                end = 0
                self.error_window("Don't correct numbers for using")
        except:
            end = 0
            self.error_window("Need write numbers")
        if end == 1:

            script_pho.script_get(BASE_DIR,number1, number2)


            self.information_windows("Complete work with create photo/..")

    def Work_on_order(self):
        print("start work")
        # Work main element
        photo_order.order(BASE_DIR)
        self.information_windows("Complete work with create pull_photo.xlsx")


    def Work_on_describe(self, entry_number):
        print("start work")
        script_des.get_des(BASE_DIR)
        self.information_windows("Complete work with create describe.xlsx")

    def star_text_edited(self, entry_number):
        self.star_photo_en = entry_number
    def end_text_edited(self, entry_number):
        self.end_photo_en = entry_number
    # def show_error_diagnostic(self, title, message):
    #     dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.OK, title)
    #     dialog.format_secondary_text(message)
    #     dialog.run()
    #     dialog.destroy()



    # def Window():
    #     app = QApplication(sys.argv)
    #     widget = QWidget()
    #     label = QLabel(widget)
    #     label.setText("Hello World!")


# class MyWindow(Gtk.Window):

#     def Work_on_photo(self, button):
#         print("start work")
#         end = 1
#         num1 = self.star_photo.get_text()
#         num2 = self.end_photo.get_text()
#         print(num1, num2)
#         try:
#             number1 = int(num1)
#             number2 = int(num2)
#             if (number1 >= number2) | (number1 < 0):
#                 end = 0
#                 self.show_error_diagnostic("Error","don't correct number")
#         except:
#             end = 0
#             self.show_error_diagnostic("Error","Need write number !!!")
#
#         if end == 1:
#             # Get the text from the entry fields
#             # text1 = self.entry1.get_text()
#             script_pho.script_get(BASE_DIR,number1, number2)
#             complite = Gtk.MessageDialog(parent=self, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Done")
#             complite.format_secondary_text("done work")
#             complite.run()
#             complite.destroy()
#             print(f"end work")
#
#     def Work_on_order(self, button):

#

#         print("start work")
#         # Work main element
#         photo_order.order(BASE_DIR)
#
#         complite = Gtk.MessageDialog(  parent=self, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Done")
#         complite.format_secondary_text("done work")
#         complite.run()
#         complite.destroy()

#     print("end work")
#
#     def Work_on_describe(self, button):
#
#         print(f"Start")
#         script_des.get_des(BASE_DIR)
#         complite = Gtk.MessageDialog(parent=self, flags=0, message_type=Gtk.MessageType.INFO,
#                                      buttons=Gtk.ButtonsType.OK, text="Done")
#         complite.format_secondary_text("done work")
#         complite.run()
#         complite.destroy()
#
#     def show_error_diagnostic(self, title, message):
#         dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.OK, title)
#         dialog.format_secondary_text(message)
#         dialog.run()
#         dialog.destroy()
#

# Create and run the application
app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec()

# # Create and run the application
# win = MyWindow()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()

