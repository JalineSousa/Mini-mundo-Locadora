#coding:utf-8
import unittest
from should_dsl import should
from filmes import Filmes
from diretor import Diretor
from artista import Artista
from fitas import Fitas
from socio import Socio
from aluguel import Aluguel
from datetime import date





class Test_filmes(unittest.TestCase):




    def test_filmes(self):
        filme1=Filmes("10","E o vento levou", "90", "2000", "Drama", "Joao", "Maria e Jose")
        filme1.codigo_filme |should| equal_to ("10")
        filme1.titulo |should| equal_to ("E o vento levou")
        filme1.duracao |should| equal_to ("90")
        filme1.ano |should| equal_to ("2000")
        filme1.genero |should| equal_to ("Drama")
        filme1.diretor |should| equal_to ("Joao")
        filme1.artista |should| equal_to ("Maria e Jose")

    def test_adicionar_filme(self):
        Filmes.lista_filmes=[]
        diretor1=Diretor("Lucas","Brasil","12/09/1970")
        artista1=Artista ("Mario","Holanda","12/09/1975")
        filme1=Filmes("20","Titanic","120","1998","Romance", diretor1, artista1)
        filme1.adicionar_filme(filme1)
        Filmes.lista_filmes[0].titulo |should| equal_to ("Titanic")

    
    def test_adicionar_fita(self):
        Filmes.lista_filmes=[]
        diretor1=Diretor("Lucas","Brasil","12/09/1970")
        artista1=Artista ("Mario","Holanda","12/09/1975")
        filme1=Filmes("11","House","60", "1999", "Comédia", diretor1, artista1)
        fita1 = Fitas ("001", "14/03/10", "ruim", False)
        filme1.adicionar_fita(fita1)
        filme1.lista_fitas[0].codigo_fita |should| equal_to("001")

  
    
    def test_adicionar_fita_em_filme(self):
        Filmes.lista_filmes=[]  
        diretor1=Diretor("Lucas","Brasil","12/09/1970")
        artista1=Artista ("Mario","Holanda","12/09/1975")   
        filme1 = Filmes("10","House","90","2009","Terror",diretor1, artista1)
        filme1.adicionar_filme(filme1)
        fita1 = Fitas("100","12/12/09","bom", False)
        filme1.adicionar_fita_em_filme("10",fita1)
        filme1.lista_fitas[0].codigo_fita |should| equal_to ("100")


   
   
    def test_buscar_filme_por_diretor(self):
        Filmes.lista_filmes=[]
        diretor1 = Diretor("Lucas","Brasil","12/09/1970")
        artista1=Artista ("Mario","Holanda","12/09/1975")        
        diretor2 = Diretor ("Mateus", "Canada", "13/05/1975")
        artista2=Artista ("Marcelo","Argentina","16/05/1971")
        filme1 = Filmes ("10","Future","90","2001","Drama",diretor1, artista1)
        filme2 = Filmes("20", "Past", "120", "2002","Drama", diretor2, artista2)
        filme1.adicionar_filme(filme1)
        filme2.adicionar_filme(filme2)
        #print Filmes.lista_filmes        
        filme1.buscar_filme_por_diretor("Lucas") |should| equal_to ([filme1])


    def test_buscar_filme_por_genero(self):
        Filmes.lista_filmes=[]
        diretor1 = Diretor("Lucas","Brasil","12/09/1970")
        diretor2 = Diretor ("Mateus", "Canada", "13/05/1975")
        artista1=Artista ("Mario","Holanda","12/09/1975")
        artista2=Artista ("Mercedes","Mexico","20/09/1980")
        filme1=Filmes("30","Volta ao mundo","120","2007","Aventura",diretor1, artista1)
        filme2=Filmes("40","A hora do rush 2","120","2008","Ação",diretor2, artista2)
        filme1.adicionar_filme(filme1)
        filme2.adicionar_filme(filme2)
        filme2.buscar_filmes_por_genero("Ação") |should| equal_to ([filme2])


    
    def test_buscar_filme_por_artista(self):
        Filmes.lista_filmes=[]
        diretor1 = Diretor("Lucas","Brasil","12/09/1970")
        diretor2 = Diretor ("Mateus", "Canada", "13/05/1975")
        artista1 = Artista("Luana","Brasil","12/09/1970")
        artista2 = Artista ("Marcos", "Canada", "13/05/1975")
        filme1 = Filmes ("10","Future","90","2001","Drama",diretor1, artista1)
        filme2 = Filmes("20", "Past", "120", "2002","Drama", diretor2, artista2)
        filme1.adicionar_filme(filme1)
        filme2.adicionar_filme(filme2)
        filme1.buscar_filmes_por_artista("Luana") |should| equal_to ([filme1]) 

    
    

    def test_listar_todos_os_filmes_e_quantidade_de_fitas(self):
        Filmes.lista_filmes=[]
        diretor1 = Diretor("Joao","Brasil","12/08/1980")
        diretor2 = Diretor("Maria","Brasil","09,10,1988")
        diretor3 = Diretor("Jose","Brasil","12/04/1986")
        artista1 = Artista("Artista A","Brasil","19/03/1999")
        artista2 = Artista("Artista B","Brasil","18/02/1990")
        artista3 = Artista("Artista C","Brasil","12/05/1982")
        filme1 = Filmes("1","Poeira em alto mar","120","2010","Comedia",diretor1,artista1)
        filme2 = Filmes("2","A volta dos que não foram","120","2011","Comedia",diretor2,artista2)
        filme3 = Filmes("3","As tranças do careca","120","2011","Comedia",diretor3,artista3)
        filme1.adicionar_filme(filme1)
        filme2.adicionar_filme(filme2)
        filme3.adicionar_filme(filme3)
        fita1 = Fitas("10","2010,12,28","bom",False)
        fita2 = Fitas("20","2010,12,28","ruim", False)        
        filme1.adicionar_fita_em_filme("1",fita1)
        filme1.adicionar_fita_em_filme("1",fita2)
        filme1.listar_todos_os_filmes_e_quantidade_de_fitas() |should| equal_to([("Poeira em alto mar",2),("A volta dos que não foram",0),("As tranças do careca",0)])

     


if __name__ =="__main__":
	unittest.main()
