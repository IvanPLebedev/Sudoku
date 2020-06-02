from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from sudoku import Sudoku

class Root(BoxLayout):
	def solve_sudoku(self):
		self.ids.label.text = 'Ждите, решаю...'
		matr = self.read_matr()
		
	
	def read_matr(self):
		res = []
		for i in range(9):
			line = []
			for j in range(9):
				text_input = self.ids['t{}_{}'.format(i, j)].text
				line.append(text_input)
			res.append(line)
		return res

		
class SudokuApp(App):
	def build(self):
		root = Root()
		return root

if __name__ == "__main__":
    SudokuApp().run()