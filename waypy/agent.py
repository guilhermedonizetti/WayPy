"""This module is responsible for calling each method as needed."""

from waypy.methods import busca

class Agente(busca):

    starting_points = []
    arrival_points = []
    nodes = []
    graphs = []

    #Inicializa as listas que sao de valores padrao
    def __init__(self):
                
        #Declara o nome dos metodos a serem escolhidos para comparar com a entrada
        self.methods = ["AMPLITUDE", "PROFUNDIDADE", "PROFUNDIDADE LIMITADA",
                   "APROFUNDAMENTO ITERATIVO", "BIDIRECIONAL"]

        #Declara o nome dos metodos a serem chamados para executar
        self.methods_main = ["amplitude", "profundidade", "profundidade_limitada",
                        "aprofundamento_iterativo", "bidirecional"]
        
        #Inicia a lista que vai receber as rotas
        self.route_starting =  self.route_arrival = []


    def encontrar_atendimento(self, cidade_final, metodo, limite=False):
        """Metodo para encontrar um caminho entre a cidade que recebeu a AH e o hospital mais proximo.
        Recebe a cidade que teve a ajuda humanitaria e realiza as tentativas de gerar
        uma rota partindo dessa cidade ate a mais proxima dentre as da lista 'arrival_points'."""

        tam_caminho = 100000

        #se escolher Amplitude
        if metodo == self.methods[0]:
            for i in self.arrival_points: #para cada cidade da lista tenta um caminho...
                caminho = self.amplitude(cidade_final.upper(), i, self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #se escolher Profundidade
        if metodo == self.methods[1]:
            for i in self.arrival_points: #para cada cidade da lista tenta um caminho...
                caminho = self.profundidade(cidade_final.upper(), i, self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #se escolher Profundidade Limitada
        if metodo == self.methods[2]:
            for i in self.arrival_points: #para cada cidade da lista tenta um caminho...
                caminho = self.profundidade_limitada(cidade_final.upper(), i, 4, self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #se escolher Aprofundamento iterativo
        if metodo == self.methods[3]:
            for i in self.arrival_points: #para cada cidade da lista tenta um caminho...
                caminho = self.aprofundamento_iterativo(cidade_final.upper(), i, self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #se escolher Bidirecional
        if metodo == self.methods[4]:
            for i in self.arrival_points: #para cada cidade da lista tenta um caminho...
                caminho = self.bidirecional(cidade_final.upper(), i, self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting

    def encontrar_ajuda_humanitaria(self, cidade_final, metodo, limite=False):
        """Metodo para encontrar um caminho entre dois pontos.
        Recebe a cidade que precisa da ajuda humanitaria e realiza as tentativas
        de gerar uma rota partindo das cidades da lista 'starting_points' usando menos Memoria."""
        
        tam_caminho = 100000

        #se escolher Amplitude
        if metodo == self.methods[0]:
            for i in self.starting_points: #para cada cidade da lista tenta um caminho...
                caminho = self.amplitude(i, cidade_final.upper(), self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #se escolher Profundidade
        if metodo == self.methods[1]:
            for i in self.starting_points: #para cada cidade da lista tenta um caminho...
                caminho = self.profundidade(i, cidade_final.upper(), self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #se escolher Profundidade Limitada
        if metodo == self.methods[2]:
            for i in self.starting_points: #para cada cidade da lista tenta um caminho...
                caminho = self.profundidade_limitada(i, cidade_final.upper(), 4, self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #se escolher Aprofundamento iterativo
        if metodo == self.methods[3]:
            for i in self.starting_points: #para cada cidade da lista tenta um caminho...
                caminho = self.aprofundamento_iterativo(i, cidade_final.upper(), self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #se escolher Bidirecional
        if metodo == self.methods[4]:
            for i in self.starting_points: #para cada cidade da lista tenta um caminho...
                caminho = self.bidirecional(i, cidade_final.upper(), self.nodes, self.graphs)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
    
    #Funcao para unir as rotas de ajuda humanitaria e atendimento
    def unifica_caminho(self, rota_AH, rota_At):
        """Metodo para unificar o caminho, unir as rotas de AH e Atendimento"""

        caminho_unico = []
        for i in rota_AH:
            caminho_unico.append(i)
        for g in range(1, len(rota_At)):
            caminho_unico.append(rota_At[g])
        
        return caminho_unico