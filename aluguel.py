#coding: utf -8
from datetime import date
from filmes import Filmes

class Aluguel(object):
    lista_emprestimos=[]
   

    def __init__(self, codigo_aluguel, registro_socio, codigo_fita, data_emprestimo):
        self.codigo_aluguel = codigo_aluguel
        self.registro_socio = registro_socio
        self.codigo_fita = codigo_fita
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
        self.valor_pago = 3



    def emprestar_fita(self,aluguel):
        for filme in Filmes.lista_filmes:
            if str(filme.codigo_filme) == str(aluguel.codigo_fita).split(".")[0]:
                for fita in filme.lista_fitas:
                    if str(fita.codigo_fita) == aluguel.codigo_fita:
                        if fita.alugado == False:
                            fita.alugado = True
        self.lista_emprestimos.append(aluguel)



    def devolver_fita(self,identificacao_aluguel,dia,mes,ano):      
        for i in Aluguel.lista_emprestimos:
            for filme in Filmes.lista_filmes:
                if str(filme.codigo_filme) == str(i.codigo_fita).split(".")[0]:
                    for fita in filme.lista_fitas:
                        if str(fita.codigo_fita) == i.codigo_fita:
                            fita.alugado = False       
            if i.codigo_aluguel==identificacao_aluguel:
                i.data_devolucao = date(ano,mes,dia)
                resultado_data = i.data_devolucao - i.data_emprestimo
                #print ("resultado data", resultado_data.days)
                if resultado_data.days > 3 : #pagamento com multa
                    i.valor_pago=3
                    i.valor_pago = i.valor_pago + 1
                    return i.valor_pago
                elif resultado_data.days == 1:
                        i.valor_pago=3
                        i.valor_pago= i.valor_pago-2
                        return i.valor_pago
                elif resultado_data.days == 2:
                        i.valor_pago=3
                        i.valor_pago=i.valor_pago-1
                        return i.valor_pago
                elif resultado_data.days == 3:
                        i.valor_pago=3
                        i.valor_pago=i.valor_pago
                        return i.valor_pago



    



        
