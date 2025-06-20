import photo_order
import os
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BASE_DIR1 = BASE_DIR / "script_get"
os.chdir(BASE_DIR1)

df = pd.DataFrame(columns=['number'])
df.loc[len(df)] = {'number': 0}
df.loc[len(df)] = {'number': 0}
df.loc[len(df)] = {'number': BASE_DIR1}
df.to_csv(BASE_DIR1.parent/'temp/num.csv')
# stop
# import script_des
# import script_pho
## Start work with QT6
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
def Window():
    app = QApplication(sys.argv)
    widget = QWidget()
    label = QLabel(widget)
    label.setText("Hello World!")
    widget.setGeometry(200,200,300,400)
    label.move(50,20)
    widget.setWindowTitle("Get-data-from-Shop-Deere")
    widget.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    Window()

# class MyWindow(Gtk.Window):
#     def __init__(self):
#         super().__init__(title="Get data")
#         self.set_default_size(400, 400)
#         # Create a vertical box to hold the widgets
#         vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
#         self.add(vbox)
#
#         # Create two entry fields
#         self.star_photo = Gtk.Entry()
#         vbox.pack_start(self.star_photo, True, True, 0)
#
#         self.end_photo = Gtk.Entry()
#         vbox.pack_start(self.end_photo, True, True, 0)
#
#         # Button photo
#         get_photo = Gtk.Button(label="Get photo")
#         get_photo.connect("clicked", self.Work_on_photo)
#         vbox.pack_start(get_photo, True, True, 0)
#
#         # Button order
#         Get_order = Gtk.Button(label="Get order photo")
#         Get_order.connect("clicked", self.Work_on_order)
#         vbox.pack_start(Get_order, True, True, 0)
#
#         # Button desribe
#         Get_describe = Gtk.Button(label="Get describe")
#         Get_describe.connect("clicked", self.Work_on_describe)
#         vbox.pack_start(Get_describe, True, True, 0)
#         # Show all widgets
#         self.show_all()
#
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
# # Create and run the application
# win = MyWindow()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()