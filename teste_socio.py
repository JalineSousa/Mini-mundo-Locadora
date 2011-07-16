#coding:utf-8
import unittest
from should_dsl import should
from datetime import date
from datetime import timedelta
from socio import Socio
from diretor import Diretor
from artista import Artista
from fitas import Fitas
from aluguel import Aluguel
from filmes import Filmes




class Test_socio(unittest.TestCase):


	def test_criar_socio(self):
		jaline = Socio("001","Jaline Sousa", "Rua zzz", "27267527")
		jaline.registro |should| equal_to ("001")
		jaline.nome |should| equal_to("Jaline Sousa")
		jaline.endereco |should| equal_to("Rua zzz")
		jaline.telefone |should| equal_to("27267527")
		demetrio = Socio("002","Vinicius Demetrio", "Rua vvv", "81246991")
		demetrio.registro |should| equal_to ("002")
		demetrio.nome |should| equal_to("Vinicius Demetrio")
		demetrio.endereco |should| equal_to("Rua vvv")
		demetrio.telefone |should| equal_to("81246991")

    
	def test_adicionar_socio(self):
		socio1 = Socio("1000","Maria","yyy","27267527")
		socio1.adicionar_socio(socio1)
		socio1.lista_socios[0].registro |should| equal_to ("1000")


	def test_lista_de_socios_inadimplentes(self):
		Filmes.lista_filmes=[]
		Aluguel.lista_emprestimos=[]
		diretor1 = Diretor("Joao","Brasil","12/08/1980")
		artista1 = Artista("Artista A","Brasil","19/03/1999")
		filme1 = Filmes(1,"Poeira em alto mar","120","2010","Comedia",diretor1,artista1)
		filme1.adicionar_filme(filme1)
		fita1 = Fitas("1.0","2010,12,28","bom",False)       
		filme1.adicionar_fita_em_filme(1,fita1)
		socio1 = Socio("100","Jaline","Rua xxx","99000000")
		socio1.adicionar_socio(socio1)
		aluguel1=Aluguel ("1000","100","1.0",date(2011,07,05))
		aluguel1.emprestar_fita(aluguel1)
		aluguel1.lista_emprestimos |should| equal_to([aluguel1])
		socio1.lista_de_socios_inadimplentes(date(2011,07,10)) |should| equal_to ([socio1])


    
	def test_lista_de_socios_inadimplentes_com_resultado_None(self):
		Filmes.lista_filmes=[]
		Aluguel.lista_emprestimos=[]
		diretor1 = Diretor("Joao","Brasil","12/08/1980")
		artista1 = Artista("Artista A","Brasil","19/03/1999")
		filme1 = Filmes(1,"Poeira em alto mar","120","2010","Comedia",diretor1,artista1)
		filme1.adicionar_filme(filme1)
		fita1 = Fitas("1.0","2010,12,28","bom",False)       
		filme1.adicionar_fita_em_filme(1,fita1)
		socio1 = Socio("100","Jaline","Rua xxx","99000000")
		socio1.adicionar_socio(socio1)
		aluguel1=Aluguel ("1000","100","1.0",date(2011,07,07))
		aluguel1.emprestar_fita(aluguel1)
		aluguel1.lista_emprestimos |should| equal_to([aluguel1])
		socio1.lista_de_socios_inadimplentes(date(2011,07,10)) |should| equal_to (None)

  

if __name__ =="__main__":
	unittest.main()
