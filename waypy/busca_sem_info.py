class No(object):
    def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.valor1    = valor1
        self.valor2    = valor2
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, p):
        novo_no = No(p, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, p):

        novo_no = No(p, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.valor1)
            temp.append(aux.valor2)
            str.append(temp)
            aux = aux.proximo
        
        return str
    
    def exibeCaminho(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        caminho = caminho[::-1]
        return caminho
    
    def exibeCaminho1(self,valor):
                
        atual = self.head
        while atual.valor1 != valor:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho

class busca(object):

    def amplitude(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            if atual is None: break

            ind = nos.index(atual.valor1)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"


    def profundidade(self, inicio, fim):
        
        caminho = []

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)


        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            if atual is None: break

            ind = nos.index(atual.valor1)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])-1,-1,-1):

                novo = grafo[ind][i]
                #print("\tFilho de atual: ",novo)
                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                    
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        #print("Árvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"


    def profundidade_limitada(self, inicio, fim, limite):
        
        caminho = []

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)


        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            if atual is None: break

            if atual.valor2 < limite:
                ind = nos.index(atual.valor1)
    
                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind])-1,-1,-1):
    
                    novo = grafo[ind][i]
                    #print("\tFilho de atual: ",novo)
                    flag = True  # pressuponho que não foi visitado
    
                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.valor2+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.valor2+1
                            break
                        
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.valor2 + 1, atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor2+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho += l2.exibeCaminho()
                            #print("Árvore de busca:\n",l2.exibeLista())
                            return caminho

        return "caminho não encontrado"


    def aprofundamento_iterativo(self, inicio, fim):
        
        for limite in range(len(nos)):
            caminho = []
    
            # manipular a FILA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
    
            while l1.vazio() is not None:
                # remove o primeiro da fila
                atual = l1.deletaUltimo()
                if atual is None: break
    
                if (atual.valor2) < limite:
                    ind = nos.index(atual.valor1)
        
                    # varre todos as conexões dentro do grafo a partir de atual
                    for i in range(len(grafo[ind])-1,-1,-1):
        
                        novo = grafo[ind][i]
                        #print("\tFilho de atual: ",novo)
                        flag = True  # pressuponho que não foi visitado
        
                        # para cada conexão verifica se já foi visitado
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.valor2+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.valor2+1
                                break
                            
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.valor2 + 1, atual)
                            l2.insereUltimo(novo, atual.valor2 + 1, atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.valor2+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho += l2.exibeCaminho()
                                #print("Árvore de busca:\n",l2.exibeLista())
                                return caminho

        return "caminho não encontrado"

    def bidirecional(self, inicio, fim):

        # listas para a busca a partir da origem - busca 1
        l1 = lista()      # busca na FILA
        l2 = lista()      # cópia da árvore completa

        # listas para a busca a partir da destino -  busca 2
        l3 = lista()      # busca na FILA
        l4 = lista()      # cópia da árvore completa

        # cria estrutura para controle de nós visitados
        visitado = []

        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        linha = []
        linha.append(inicio)
        linha.append(1)
        visitado.append(linha)
        
        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)
        linha = []
        linha.append(fim)
        linha.append(2)
        visitado.append(linha)
        
        while True:
            
            # EXECUÇÃO DO PRIMEIRO AMPLITUDE - BUSCA 1
            flag1 = True
            while flag1:
                atual = l1.deletaPrimeiro()
                ind = nos.index(atual.valor1)
                for i in range(len(grafo[ind])):
                    novo = grafo[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 1:    # visitado na mesma árvore
                                flag2 = False
                            else:                      # visitado na outra árvore
                                flag3 = True
                            break
                    # for j
                        
                    if flag2:
                        l1.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
                        
                        if flag3:
                            caminho = []
                            caminho = l2.exibeCaminho()
                            #caminho = caminho[::-1]
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(1)
                            visitado.append(linha)
                        # if flag3
                    # if flag2
                # for i
                
                
                if(l1.vazio()!=True):
                    aux = l1.primeiro()
                    if aux.valor2 == atual.valor2:
                        flag1 = True
                    else:
                        flag1 = False                

            # EXECUÇÃO DO SEGUNDO AMPLITUDE - BUSCA 2
            flag1 = True
            while flag1:
                atual = l3.deletaPrimeiro()
                if atual==None:
                    break
                ind = nos.index(atual.valor1)
                for i in range(len(grafo[ind])):
                    novo = grafo[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 2:
                                flag2 = False
                            else:
                                flag3 = True
                            break
                        
                    if flag2:
                        l3.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l4.insereUltimo(novo, atual.valor2 + 1, atual)
                        
                        if flag3:
                            caminho = []
                            caminho = l4.exibeArvore()
                            caminho = caminho[::-1]
                            caminho += l2.exibeArvore1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(2)
                            visitado.append(linha)
                        
                if(l3.vazio() != True):
                    aux = l3.primeiro()
                    if(atual.valor2 == aux.valor2):
                        flag1 = True
                    else:
                        flag1 = False


"""
********************************************************************
        PROBLEMA 1: MAPA DA ROMÊNIA
********************************************************************
"""

nos = ["ARAD", "BUCARESTE", "CRAIOVA", "DOBRETA",
       "EFORIE", "FAGARAS", "GIORGIU", "HIRSOVA",
       "IASI", "LUGOJ", "MEHADIA", "NEAMT", "ORADEA",
       "PITESTI", "RIMNICU VILCEA", "SIBIU", "TIMISOARA",
       "URZICENI", "VASLUI", "ZERIND"]

# ORDEM DECRESCENTE

grafo = [
            ["ZERIND", "TIMISOARA", "SIBIU"],                 #0
            ["URZICENI", "PITESTI", "GIORGIU", "FAGARAS"],
            ["RIMNICU VILCEA", "PITESTI", "DOBRETA"],
            ["MEHADIA", "CRAIOVA"],
            ["HIRSOVA"],
            ["SIBIU", "BUCARESTE"],
            ["BUCARESTE"],
            ["URZICENI", "EFORIE"],
            ["VASLUI", "NEAMT"],
            ["TIMISOARA", "MEHADIA"],
            ["LUGOJ", "DOBRETA"],
            ["IASI"],
            ["ZERIND", "SIBIU"],
            ["RIMNICU VILCEA", "CRAIOVA", "BUCARESTE"],
            ["SIBIU", "PITESTI", "CRAIOVA"],
            ["RIMNICU VILCEA", "ORADEA", "FAGARAS", "ARAD"],
            ["LUGOJ", "ARAD"],
            ["VASLUI", "HIRSOVA", "BUCARESTE"],
            ["URZICENI", "IASI"],
            ["ORADEA", "ARAD"]
       ]

"""
# ORDEM CRESCENTE

nos = ["ARAD", "BUCARESTE", "CRAIOVA", "DOBRETA",
       "EFORIE", "FAGARAS", "GIORGIU", "HIRSOVA",
       "IASI", "LUGOJ", "MEHADIA", "NEAMT", "ORADEA",
       "PITESTI", "RIMNICU VILCEA", "SIBIU", "TIMISOARA",
       "URZICENI", "VASLUI", "ZERIND"]
# ORDEM CRESCENTE

grafo = [
            ["SIBIU", "TIMISOARA", "ZERIND"], 
            ["FAGARAS", "GIORGIU", "PITESTI", "URZICENI"], 
            ["DOBRETA", "PITESTI", "RIMNICU VILCEA"],
            ["CRAIOVA", "MEHADIA"], 
            ["HIRSOVA"],
            ["BUCARESTE", "SIBIU"],
            ["BUCARESTE"], 
            ["EFORIE", "URZICENI"], 
            ["NEAMT", "VASLUI"],
            ["MEHADIA", "TIMISOARA"], 
            ["DOBRETA", "LUGOJ"], 
            ["IASI"], 
            ["SIBIU", "ZERIND"],
            ["BUCARESTE", "CRAIOVA", "RIMNICU VILCEA"],
            ["CRAIOVA", "PITESTI", "SIBIU"], 
            ["ARAD", "FAGARAS", "ORADEA", "RIMNICU VILCEA"],
            ["ARAD", "LUGOJ"],
            ["BUCARESTE", "HIRSOVA", "VASLUI"], 
            ["IASI", "URZICENI"], 
            ["ARAD", "ORADEA"]        
        ]
"""

""" 
********************************************************************
        PROBLEMA 2: GRAFO GENÉRICO
********************************************************************
"""

"""
nos = ["A","1","2","3","4","5","6","7","8","9"]

# ORDEM DECRESCENTE
grafo = [
            ["3","2","1"],               
            ["A","4"],
            ["A","6","4","3"],
            ["A","6","5","2"],
            ["8","6","2","1"],
            ["9","6","3"],
            ["9","8","7","4","3","2"],
            ["B","9","6"],
            ["B","6","4"],
            ["B","7","6","5"]
       ]

"""



sol = busca()
caminho = []


# PROBLEMA A
origem  = "ARAD"
destino = "BUCARESTE"

caminho = sol.amplitude(origem,destino)
print("\nAmplitude.............: ",caminho)


caminho = sol.profundidade(origem,destino)
print("\nProfundidade..........: ",caminho)


caminho = sol.profundidade_limitada(origem,destino,2)
print("\nProfun. Limitada (2)..: ",caminho)

caminho = sol.profundidade_limitada(origem,destino,3)
print("\nProfun. Limitada (3)..: ",caminho)

caminho = sol.profundidade_limitada(origem,destino,4)
print("\nProfun. Limitada (4)..: ",caminho)


caminho = sol.aprofundamento_iterativo(origem,destino)
print("\nAprofun. Iterativo...:",caminho)


caminho = sol.bidirecional(origem,destino)
print("\nBidirecional.........: ",caminho)