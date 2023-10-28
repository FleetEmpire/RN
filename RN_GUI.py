import sys
from RnCore import*
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QComboBox, QLineEdit, QGroupBox

class RN_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("RN_MainWindow")
        self.layout = QVBoxLayout() # type: ignore
        self.lower_widget = QGroupBox("Selections")
        self.lower_layout = QVBoxLayout()
        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.lower_widget)
        self.lower_widget.setLayout(self.lower_layout)
        self.setLayout(self.layout)
        
        self.show()
        
    def IndexChanged(self):
        self.sl = QLineEdit()
        if self.combo.currentText() == "随机抽取":
            self.start_line_edit()
        elif self.combo.currentText() == "含剔除的随机抽取":
            pass
        
    def start_line_edit(self):
        self.lower_layout.addWidget(self.sl)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RN_MainWindow()
    sys.exit(app.exec_())
    