import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLineEdit, QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Настройка главного окна
        self.setWindowTitle("Мое приложение на PyQt5")
        self.setMinimumSize(400, 300)
        
        # Создание центрального виджета
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Создание вертикального layout
        v_layout = QVBoxLayout()
        central_widget.setLayout(v_layout)
        
        # Создание метки (QLabel)
        self.label = QLabel("Введите текст:")
        v_layout.addWidget(self.label)
        
        # Создание текстового поля (QLineEdit)
        self.text_input = QLineEdit()
        v_layout.addWidget(self.text_input)
        
        # Создание горизонтального layout для кнопок
        h_layout = QHBoxLayout()
        
        # Создание кнопки 1
        self.button1 = QPushButton("Нажми меня")
        self.button1.clicked.connect(self.on_button_click)
        h_layout.addWidget(self.button1)
        
        # Создание кнопки 2
        self.button2 = QPushButton("Очистить")
        self.button2.clicked.connect(self.clear_text)
        h_layout.addWidget(self.button2)
        
        # Добавление горизонтального layout в вертикальный
        v_layout.addLayout(h_layout)
        
        # Создание метки для результата
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
