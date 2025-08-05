import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFontDatabase, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("MC Bedrock Unlocker")
    win.setFixedSize(600, 300)
    win.setStyleSheet("background-color: #292929;")

    # Set window icon
    if os.path.exists("./assets/icon/icon.png"):
        win.setWindowIcon(QIcon("./assets/icon/icon.png"))
    else:
        print("Warning: icon.png not found.")

    # Center the window
    qr = win.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    win.move(qr.topLeft())

    # Load custom font
    if os.path.exists("./assets/font/MinecraftTen.ttf"):
        font_id = QFontDatabase.addApplicationFont("./assets/font/MinecraftTen.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    else:
        print("Font file not found.")
        font_family = "monospace"

    # Add PNG Button
    png_button = QPushButton("", win)
    if os.path.exists("./assets/buttons/unlock1.png"):
        png_button.setIcon(QIcon("./assets/buttons/unlock1.png"))
        png_button.setIconSize(QSize(400, 156))  # Adjust size as needed
    else:
        print("Warning: unlock.png not found.")
        png_button.setText("Unlock")

    png_button.setGeometry(250, 100, 400, 156)  # x, y, width, height
    png_button.setFlat(True)  # Remove button border
    png_button.setStyleSheet("border: none;")  # Optional, to remove any border styling

    # Add button action
    def on_click():
        QMessageBox.information(win, "Button Clicked", "Unlock button was clicked!")

    png_button.clicked.connect(on_click)

    win.show()
    sys.exit(app.exec_())


window()
