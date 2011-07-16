#coding:utf-8


class Filmes(object):
    lista_filmes=[]
	
	

    
    def __init__(self, codigo_filme, titulo, duracao, ano, genero, diretor, artista):
        self.codigo_filme=codigo_filme
        self.titulo=titulo
        self.duracao=duracao
        self.ano=ano
        self.genero=genero
        self.diretor=diretor
        self.artista=artista       
        self.lista_fitas=[]




    def adicionar_filme(self, filme):
        self.lista_filmes.append(filme)


    def quantidade_de_fitas_do_filme(self):
        return self.lista_fitas.__len__()


    def adicionar_fita(self, fita):
        self.lista_fitas.append(fita)
 
    
    def adicionar_fita_em_filme(self, cod_filme, fita):
        for i in self.lista_filmes:
            if i.codigo_filme == cod_filme:
                self.adicionar_fita(fita)   



    def buscar_filme_por_diretor(self, diretor_filme):
        lista_encontrada=[]
        for i in Filmes.lista_filmes:
            if i.diretor.nome == diretor_filme:
                lista_encontrada.append(i)
            if lista_encontrada!=[]:
                return (lista_encontrada)




    def buscar_filmes_por_genero(self, genero_filme):
        lista_encontrada = []
        for i in Filmes.lista_filmes:
            if i.genero == genero_filme:
                lista_encontrada.append(i)
            if lista_encontrada != []:
                return lista_encontrada


    
    def buscar_filmes_por_artista(self, artista_filme):
        lista_encontrada=[]
        for i in Filmes.lista_filmes:
            if i.artista.nome == artista_filme:
                lista_encontrada.append(i)
            if lista_encontrada!=[]:
                return (lista_encontrada)
 	



    def listar_todos_os_filmes_e_quantidade_de_fitas(self):
        lista_encontrada = []
        for i in self.lista_filmes:
            lista_encontrada.append((i.titulo, i.quantidade_de_fitas_do_filme()))
        return lista_encontrada


