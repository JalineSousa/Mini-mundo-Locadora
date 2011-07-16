#coding:utf-8
import unittest
from should_dsl import should
from datetime import date
from fitas import Fitas
from filmes import Filmes
from artista import Artista
from diretor import Diretor



class Test_fitas(unittest.TestCase):


    def teste_fitas(self):
        fita1=Fitas ("1.30","10/10/10","ruim",False)
        fita1.codigo_fita |should| equal_to ("1.30")
        fita1.aquisicao |should| equal_to ("10/10/10")
        fita1.estado |should| equal_to ("ruim")
        fita1.alugado |should| equal_to (False)


    
        

    def test_listar_fitas_por_estado(self):
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        filme1 = Filmes(1,"Titanic","90","1998","Romance",diretor1,artista1)
        filme1.adicionar_filme(filme1)
        fita1 = Fitas("1.10",date(2010,12,28),"ruim",False)
        fita2 = Fitas("1.20",date(2010,12,28),"ruim",False)
        fita3 = Fitas("1.30",date(2010,12,28),"bom",False)
        filme1.adicionar_fita_em_filme(1,fita1)
        filme1.adicionar_fita_em_filme(1,fita2)
        filme1.adicionar_fita_em_filme(1,fita3)
        fita1.listar_fitas_por_estado("ruim") |should| equal_to([['Titanic',['1.10','1.20']]])

if __name__ =="__main__":
	unittest.main()
