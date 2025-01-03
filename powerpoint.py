import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsView, QGraphicsScene,
                             QGraphicsTextItem, QGraphicsPixmapItem, QColorDialog, QFileDialog, QLabel, QGraphicsItem,
                             QMenuBar, QAction, QInputDialog, QToolBar, QSlider, QStyle, QGraphicsRectItem, QGraphicsOpacityEffect)
from PyQt5.QtGui import QPixmap, QColor, QFont, QImage, QPainter, QIcon
from PyQt5.QtCore import Qt, QPointF, QPropertyAnimation, QRect, QSequentialAnimationGroup, QTimer


class Slide(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 800, 600)
        self.setBackgroundBrush(Qt.white)
        self.items = []  # List to store items (text, images) for animation purposes

    def add_text(self, text):
        text_item = DraggableText(text)
        text_item.setFont(QFont("Arial", 16))
        self.addItem(text_item)
        self.items.append(text_item)
        self.add_animation(text_item)

    def add_image(self, image_path):
        pixmap = QPixmap(image_path)
        image_item = DraggableImage(pixmap)
        self.addItem(image_item)
        self.items.append(image_item)
        self.add_animation(image_item)

    def add_animation(self, item):
        # Animation for fade-in effect
        animation = QPropertyAnimation(item, b"opacity")
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.setDuration(1000)
        animation.start()


class DraggableText(QGraphicsTextItem):
    def __init__(self, text):
        super().__init__(text)
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.setOpacity(0)  # Initially invisible for fade-in effect
        self.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.setAcceptHoverEvents(True)

    def mouseDoubleClickEvent(self, event):
        new_text, ok = QInputDialog.getText(None, "Edit Text", "Enter new text:", text=self.toPlainText())
        if ok:
            self.setPlainText(new_text)

    def hoverEnterEvent(self, event):
        self.setCursor(Qt.SizeAllCursor)


class DraggableImage(QGraphicsPixmapItem):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.setOpacity(0)  # Initially invisible for fade-in effect
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event):
        self.setCursor(Qt.SizeAllCursor)


class PresentationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Presentation App")
        self.setGeometry(100, 100, 1024, 768)
        self.slides = []
        self.current_slide_index = -1

        # Main Layout
        main_layout = QVBoxLayout()

        # Graphics View
        self.graphics_view = QGraphicsView()
        main_layout.addWidget(self.graphics_view)

        # Controls Layout (for buttons)
        controls_layout = QHBoxLayout()

        self.add_slide_btn = QPushButton("Add Slide")
        self.add_slide_btn.clicked.connect(self.add_slide)
        controls_layout.addWidget(self.add_slide_btn)

        self.next_slide_btn = QPushButton("Next Slide")
        self.next_slide_btn.clicked.connect(self.next_slide)
        controls_layout.addWidget(self.next_slide_btn)

        self.prev_slide_btn = QPushButton("Previous Slide")
        self.prev_slide_btn.clicked.connect(self.prev_slide)
        controls_layout.addWidget(self.prev_slide_btn)

        self.add_text_btn = QPushButton("Add Text")
        self.add_text_btn.clicked.connect(self.add_text)
        controls_layout.addWidget(self.add_text_btn)

        self.add_image_btn = QPushButton("Add Image")
        self.add_image_btn.clicked.connect(self.add_image)
        controls_layout.addWidget(self.add_image_btn)

        self.change_bg_btn = QPushButton("Change Background")
        self.change_bg_btn.clicked.connect(self.change_background)
        controls_layout.addWidget(self.change_bg_btn)

        self.export_slide_btn = QPushButton("Export Slide")
        self.export_slide_btn.clicked.connect(self.export_slide)
        controls_layout.addWidget(self.export_slide_btn)

        self.preview_btn = QPushButton("Preview")
        self.preview_btn.clicked.connect(self.start_preview)
        controls_layout.addWidget(self.preview_btn)

        main_layout.addLayout(controls_layout)

        # Container Widget
        container_widget = QLabel()
        container_widget.setLayout(main_layout)
        self.setCentralWidget(container_widget)

        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_presentation)
        file_menu.addAction(new_action)
        
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_presentation)
        file_menu.addAction(open_action)
        
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_presentation)
        file_menu.addAction(save_action)
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Toolbar for quick actions
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

    def add_slide(self):
        slide = Slide()
        self.slides.append(slide)
        self.current_slide_index = len(self.slides) - 1
        self.graphics_view.setScene(slide)

    def next_slide(self):
        if self.current_slide_index < len(self.slides) - 1:
            self.current_slide_index += 1
            self.graphics_view.setScene(self.slides[self.current_slide_index])

    def prev_slide(self):
        if self.current_slide_index > 0:
            self.current_slide_index -= 1
            self.graphics_view.setScene(self.slides[self.current_slide_index])

    def add_text(self):
        if self.current_slide_index >= 0:
            text, ok = QInputDialog.getText(self, "Add Text", "Enter text:")
            if ok and text:
                self.slides[self.current_slide_index].add_text(text)

    def add_image(self):
        if self.current_slide_index >= 0:
            image_path, _ = QFileDialog.getOpenFileName(self, "Add Image", "", "Image Files (*.png *.jpg *.bmp)")
            if image_path:
                self.slides[self.current_slide_index].add_image(image_path)

    def change_background(self):
        if self.current_slide_index >= 0:
            color = QColorDialog.getColor()
            if color.isValid():
                self.slides[self.current_slide_index].setBackgroundBrush(color)

    def export_slide(self):
        if self.current_slide_index >= 0:
            file_path, _ = QFileDialog.getSaveFileName(self, "Export Slide", "", "PNG Files (*.png)")
            if file_path:
                image = QImage(800, 600, QImage.Format_ARGB32)
                painter = QPainter(image)
                self.slides[self.current_slide_index].render(painter)
                painter.end()
                image.save(file_path)

    def new_presentation(self):
        self.slides = []
        self.current_slide_index = -1
        self.graphics_view.setScene(None)

    def open_presentation(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Presentation", "", "Presentation Files (*.pptx)")
        if file_path:
            # Code to load presentation from file (to be implemented)
            pass

    def save_presentation(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Presentation", "", "Presentation Files (*.pptx)")
        if file_path:
            # Code to save presentation to file (to be implemented)
            pass

    def start_preview(self):
        if not self.slides:
            return
        # Run the preview with animations
        self.current_slide_index = 0
        self.preview_slide()

    def preview_slide(self):
        if self.current_slide_index < len(self.slides):
            slide = self.slides[self.current_slide_index]
            self.graphics_view.setScene(slide)
            
            # Apply animations for the slide
            for item in slide.items:
                animation = QPropertyAnimation(item, b"opacity")
                animation.setStartValue(0)
                animation.setEndValue(1)
                animation.setDuration(1000)
                animation.start()

            # Set the next slide after a short delay
            self.current_slide_index += 1
            QTimer.singleShot(2000, self.preview_slide)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = PresentationApp()
    main_window.show()
    sys.exit(app.exec_())
