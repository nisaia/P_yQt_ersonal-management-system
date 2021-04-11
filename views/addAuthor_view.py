import sys
from PyQt5.QtWidgets import QWidget
from assets.ui_PY.addAuthor_window import *
from database.db import session
from database.models import Author

class AddAuthorView(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.addAuthor_button.clicked.connect(self.addAuthor)
        self.ui.clearAll_button.clicked.connect(self.clearAll)

    def addAuthor(self):
        name = self.ui.name_lineEdit.text()
        surname = self.ui.surname_lineEdit.text()

        author = Author(name=name, surname=surname)
        session.add(author)
        session.commit()

        self.clearAll()

    def clearAll(self):
        self.ui.name_lineEdit.clear()
        self.ui.surname_lineEdit.clear()