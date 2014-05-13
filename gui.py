# coding: utf-8
from Tkinter import *
from coding import MatrixMethod

class Gui(object):
	def __init__(self):		
		self.main()

	def main(self):
		self.root = Tk()
		self.root.title("ОТПДС")

		screenWidth = self.root.winfo_screenwidth()
		screenHeight = self.root.winfo_screenheight()
		windowWidth = 300
		windowHeight = 700

		x = (screenWidth/2) - (windowWidth/2)
		y = (screenHeight/2) - (windowHeight/2)

		self.root.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, x, y))

		Canvas(self.root).pack(fill = 'both', expand = 'yes')
		
		Label(self.root, text = 'Введите вашу матрицу:').place(x = 70, y = 20)
		
		self.matrix = Text(height = 5, width = 11)
		self.matrix.place(x = 100, y = 45)

		self.OKButton = Button(self.root, text = 'OK')
		self.OKButton.place(x = 120, y = 135)
		self.OKButton.bind('<Button-1>', self.matrixInit)

		Label(self.root, text = 'Текущая матрица:').place(x = 85, y = 175)

		self.currentMatrix = Label(self.root, text = '')
		self.currentMatrix.place(x = 100, y = 195)

		Label(self.root, text = 'Введите информационные символы:').place(x = 30, y = 275)

		self.information = Text(height = 1, width = 6)
		self.information.place(x = 120, y = 305)

		self.codingButton = Button(self.root, text = 'Кодировать')
		self.codingButton.place(x = 95, y = 335)
		self.codingButton.bind('<Button-1>', self.coding)

		Label(self.root, text = 'Кодовая комбинация:').place(x = 80, y = 375)

		self.codeLabel = Label(self.root, text = '', font = ('bold'))
		self.codeLabel.place(x = 75, y = 395)

		Label(self.root, text = 'Введите многочлен ошибок:').place(x = 60, y = 425)

		self.errors = Text(height = 1, width = 16)
		self.errors.insert(INSERT, '0' * 15)
		self.errors.place(x = 90, y = 450)

		self.decodingButton = Button(self.root, text = 'Декодировать')
		self.decodingButton.place(x = 90, y = 485)
		self.decodingButton.bind('<Button-1>', self.decoding)

		Label(self.root, text = 'Принятая комбинация:').place(x = 80, y = 525)

		self.decodeLabel = Label(self.root, text = '', font = ('bold'))
		self.decodeLabel.place(x = 75, y = 545)

		Label(self.root, text = 'Исправленная комбинация:').place(x = 65, y = 575)

		self.fixedLabel = Label(self.root, text = '', font = ('bold'))
		self.fixedLabel.place(x = 75, y = 595)

		self.errorInfo = Label(self.root, text = '')
		self.errorInfo.place(x = 90, y = 645)

		self.root.mainloop()

	def matrixInit(self, event):
		text = self.matrix.get('0.0', END)
		self.currentMatrix.config(text = text)

		self.matrixMethod = MatrixMethod(text.splitlines())

	def coding(self, event):
		information = self.information.get('0.0', END).splitlines()[0]

		code = self.matrixMethod.coding(information)
		code = ''.join(str(i) for i in code)

		self.codeLabel.config(text = code)

	def decoding(self, event):
		errors = self.errors.get('0.0', END).splitlines()[0]

		errorInfo, code, fixed = self.matrixMethod.decoding(errors)

		code = ''.join(str(i) for i in code)
		fixed = ''.join(str(i) for i in fixed)
		
		self.decodeLabel.config(text = code)
		self.fixedLabel.config(text = fixed)
		self.errorInfo.config(text = errorInfo)

def main():
	Gui()

if __name__ == '__main__':
	main()