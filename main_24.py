from PyQt5.Qt import *
from dian24 import Ui_Form
import sys
import random
class MyObject(QObject):
    def timerEvent(self, evt):
        print(evt, "1")
class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)  # 这一步不能掉
        self.kaishi.clicked.connect(self.display_begin)
        self.num = [0,0,0,0]
        #self.nz.startMyTimer(1000)
        self.queding.clicked.connect(self.display_check)
        self.beginfg  = False
        self.chonglai.clicked.connect(self.display_begin)
        self.timer_id=None
    def display_check(self):
        if self.beginfg:
            temp_str = self.shuru.text()
            self.chfg = True
            self.okk = [self.num[0],self.num[1],self.num[2],self.num[3]]
            for i in temp_str:
                if i not in [str(self.num[0]),str(self.num[1]),str(self.num[2]),str(self.num[3]),] and (i not in ["(",")","+","-","*","/"]):
                    QMessageBox.about(self, "错误", "输入公式有误")
                    self.chfg = False
                    break
                if i==str(self.num[0]):
                    self.okk[0]=0
                if i==str(self.num[1]):
                    self.okk[1]=0
                if i==str(self.num[2]):
                    self.okk[2]=0
                if i==str(self.num[3]):
                    self.okk[3]=0
            if self.okk[0]!=0 or self.okk[1]!=0 or self.okk[2]!=0 or self.okk[3]!=0:
                self.chfg = False
                self.label.setText("很遗憾，答错了")
            if self.chfg:
                if eval(self.shuru.text())==24:
                    self.label.setText("恭喜你，答对了")
                    self.killTimer(self.timer_id)
                    self.nz.setText("")
                else:
                    self.label.setText("很遗憾，答错了")
        else:
            QMessageBox.about(self, "哎呀，稍等", "请选择游戏模式，并点击开始游戏")

    def startMyTimer(self, ms):
        self.timer_id = self.startTimer(ms)

    def timerEvent(self, *args, **kwargs):
        # 1. 获取当前的标签的内容
        if self.beginfg:

            try:
                current_sec = int(self.nz.text())
            except:
                return
            current_sec -= 1
            self.nz.setText(str(current_sec))
            print(current_sec)
            if current_sec <= 0:
                print("停止")
                self.killTimer(self.timer_id)
                self.label.setText("游戏结束，你输了")
                self.beginfg = False
                self.num1.setText("")
                self.num2.setText("")
                self.num3.setText("")
                self.num4.setText("")
        else:
            self.nz.setText("")



    def display_begin(self):
        self.beginfg=True
        if self.timer_id:
            self.killTimer(self.timer_id)
        if self.radioButton.isChecked() :
            self.label.setText("简单模式")

            self.nz.setText("")
            self.num = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
            self.num1.setText(str(self.num[0]))
            self.num2.setText(str(self.num[1]))
            self.num3.setText(str(self.num[2]))
            self.num4.setText(str(self.num[3]))
        elif self.radioButton_2.isChecked() :
            self.label.setText("倒计时60s")
            self.nz.setText("60")
            self.startMyTimer(1000)
            self.num = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
            self.num1.setText(str(self.num[0]))
            self.num2.setText(str(self.num[1]))
            self.num3.setText(str(self.num[2]))
            self.num4.setText(str(self.num[3]))

        elif self.radioButton_3.isChecked() :
            self.label.setText("倒计时30s")
            self.nz.setText("30")
            self.startMyTimer(1000)
            self.num = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
            self.num1.setText(str(self.num[0]))
            self.num2.setText(str(self.num[1]))
            self.num3.setText(str(self.num[2]))
            self.num4.setText(str(self.num[3]))


if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())