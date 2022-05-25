#pylint:disable=E1101
from kivymd.app import MDApp
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.metrics import sp, dp
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.gridlayout import GridLayout
from functools import partial
from datetime import datetime


class ScrollLayout(StackLayout):
	def __init__(self, **kwargs):
		super().__init__()
		
		self.bind(minimum_height=self.setter('height'))
		self.size_hint_y = None


class MeuLabel(MDLabel):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)

    
    def on_size(self,*args):
        # vamos colocar um espaço de 10 sp
        self.text_size = (self.width - sp(20), None)
    
    def on_texture_size(self,*args):
        self.size = self.texture_size
        # vamos colocar um espaço a mais de 20sp
        self.height += sp(20)


class Inputa(TextInput):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.background_normal = 'img/inputbg.png'
		self.background_active = 'img/inputbga.png'
		self.font_size = '14dp'
		self.foreground_color = (.5,.5,.5)
		self.padding = '10dp'
		

class BannerMov(FloatLayout):
	def __init__(self, d, **kwargs):
		super().__init__(**kwargs)
		
		inf = MDLabel(text=f'''[b][size=15sp]{d['descrincao']}[/b][size=12sp]
{d['PV']} - {d['f.pgm']} - {d['quant']}x
Data: {d['data']}[/size]''')
		inf.pos_hint = {'right': .7, 'center_y': .5}
		inf.size_hint = (.67, .8)
		inf.color = (.5,.5,.5)
		inf.markup = True
		
		val = MDLabel(text=f"R$ {d['valor']:,.2f}")
		val.bold= True
		val.color = (.5,.5,.5)
		val.pos_hint = {'right': .98, 'center_y': .5}
		val.font_size = '15sp'
		val.halign = 'right'
		val.size_hint = (.28, .8)
		
		
		self.add_widget(inf)
		self.add_widget(val)
		

class ImageButton(ButtonBehavior, Image):
	pass
	

class LabelButton(ButtonBehavior, MDLabel):
	pass


class ImgaButtonLabel(ButtonBehavior, FloatLayout):
	
	def __init__(self, image='', label='', **kwargs):
		
		super().__init__(**kwargs)
		
		
		self.im = Image(source='img/transp.png')
		self.im.pos_hint = {"center_x": .5, "top": .1}
		self.im.size_hint = (.8, .03)
		self.im.allow_stretch = True
		self.im.keep_ratio = False
		self.add_widget(self.im)
		
		image = Image(source=image)
		image.pos_hint = {"center_x": .5, "top": .9}
		image.size_hint = (.7, .4)
		
		lab = MDLabel(text=label)
		lab.color = '#151515'
		lab.font_size = '10sp'
		lab.halign = 'center'
		lab.pos_hint = {"center_x": .5, "top": .5}
		lab.size_hint = (1, .4)
		
		self.add_widget(image)
		self.add_widget(lab)


class ImgaButtonLabelc(ButtonBehavior, FloatLayout):
	def __init__(self, image, label, ls='10dp', lfn='', fc='', **kwargs):
		super().__init__(**kwargs)
		
		image = Image(source=image)
		image.pos_hint = {"center_x": .5, "top": 1}
		image.size_hint = (1, 1)
		image.allow_stretch = True
		image.keep_ratio = False
		
		lab = MDLabel(text=label)
		lab.color = '#151515' if fc == '' else fc
		lab.font_size = ls
		if lfn != '':
			lab.font_name = lfn
		lab.halign = 'center'
		lab.pos_hint = {"center_x": .5, "center_y": .5}
		lab.size_hint = (1, 1)
		
		self.add_widget(image)
		self.add_widget(lab)


class PopComprasDiversas(Popup):
	def __init__(self, **kwargs):
		
		self.title = 'Nova Compra Comum'
		self.separator_height = 0
		self.title_align = 'center'
		self.title_color = (.5,.5,.5,1)
		self.title_size = '20dp'
		self.background = 'img/popbgw.png'
		self.ttt = 1
		
		super().__init__(**kwargs)
		
		tela = FloatLayout()

	# Descrincao
	
		self.innput = Inputa()
		self.innput.focus = True
		self.innput.font_size = '15dp'
		self.innput.multiline = False
		self.innput.hint_text = 'Descrinção'
		self.innput.hint_text_color = (.7,.7,.7)
		self.innput.size_hint = (.9, .08)
		self.innput.pos_hint = {'right': .93, 'top': 1}
		
		tela.add_widget(self.innput)
		
	# Observacoes
	
		self.iobs = Inputa()
		self.iobs.hint_text = 'Obs:'
		self.iobs.hint_text_color = (.7,.7,.7)
		self.iobs.font_size = '13dp'
		self.iobs.size_hint = (.9, .12)
		self.iobs.pos_hint = {'right': .93, 'top': .93}
		
		tela.add_widget(self.iobs)
		
	# Valor
		
		self.va = FloatLayout()
		self.va.pos_hint = {"center_x": .5, "top": .65}
		self.va.size_hint = (1, .53)
		
		self.val = '0'
		self.valor = MDLabel(text=f'R$: {float(int(self.val)):,.2f}')
		self.valor.bold = True
		self.valor.color = (.7,.7,.7)
		self.valor.font_size = '30dp'
		self.valor.halign = 'center'
		self.valor.pos_hint = {"center_x": .5, "top": 1}
		self.valor.size_hint = (1, .2)
		
		self.va.add_widget(self.valor)
		
		numeros = GridLayout(cols=3)
		numeros.pos_hint = {"center_x": .5, "top": .8}
		numeros.size_hint = (.9, .8)
		
		for numero in [1,2,3,4,5,6,7,8,9,'C',0,'.']:
			n = ImgaButtonLabelc(image='img/b.png', label=str(numero), ls='15dp')
			if numero != 'C':
				n.on_release = partial(self.add, numero)
			else:
				n.on_release = self.apagar
			numeros.add_widget(n)
		
		self.va.add_widget(numeros)
		tela.add_widget(self.va)
	
	# Botoes Salvar/cancelar
		
		badd = ImgaButtonLabelc(image='img/bgreen.png', label='Salvar', ls='15dp', fc='Ffffff')
		badd.pos_hint = {"center_x": .33, "top": .1}
		badd.color = (1,1,1)
		badd.size_hint = (.5, .08)
		badd.on_release = self.salvar
		
		tela.add_widget(badd)
		
		bcan = ImgaButtonLabelc(image='img/bred.png', label='Cancelar', ls='15dp', fc='Ffffff')
		bcan.pos_hint = {"center_x": .78, "top": .1}
		bcan.color = (1,1,1)
		bcan.size_hint = (.3, .08)
		bcan.on_release = self.cancelar
		
		tela.add_widget(bcan)
	
	# botoes avista/parcelado
		
		but = GridLayout(rows=1)
		but.pos_hint = {'right': .9, 'top': .8}
		but.size_hint = (.8, .1)
		
		self.CV = ImgaButtonLabel(image='img/money.png', label='Á Vista')
		self.CV.im.source = 'img/green.png'
		self.CV.on_release = partial(self.VP, 1)
		but.add_widget(self.CV)
		
		self.CP = ImgaButtonLabel(image='img/card.png', label='Á Prazo / Parcelado')
		self.CP.on_release = partial(self.VP, 2)
		but.add_widget(self.CP)
		
		tela.add_widget(but)
		
		self.quant = FloatLayout()
		self.quant.size_hint = (.9, .1)
		self.quant.pos_hint = {'right': .95, 'top': 50}
		
		self.fp = MDLabel(text='F. Pagamento:')
		self.fp.font_size = '12dp'
		self.fp.color= (.5,.5,.5)
		self.fp.bold= True
		self.fp.halign = 'right'
		self.fp.size_hint = ( .3, .33)
		self.fp.pos_hint = {'right': .3, 'center_y': .825}
		self.quant.add_widget(self.fp)
	
		self.listafp = Spinner()
		self.listafp.background_color = (1,1,1,.08)
		self.listafp.bold = True
		self.listafp.halign = 'left'
		self.listafp.color = (.5,.5,.5)
		self.listafp.values = ['Boleto', 'Promissoria', 'Outros', 'Cartao 1', 'Cartao 2']
		self.listafp.size_hint = ( .68, .33)
		self.listafp.pos_hint = {'right': 1, 'center_y': .825}
		self.quant.add_widget(self.listafp)
		
		self.quantidade = MDLabel(text='Quantidade:')
		self.quantidade.font_size = '12dp'
		self.quantidade.color= (.5,.5,.5)
		self.quantidade.bold= True
		self.quantidade.halign = 'right'
		self.quantidade.size_hint = ( .3, .33)
		self.quantidade.pos_hint = {'right': .3, 'center_y': .495}
		self.quant.add_widget(self.quantidade)
		
		self.nparcela = Spinner()
		self.nparcela.text = '1'
		self.nparcela.background_color = (1,1,1,.08)
		self.nparcela.bold = True
		self.nparcela.halign = 'left'
		self.nparcela.color = (.5,.5,.5)
		self.nparcela.values = [f'{n}' for n in range(1, 360)]
		self.nparcela.size_hint = ( .68, .33)
		self.nparcela.pos_hint = {'right': 1, 'center_y': .495}
		self.quant.add_widget(self.nparcela)
		
		self.dpg = MDLabel(text='D. Vencimento:')
		self.dpg.font_size = '12dp'
		self.dpg.color= (.5,.5,.5)
		self.dpg.bold= True
		self.dpg.halign = 'right'
		self.dpg.size_hint = ( .3, .33)
		self.dpg.pos_hint = {'right': .3, 'center_y': .165}
		self.quant.add_widget(self.dpg)
		
		self.idpg = Spinner()
		self.idpg.text = str(datetime.now().day)
		self.idpg.background_color = (1,1,1,.08)
		self.idpg.bold = True
		self.idpg.halign = 'left'
		self.idpg.color = (.5,.5,.5)
		self.idpg.values = [f'{n}' for n in range(1, 32)]
		self.idpg.size_hint = ( .68, .33)
		self.idpg.pos_hint = {'right': 1, 'center_y': .165}
		self.quant.add_widget(self.idpg)
		
		tela.add_widget(self.quant)
		
	# End	
		
		self.auto_dismiss = False
		self.content = tela
		self.size_hint = (.9, .9)
	
# Selecionar A Vista / Parcelado
	
	def VP(self, tip):
		if tip == 1:
			
			self.quant.pos_hint = {'right': .95, 'top': 50}
			self.va.pos_hint = {"center_x": .5, "top": .65}
			self.va.size_hint = (1, .53)
			self.CP.im.source = 'img/transp.png'
			self.CV.im.source = 'img/green.png'
		else:
			
			self.quant.pos_hint = {'right': .95, 'top': .67}
			self.va.pos_hint = {"center_x": .5, "top": .55}
			self.va.size_hint = (1, .43)
			self.ttt = 2
			self.CV.im.source = 'img/transp.png'
			self.CP.im.source = 'img/green.png'
			
		self.ttt = tip


# adicionar valores

	def add(self, n):
		if n == '.' and '.' in self.val or n == '.' and self.val == '0':
			return 
		if self.val == '0':
			self.val = str(n)
		else:
			self.val += str(n)
		self.valor.text = f'R$: {float(self.val):,.2f}'

# Apagar Valor

	
	def apagar(self):
		self.val = '0'
		self.valor.text = f'R$: {float(self.val):,.2f}'
	
# confirmar salvar

	def salvar(self):
		if self.innput.text == '':
			self.innput.hint_text_color = 'red'
			return 
		
		if self.listafp.text == '' and self.ttt == 2:
			self.fp.color = 'red'
			return 
			
		if self.val == '0':
			self.valor.color = (1,0,0)
			return 
		
		d = {"data": datetime.now().strftime('%d/%m/%Y'), "descrincao": self.innput.text, "obs": self.iobs.text, "PV": "A Vista" if self.ttt == 1 else "A Prazo", "f.pgm": self.listafp.text if self.ttt == 2 else "Dinheiro/Debito", "dia_vencimento": self.idpg.text, "quant": self.nparcela.text if self.ttt == 2 else '1', "valor": float(self.val), "valor_total": float(self.val)*int(self.nparcela.text) if self.ttt == 2 else float(self.val)}
		
		lb = f'''
[b]Data[/b] {d['data']}
[b]Descrinção[/b]: {d['descrincao']}
[b]Obs[/b]: {d['obs']}
[b]Tipo de Compra[/b]: {d['PV']}
[b]Dia de Vencimento[/b]: {d['dia_vencimento']}
[b]Forma de Pagamento[/b]: {d['f.pgm']}
[b]Quantidade[/b]: {d['quant']}x
[b]Valor/M[/b]: R${float(d['valor']):,.2f}
[b]Valor Total[/b]: R${float(d['valor'])*int(d['quant']):,.2f}
'''
		
		pg = Popup()
		pg.background = self.background
		pg.title = 'Confirmar Compra'
		pg.title_size = '14dp'
		pg.title_align = 'center'
		pg.title_color = (.5,.5,.5)
		pg.separator_height = 0
		
		ff = FloatLayout()
		
		i = Image(source='img/$.png')
		i.pos_hint = {"center_x": .5, "top": 1}
		i.size_hint = (.9, .2)
		ff.add_widget(i)
		
		des = MDLabel(text=lb)
		des.halign = 'center'
		des.markup = True
		des.font_size = '13dp'
		des.color = (.6,.6,.6)
		des.pos_hint = {"center_x": .5, "top": .8}
		des.size_hint = (.9, .6)
		ff.add_widget(des)
		
		badd = ImgaButtonLabelc(image='img/bgreen.png', label='Confirmar', ls='15dp', fc='Ffffff')
		badd.pos_hint = {"center_x": .5, "top": .18}
		badd.color = (1,1,1)
		badd.size_hint = (.5, .13)
		badd.on_release = partial(self.gravar, d)
		badd.on_press = pg.dismiss
		ff.add_widget(badd)
		
		pg.content = ff
		pg.size_hint = (.85,.5)
		
		pg.open()
		
# gravar
	
	def gravar(self, d):
		app = MDApp.get_running_app()
		app.lista_compra.append(d)
		app.carregar_lista()
		self.auto_dismiss = True
		self.dismiss()
		

# Cancelar
	
	def cancelar(self):
		self.auto_dismiss = True
		self.dismiss()