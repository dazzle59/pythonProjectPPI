import main_window
import sys
import sqlitedb


if __name__ == "__main__":
    app = main_window.QtWidgets.QApplication(sys.argv)
    MainWindow = main_window.QtWidgets.QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
