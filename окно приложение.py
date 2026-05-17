import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLineEdit, QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Мое приложение")
        self.setMinimumSize(400, 300)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        v_layout = QVBoxLayout()
        central_widget.setLayout(v_layout)
        
        self.label = QLabel("Введите текст:")
        v_layout.addWidget(self.label)
        
        self.text_input = QLineEdit()
        v_layout.addWidget(self.text_input)
        
        h_layout = QHBoxLayout()
        
        self.button1 = QPushButton("Нажми меня")
        self.button1.clicked.connect(self.on_button_click)
        h_layout.addWidget(self.button1)
        
        self.button2 = QPushButton("Очистить")
        self.button2.clicked.connect(self.clear_text)
        h_layout.addWidget(self.button2)
        
        v_layout.addLayout(h_layout)
        
        self.result_label = QLabel("Результат будет здесь")
        v_layout.addWidget(self.result_label)
    
    def on_button_click(self):
        text = self.text_input.text()
        if text:
            self.result_label.setText(f"Вы ввели: {text}")
        else:
            self.result_label.setText("Поле пустое!")
    
    def clear_text(self):
        self.text_input.clear()
        self.result_label.setText("Поле очищено")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
