#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from PyQt4 import QtGui,QtCore

'''app=QtGui.QApplication(sys.argv)
w=QtGui.QWidget()
w.resize(300,250)
w.move(200,100)
w.setWindowTitle('code10')
w.show()
sys.exit(app.exec_())'''
class Index(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		#设置窗口大小和位置
		self.setGeometry(600,100,400,650)
		#设置窗口名字
		self.setWindowTitle(u'code10代码')
		#设置窗口图标
		self.setWindowIcon(QtGui.QIcon('../pic/0321.png'))
		#设置窗口提示(代码不起作用)
		#self.setToolTip(u'This is a<b>QWidget</b>widget')
		#QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish',20))
		#创建按钮 
		quit=QtGui.QPushButton(u'点击关闭',self)
		#创建按钮位置
		quit.setGeometry(0,0,60,35)
		#点击按钮关闭(PyQt4的事件处理系统建立在信号-槽机制之上)
		self.connect(quit,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))
	#关闭窗口的方法
	def closeEvent(self,event):
			#关闭窗口触发closeEvent方法
			reply=QtGui.QMessageBox.question(self,u'提示',u"你确定关闭吗？",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
			#第一个字符串参数提示在消息窗口的标题栏显示，
			#第二个字符串参数一对话的形式显示在消息窗口中
			#返回的结果被保存在reply变量中
			if reply==QtGui.QMessageBox.Yes:
				#同意
				event.accept()
			else:
				#忽视
				event.ignore()
					
app=QtGui.QApplication(sys.argv)
index=Index()
index.show()
sys.exit(app.exec_())
