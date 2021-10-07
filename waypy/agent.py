"""This module is responsible for calling each method as needed."""

from waypy.methods import busca

class Agente(busca):

    starting_points = []
    arrival_points = []
    nodes = []
    graphs = []

    #Initialize lists that are from default values
    def __init__(self):
                
        #Declare the name of the methods to be chosen to compare with the input
        self.methods = ["AMPLITUDE", "PROFUNDIDADE", "PROFUNDIDADE LIMITADA",
                   "APROFUNDAMENTO ITERATIVO", "BIDIRECIONAL"]

        #Declare the name of the methods to be called to execute
        self.methods_main = ["amplitude", "profundidade", "profundidade_limitada",
                        "aprofundamento_iterativo", "bidirecional"]
        
        #Starts the list that will receive the routes
        self.route_starting =  self.route_arrival = []


    def encontrar_atendimento(self, cidade_final, metodo, limite=False):
        """Method to find a way between the city that received the AH and the nearest hospital.
            Receives the city that had humanitarian aid and makes attempts to generate
            a route from this city to the closest one on the list 'arrival_points'."""

        tam_caminho = 100000

        #if Amplitude is chosen...

        if metodo == self.methods[0]:
            for i in self.arrival_points: #for each city on the list try a path...
                caminho = self.amplitude(cidade_final.upper(), i, self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #if Depth is chosen... 
        if metodo == self.methods[1]:
            for i in self.arrival_points: #for each city on the list try a path...
                caminho = self.profundidade(cidade_final.upper(), i, self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #if Limited Depth is chosen...
        if metodo == self.methods[2]:
            for i in self.arrival_points: #for each city on the list try a path...
                caminho = self.profundidade_limitada(cidade_final.upper(), i, 4, self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #if Iterative Deepening is chosen...
        if metodo == self.methods[3]:
            for i in self.arrival_points: #for each city on the list try a path...
                caminho = self.aprofundamento_iterativo(cidade_final.upper(), i, self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #if Bidirectional is chosen...
        if metodo == self.methods[4]:
            for i in self.arrival_points: #for each city on the list try a path...
                caminho = self.bidirecional(cidade_final.upper(), i, self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting

    def encontrar_ajuda_humanitaria(self, cidade_final, metodo, limite=False):
        """Method to find a way between two points.
           Receives the city that needs humanitarian aid and makes the attempts
           to generate a route starting from the cities in the 'starting_points' list using less Memory."""
        
        tam_caminho = 100000

        #if Amplitude is chosen...
        if metodo == self.methods[0]:
            for i in self.starting_points: #for each city on the list try a path...
                caminho = self.amplitude(i, cidade_final.upper(), self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #if Depth is chosen...
        if metodo == self.methods[1]:
            for i in self.starting_points: #for each city on the list try a path...
                caminho = self.profundidade(i, cidade_final.upper(), self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #if Limited Depth is chosen...
        if metodo == self.methods[2]:
            for i in self.starting_points: #for each city on the list try a path...
                caminho = self.profundidade_limitada(i, cidade_final.upper(), 4, self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #if Iterative Deepening is chosen...
        if metodo == self.methods[3]:
            for i in self.starting_points: #for each city on the list try a path...
                caminho = self.aprofundamento_iterativo(i, cidade_final.upper(), self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
        
        #if Bidirectional is chosen...
        if metodo == self.methods[4]:
            for i in self.starting_points: #for each city on the list try a path...
                caminho = self.bidirecional(i, cidade_final.upper(), self.nodes, self.graphs)
                #the shortest path will be the current
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.route_starting = caminho
            return self.route_starting
    
    #Function to unite humanitarian aid and care routes
    def unifica_caminho(self, rota_AH, rota_At):
        """Method to unify the path, unite the AH and Service routes"""

        caminho_unico = []
        for i in rota_AH:
            caminho_unico.append(i)
        for g in range(1, len(rota_At)):
            caminho_unico.append(rota_At[g])
        
        return caminho_unico