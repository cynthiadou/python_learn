import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
from UI_calc import Ui_MainWindow

# 屏幕显示缓存
ulist = ''

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def ButtonAct(self):
        global ulist
        # 通过sender方法找到发送信号的按键
        sender = super(MainWindow, self).sender()
        # 判断按下的键并动作
        if sender.text() == '=':
            # 防止计算异常
            try:
                value = eval(ulist)
            except BaseException:
                ulist = 'ERROR'
            else:
                ulist = str(value)
        # 退出
        elif sender.text() == 'ESC':
            qApp.quit()
        # 清屏
        elif sender.text() == 'Clear':
            ulist = ''
        # 清除前一个字符和"backspace"共10个字符
        elif sender.text() == 'Backspace':
            ulist = ulist[:-1]
        # 增加输入的键到缓冲区
        else:
            ulist += sender.text()
        # 刷新结果
        self.ui.Result.setText(ulist)

if __name__=="__main__":  
    app = QApplication(sys.argv)  
    win = MainWindow()  
    win.show()  
    sys.exit(app.exec_())  
