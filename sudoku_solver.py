from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from sudoku import Sudoku
from utils import InputError
from threading import Thread
from kivy.clock import mainthread

from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class Root(BoxLayout):
	# нажатие кнопки Решить
	def touch_solve(self):
		self.update_label_text('Ждите, решаю...')
		try: 
			matr = self.read_matr()
			Thread(target=self.solve_sudoku, args=(matr,)).start()	
		except InputError as e:
			self.update_label_text(e.msg)
	
	# решать судоку
	def solve_sudoku(self, matr):
		sudoku = Sudoku(matr)
		if sudoku.check() == False:
			self.update_label_text('Решения нет. Неправильая матрица.')
		elif sudoku.solve():
			self.print_matr(sudoku.matrix)
			self.update_label_text('Решение')
		else:
			self.update_label_text('Решения нет!')
	
	@mainthread
	def update_label_text(self, new_text):
		self.ids.label.text = new_text
		
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
						if 0 < number < 10:
							line.append(number)
						else:
							raise InputError('Ошибка значения в {} строке {} столбце!'.format(i + 1, j + 1))
					except:
						raise InputError('Ошибка значения в {} строке {} столбце!'.format(i + 1, j + 1))
					
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