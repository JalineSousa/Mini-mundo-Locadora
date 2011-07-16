#coding: utf -8


class Diretor(object):
    lista_diretores=[]
    
    def __init__(self, nome, pais, data_nascimento):
        self.nome=nome
        self.pais=pais
        self.data_nascimento=data_nascimento

