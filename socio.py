#coding: utf -8
from aluguel import Aluguel

class Socio(object):
    lista_socios = []

    def __init__(self, registro, nome, endereco, telefone):
        self.registro=registro
        self.nome=nome
        self.endereco=endereco
        self.telefone=telefone


    
    def adicionar_socio(self, socio):
        Socio.lista_socios.append(socio)


    def lista_de_socios_inadimplentes(self,data_hoje):
        lista_codigos_socios_inadimplentes = []
        for i in Aluguel.lista_emprestimos:
            if i.data_devolucao == None:
                resultado_data = data_hoje - i.data_emprestimo
                dias = resultado_data.days
                if dias > 3:
                    lista_codigos_socios_inadimplentes.append(i.registro_socio)
        if lista_codigos_socios_inadimplentes != []:
            lista_socios_inadimplentes = []
            for socio in self.lista_socios:
                for cod_socio in lista_codigos_socios_inadimplentes:
                    if str(socio.registro) == str(cod_socio):
                        lista_socios_inadimplentes.append(socio)
            return lista_socios_inadimplentes
        else:
            return None
       


