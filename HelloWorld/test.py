import sys

from PyQt5 import QtWidgets

from HelloWorld.form import Ui_Form  # 导入生成form.py里生成的类


class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    #定义槽函数
    def hello(self):
        self.textEdit.setText("  Hello world!!")

app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())