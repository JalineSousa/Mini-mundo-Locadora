#coding: utf -8
import unittest
from should_dsl import should
from artista import Artista


class Test_artista(unittest.TestCase):


	def test_criar_artista(self):
		artista1=Artista("Antônio","Brasil","12/12/1970")
		artista1.nome |should| equal_to ("Antônio")
		artista1.pais |should| equal_to ("Brasil")
		artista1.data_nascimento |should| equal_to ("12/12/1970")



if __name__ =="__main__":
	unittest.main()    
    
