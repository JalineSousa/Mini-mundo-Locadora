#coding: utf -8
import unittest
from should_dsl import should
from diretor import Diretor


class Test_diretor(unittest.TestCase):

	def test_criar_diretor(self):
		diretor1=Diretor("Joao", "EUA", "15/03/1980")
		diretor1.nome |should| equal_to ("Joao")
		diretor1.pais |should| equal_to ("EUA")
		diretor1.data_nascimento |should| equal_to ("15/03/1980")



if __name__=="__main__":
    unittest.main()
