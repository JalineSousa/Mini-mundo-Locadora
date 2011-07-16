#coding:utf-8
from filmes import Filmes

class Fitas(object):
	#lista_filmes_encontrada=[] 
	#lista_fitas_encontrada=[]


	def __init__(self,  codigo_fita, aquisicao, estado, alugado):
		self.codigo_fita = codigo_fita
		self.aquisicao = aquisicao
		self.estado = estado
		self.alugado = False


     

	def listar_fitas_por_estado(self, estado_fita):
		lista_filmes_encontrada=[]
		for i in Filmes.lista_filmes:
			lista_fitas_encontrada = []
			if i.lista_fitas != []:
				for j in i.lista_fitas:
					if j.estado == estado_fita:
						lista_fitas_encontrada.append(str(j.codigo_fita))
				lista_filmes_encontrada.append([i.titulo, lista_fitas_encontrada])
    			return lista_filmes_encontrada

    
   

        

