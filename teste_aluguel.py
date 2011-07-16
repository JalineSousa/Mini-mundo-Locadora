#coding:utf-8
import unittest
from should_dsl import should
from datetime import date
from datetime import timedelta
from aluguel import Aluguel
from fitas import Fitas
from diretor import Diretor
from artista import Artista
from socio import Socio
from filmes import Filmes





class Test_aluguel(unittest.TestCase):

    def test_aluguel(self):
        aluguel1 = Aluguel ("1000", "001", "003", "07/07/07")
        aluguel1.codigo_aluguel |should| equal_to ("1000")
        aluguel1.registro_socio |should| equal_to ("001")
        aluguel1.codigo_fita |should| equal_to ("003")
        aluguel1.data_emprestimo |should| equal_to ("07/07/07")



    def test_emprestar_fita(self):
        Filmes.lista_filmes=[]
        diretor1 = Diretor("Joao","Brasil","12/08/1980")
        artista1 = Artista("Artista A","Brasil","19/03/1999")
        filme1 = Filmes(1,"Poeira em alto mar","120","2010","Comedia",diretor1,artista1)
        filme1.adicionar_filme(filme1)
        fita1 = Fitas("1.0","2010,12,28","bom",False)       
        filme1.adicionar_fita_em_filme(1,fita1)
        aluguel1=Aluguel ("1000","100","1.0",date(2011,12,01))
        aluguel1.emprestar_fita(aluguel1)
        filme1.lista_fitas[0].alugado |should| equal_to(True)


    def test_devolver_fita_com_multa(self):
        Filmes.lista_filmes=[]
        diretor1 = Diretor("Joao","Brasil","12/08/1980")
        artista1 = Artista("Artista A","Brasil","19/03/1999")
        filme1 = Filmes(1,"Poeira em alto mar","120","2010","Comedia",diretor1,artista1)
        filme1.adicionar_filme(filme1)
        fita1 = Fitas("1.0","2010,12,28","bom",False)       
        filme1.adicionar_fita_em_filme(1,fita1)
        aluguel1=Aluguel ("1000","100","1.0",date(2011,12,01))
        aluguel1.emprestar_fita(aluguel1)
        aluguel1.devolver_fita("1000",05,12,2011)
        filme1.lista_fitas[0].alugado |should| equal_to (False)
        aluguel1.lista_emprestimos[0].valor_pago |should| equal_to (4)




    
    def test_devolver_fita_sem_multa(self):
        Filmes.lista_filmes=[]
        diretor1 = Diretor("Joao","Brasil","12/08/1980")
        artista1 = Artista("Artista A","Brasil","19/03/1999")
        filme1 = Filmes(1,"Poeira em alto mar","120","2010","Comedia",diretor1,artista1)
        filme1.adicionar_filme(filme1)
        fita1 = Fitas("1.0","2010,12,28","bom",False)       
        filme1.adicionar_fita_em_filme(1,fita1)
        aluguel1=Aluguel ("1000","100","1.0",date(2011,12,01))
        aluguel1.emprestar_fita(aluguel1)
        aluguel1.devolver_fita("1000",02,12,2011)
        filme1.lista_fitas[0].alugado |should| equal_to (False)
        aluguel1.lista_emprestimos[0].valor_pago |should| equal_to (1)

if __name__ =="__main__":
	unittest.main()


