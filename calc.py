from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from maths import Maths
cls, wnd = uic.loadUiType('win.ui')

class Calc(wnd, cls):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text = ''
        self.sign = ''
        self.m = Maths()
        
    def on_pb0_pressed(self):
        self.text += '0'
        self.leDisp.setText(self.text)

    def on_pb1_pressed(self):
        self.text += '1'
        self.leDisp.setText(self.text)

    def on_pb2_pressed(self):
        self.text += '2'
        self.leDisp.setText(self.text)
        
    def on_pb3_pressed(self):
        self.text += '3'
        self.leDisp.setText(self.text)

    def on_pb4_pressed(self):
        self.text += '4'
        self.leDisp.setText(self.text)

    def on_pb5_pressed(self):
        self.text += '5'
        self.leDisp.setText(self.text)
        
    def on_pb6_pressed(self):
        self.text += '6'
        self.leDisp.setText(self.text)

    def on_pb7_pressed(self):
        self.text += '7'
        self.leDisp.setText(self.text)


    def on_pb8_pressed(self):
        self.text += '8'
        self.leDisp.setText(self.text)

    def on_pb9_pressed(self):
        self.text += '9'
        self.leDisp.setText(self.text)

    def on_pbAdd_pressed(self):
        self.text += '+'
        self.leDisp.setText(self.text)
        self.sign = '+'

    def on_pbSub_pressed(self):
        self.text += '-'
        self.leDisp.setText(self.text)
        self.sign = '-'

    def on_pbMulti_pressed(self):
        self.text += '*'
        self.leDisp.setText(self.text)
        self.sign = '*'

    def on_pbDiv_pressed(self):
        self.text += '/'
        self.leDisp.setText(self.text)
        self.sign = '/'

    def on_pbDot_pressed(self):
        self.text += '.'
        self.leDisp.setText(self.text)

    def on_pbDel_pressed(self):
        if self.text != '':
            self.text = self.text.replace(self.text[-1],'')
            self.leDisp.setText(self.text)

    def on_pbEqual_pressed(self):
        if self.text != '':
            a, b = self.removeSign(self.sign)
            a, b = self.str2float(a, b)
            if self.sign == '+': result = self.m.add(a, b)
            elif self.sign == '-': result = self.m.sub(a, b)
            elif self.sign == '*': result = self.m.multi(a, b)
            elif self.sign == '/': result = self.m.divide(a, b)
            self.text = str(result)
            self.leDisp.setText(self.text)
            self.text = ''
            
    def str2float(self, *args):
        int_list = [float(val) for val in args] 
        return int_list

    def removeSign(self, sign: str) -> str:
        self.text = self.text.split(sign)
        a = self.text[0]
        b = self.text[-1]
        return a, b
    


    
        

app = QApplication([])
calc = Calc()
calc.show()
app.exec()
