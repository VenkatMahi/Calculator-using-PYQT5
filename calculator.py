import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MainWindow(qtw.QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")     #sets title of window
        self.setLayout(qtw.QVBoxLayout())     #create a layout
        self.keypad()
        self.temp_nums = []                   #creating a list to store numbers
        self.fin_nums = []
        self.cal = []
        self.show()                           #used to show the progress


    def keypad(self):
        container = qtw.QWidget()             #creates a widget
        container.setLayout(qtw.QGridLayout()) #creates a grid layout in widget


        #Buttons
        self.result_field = qtw.QLineEdit()    #shows the result
        btn_result = qtw.QPushButton("Enter",clicked = self.func_result)
        btn_clear = qtw.QPushButton("clear",clicked = self.clear_calc)
        btn_back = qtw.QPushButton("<-",clicked  = self.backspace)
        btn_9 = qtw.QPushButton("9",clicked = lambda:self.num_press('9'))
        btn_8 = qtw.QPushButton("8",clicked = lambda:self.num_press('8'))
        btn_7 = qtw.QPushButton("7",clicked = lambda:self.num_press('7'))
        btn_6 = qtw.QPushButton("6",clicked = lambda:self.num_press('6'))
        btn_5 = qtw.QPushButton("5",clicked = lambda:self.num_press('5'))
        btn_4 = qtw.QPushButton("4",clicked = lambda:self.num_press('4'))
        btn_3 = qtw.QPushButton("3",clicked = lambda:self.num_press('3'))
        btn_2 = qtw.QPushButton("2",clicked = lambda:self.num_press('2'))
        btn_1 = qtw.QPushButton("1",clicked = lambda:self.num_press('1'))
        btn_0 = qtw.QPushButton("0",clicked = lambda:self.num_press('0'))
        btn_plus = qtw.QPushButton("+",clicked = lambda:self.func_press('+'))
        btn_sub = qtw.QPushButton("-",clicked = lambda:self.func_press('-'))
        btn_mul = qtw.QPushButton("x",clicked = lambda:self.func_press('*'))
        btn_div = qtw.QPushButton("/",clicked = lambda:self.func_press('/'))

        #gui
        

        #placing buttons
        container.layout().addWidget(self.result_field,0,0,1,3)
        container.layout().addWidget(btn_result,1,0,1,2)
        container.layout().addWidget(btn_clear,1,2)
        container.layout().addWidget(btn_back,1,3)
        container.layout().addWidget(btn_9,2,0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 2)
        container.layout().addWidget(btn_sub, 3, 3)
        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_mul, 4, 3)
        container.layout().addWidget(btn_0, 5,0,1,3)
        container.layout().addWidget(btn_div, 5, 3)
        self.layout().addWidget(container)

    def num_press(self,key_number):   ##used to store presed keys
        self.temp_nums.append(key_number)
        self.cal.append(key_number)
        temp_String = "".join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_String)
        else:
            self.result_field.setText(temp_String)

    def backspace(self):
        if(len(self.cal)==0):
            pass
        else:
            a=self.cal[-1]
            self.cal.pop()
            for i in range(len(self.temp_nums)):
                if(self.temp_nums[i]==a):
                    self.temp_nums.pop(i)
                    self.result_field.setText(str(*self.temp_nums))
            for i in range(len(self.fin_nums)):
                if(self.fin_nums[i]==a):
                    self.fin_nums.pop(i)
                    self.result_field.setText(str(*self.fin_nums))




    def func_press(self,operator):    #used to store operators
        temp_String  = ''.join(self.temp_nums)
        self.cal.append(operator)
        self.fin_nums.append(temp_String)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))


    def func_result(self):
        if(len(self.temp_nums)==0 and len(self.fin_nums)==0):
            result_string = "enter a valid number"
            self.result_field.setText(result_string)

        else:
            fin_String = ''.join(self.fin_nums) + ''.join(self.temp_nums)
            result_string = eval(fin_String)
            fin_String += "="
            fin_String += str(result_string)
            self.result_field.setText(fin_String)    #shows the result


    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums=[]
        self.fin_nums=[]


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()




                                                                                                                   