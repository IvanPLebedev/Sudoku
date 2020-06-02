from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from sudoku import Sudoku

matrix1 = [
        [0,0,5,0,0,0,6,0,0],
        [6,0,0,0,1,0,0,0,3],
        [0,0,4,5,0,9,1,0,0],
        [0,7,0,0,0,0,0,6,0],
        [4,6,2,0,7,0,3,5,9],
        [0,3,0,0,0,0,0,1,0],
        [0,0,6,3,0,8,2,0,0],
        [7,0,0,0,2,0,0,0,6],
        [0,0,3,0,0,0,9,0,0],
        ]

class Root(BoxLayout):
	def solve_sudoku(self):
		#self.print_matr(matrix1)
		self.ids.label.text = 'Ждите, решаю...'
		matr = self.read_matr()
		sudoku = Sudoku(matr)
		if sudoku.solve():
			self.print_matr(sudoku.matrix)
			self.ids.label.text = 'Решение'
		else:
			self.ids.label.text = 'Решения нет!'

	
	def read_matr(self):
		#добавить обработку ошибок ввода
		res = []
		for i in range(9):
			line = []
			for j in range(9):
				text_input = self.ids['t{}_{}'.format(i, j)].text
				if text_input == '':
					line.append(0)
				else:
					line.append(int(text_input))
			res.append(line)
		return res
	
	def print_matr(self, matr):
		print(matr)
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