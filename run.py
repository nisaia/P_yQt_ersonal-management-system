import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from views.main_view import MainView
from os.path import join
from utils.constants import styles_path

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('assets/images/icons/book.png'))
    with open(join(styles_path, 'style.qss'), 'r') as f:
        qss = f.read()
        app.setStyleSheet(qss)
    main_window = MainView()
    main_window.setWindowTitle('Personl book library')
    main_window.show()
    sys.exit(app.exec_())