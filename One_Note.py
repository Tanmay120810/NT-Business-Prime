import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsView,
                             QGraphicsScene, QGraphicsTextItem, QGraphicsPixmapItem, QColorDialog, QFileDialog, QLabel, 
                             QGraphicsItem, QMenuBar, QAction, QInputDialog, QToolBar, QTextEdit, QListView, QStyledItemDelegate)
from PyQt5.QtGui import QFont, QColor, QPixmap, QIcon, QPainter
from PyQt5.QtCore import Qt, QPointF, QTimer


class VintageNoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vintage Note App")
        self.setGeometry(100, 100, 1024, 768)
        self.setStyleSheet('background-color: #F4E1D2; color: #4B3621;')  # Vintage look
        
        # Main layout setup
        main_layout = QVBoxLayout()
        
        # Menu bar setup
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        
        new_action = QAction("New Note", self)
        new_action.triggered.connect(self.new_note)
        file_menu.addAction(new_action)
        
        open_action = QAction("Open Note", self)
        open_action.triggered.connect(self.open_note)
        file_menu.addAction(open_action)
        
        save_action = QAction("Save Note", self)
        save_action.triggered.connect(self.save_note)
        file_menu.addAction(save_action)
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create toolbar
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

        # Left-side layout for the notebook view (list of notes)
        self.note_list = QListView()
        self.note_list.setStyleSheet('background-color: #D9C3A8; border-radius: 10px;')
        
        self.note_list.clicked.connect(self.show_note)

        # Note area
        self.note_area = QTextEdit()
        self.note_area.setFont(QFont("Times New Roman", 12))  # Vintage font
        self.note_area.setStyleSheet('background-color: #FFF1E6; color: #4B3621; border-radius: 8px;')

        # Split the window with a vertical layout
        layout = QHBoxLayout()
        layout.addWidget(self.note_list, 1)
        layout.addWidget(self.note_area, 3)
        
        container_widget = QLabel()
        container_widget.setLayout(layout)
        self.setCentralWidget(container_widget)

        # To hold notes as key-value pairs (title -> content)
        self.notes = {}
        self.current_note_title = None

    def new_note(self):
        # Create a new note
        title, ok = QInputDialog.getText(self, "New Note", "Enter note title:")
        if ok and title:
            self.notes[title] = ""  # Initialize the note content
            self.note_list.setModel(self.get_notes_model())
            self.note_area.clear()
            self.current_note_title = title

    def open_note(self):
        # Open an existing note
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Note", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.notes[file_path] = content
                self.note_list.setModel(self.get_notes_model())
                self.note_area.setText(content)

    def save_note(self):
        if self.current_note_title:
            content = self.note_area.toPlainText()
            self.notes[self.current_note_title] = content
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Note", "", "Text Files (*.txt)")
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(content)
        
    def show_note(self, index):
        title = self.note_list.model().data(index)
        if title in self.notes:
            self.note_area.setText(self.notes[title])
            self.current_note_title = title

    def get_notes_model(self):
        from PyQt5.QtCore import QStringListModel
        model = QStringListModel()
        model.setStringList(list(self.notes.keys()))
        return model


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = VintageNoteApp()
    main_window.show()
    sys.exit(app.exec_())
