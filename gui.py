import os
import sys
import pikepdf
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("decrypt pdf")
        self.setGeometry(350,150,400,100)
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()
        
        self.pathEdit=QLineEdit()
        fileButton = QPushButton("Select")
        fileButton.clicked.connect(self.openFile)
        runButton = QPushButton("Run")
        runButton.clicked.connect(self.convert)

        hbox1.addWidget(self.pathEdit)
        hbox1.addWidget(fileButton)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
    
        hbox2.addStretch()
        hbox2.addWidget(runButton)
        hbox2.addStretch()
        self.setLayout(vbox)
        self.show()

    def openFile(self):
        url = QFileDialog.getOpenFileName(self,"Select a File","","*.pdf")
        
        fileUrl = url[0]
        self.pathEdit.setText(fileUrl)

    def convert(self):

        file_path = self.pathEdit.text()
        if file_path == "":
            QMessageBox.about(self,"select a file")

        input_pdf = pikepdf.Pdf.open(file_path)
        pdf = pikepdf.Pdf.new()

        for _, page in enumerate(input_pdf.pages):
            pdf.pages.append(page)
        pdf.save(os.path.splitext(file_path)[0]+"_decrypt.pdf")
        
        QMessageBox.about(self,"done", "<p align='center'>Saved<br>"+os.path.splitext(file_path)[0]+"_decrypt.pdf</p>")
        print("done")        

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
