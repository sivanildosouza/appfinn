from kivymd.app import MDApp
from kivy.lang import Builder

from classes import *
from telas import *



		
	


class MyApp(MDApp):
	
	lista_compra = []
	
	def build(self):
		return Builder.load_file('main.kv')

	
	def on_start(self):
		self.p_home = self.root.ids['homepage'].ids
		
		self.carregar_botoes_home()
		self.carregar_lista()
	
	def carregar_botoes_home(self):
		
		NCD = ImgaButtonLabel(image='img/+.png', label='Adicionar Gastos Diversos')
		NCD.on_release = self.add_contas_diversas
		self.p_home['bot'].add_widget(NCD)
		
		ADF = ImgaButtonLabel(image='img/$.png', label='Adicionar Despesas Fixas')
		#ADF.on_release = print()
		self.p_home['bot'].add_widget(ADF)
		
		NGA = ImgaButtonLabel(image='img/food.png', label='Gastos com Alimentacão')
		#NGA.on_release = print()
		self.p_home['bot'].add_widget(NGA)
		
		NR = ImgaButtonLabel(image='img/money+.png', label='Adicionar Nova Renda')
		#NR.on_release = print()
		self.p_home['bot'].add_widget(NR)
		
		
	def carregar_lista(self):
		lista = self.p_home['gridmov']
		
		lista.clear_widgets()
		
		for c in self.lista_compra:
			lista.add_widget(BannerMov(c))
			
	
	def add_contas_diversas(self):
		pop = PopComprasDiversas()
		pop.open()
		
		
		
		
MyApp().run()
		
		