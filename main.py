import os
import sys
import ctypes
import time
from paths import CriticalPath
from PyQt5 import QtGui,QtWidgets



def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('img/icon.png'))
    if os.name == 'nt':
        # This is needed to display the app icon on the taskbar on Windows 7,8 and 10
        myappid = 'Maven....version 1.0'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            
    pixmap = QtGui.QPixmap('img/splash.png')
    splash = QtWidgets.QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    time.sleep(3)
    critical_path = CriticalPath()
    splash.finish(critical_path)
    critical_path.initialize_table()  # application starts from here by asking the user for the number of activities
    critical_path.show()
    sys.exit(app.exec_())

if __name__ == '__main__': main()
