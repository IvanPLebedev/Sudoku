from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from sudoku import Sudoku
from utils import InputError

class Root(BoxLayout):
	# решать судоку
	def solve_sudoku(self):
		self.ids.label.text = 'Ждите, решаю...'
		try: 
			matr = self.read_matr()
			sudoku = Sudoku(matr)
			if sudoku.solve():
				self.print_matr(sudoku.matrix)
				self.ids.label.text = 'Решение'
			else:
				self.ids.label.text = 'Решения нет!'
		except InputError as e:
			self.ids.label.text = e.msg
		
	# очистить экран ввода
	def clear(self):
		self.ids.label.text = 'Введите матрицу судоку.'
		matr = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        ]
		self.print_matr(matr)

	# прочитать матрицу судоку с экрана ввода
	def read_matr(self):
		res = []
		for i in range(9):
			line = []
			for j in range(9):
				text_input = self.ids['t{}_{}'.format(i, j)].text
				if text_input == '':
					line.append(0)
				else:
					try:
						number = int(text_input)
					except:
						raise InputError('Ошибка ввода в {} строке {} строке'.format(i + 1, j + 1))
					if 0 < number < 10:
						line.append(number)
					else:
						raise InputError('Ошибка ввода в {} строке {} строке'.format(i + 1, j + 1))
			res.append(line)
		return res
	
	# вывести на экран
	def print_matr(self, matr):
		for i in range(9):
			for j in range(9):
				if matr[i][j] != 0:
					self.ids['t{}_{}'.format(i, j)].text = str(matr[i][j])
				else:
					self.ids['t{}_{}'.format(i, j)].text = ''

class SudokuApp(App):
	def build(self):
		root = Root()
		return root

if __name__ == "__main__":
    SudokuApp().run()