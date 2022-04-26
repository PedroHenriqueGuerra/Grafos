
# Dupla : Pedro Henrique e Lucas Dantas

class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not (self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def vertices_nao_adjacentes(self):
        naoAdjacentes = []  # lista de nao adjacentes
        arestas = self.A.copy()  # copia das arestas
        vertices = self.N.copy()  # copia dos verticesd
        for i in range(0, len(vertices)):  # Percorre veritices
            for j in range(0, len(vertices)):  # Verifica os vertices que nao foram analisados

                ehAdjacente = False

                for aresta in arestas:  # Percorre as arestas
                    v1, v2 = arestas[aresta].split('-')
                    # Verificand se a aresta incide sobre os vertices
                    if (vertices[i] == v1 and vertices[j] == v2):
                        ehAdjacente = True
                        break

                    elif (vertices[j] == v1 and vertices[i] == v2):
                        ehAdjacente = True
                        break

                # Verifica se foi encontrad
                if (ehAdjacente == False):
                    naoAdjacentes.append(vertices[i] + "-" + vertices[j])  # Adiciona os vertices nao encontrados

        return naoAdjacentes

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not (i == len(self.A) - 1):  # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str

    def ha_paralelas(self):

        arestas = self.A.copy()

        for aresta1 in arestas:

            v1, v2 = arestas[aresta1].split("-")
            for aresta2 in arestas:
                if (aresta1 == aresta2):
                    continue

                v3, v4 = arestas[aresta2].split("-")
                if ((v1 == v3 and v2 == v4) or (v1 == v4 and v2 == v3)):
                    return True

        return False

    def ha_laco(self):
        for i in self.A:
            v1, v2 = self.A[i].split('-')
            if (v1 == v2):
                return True
        return False

    def grau(self, v):
        cont = 0
        for i in list(self.A.values()):
            if v in list(i):
                cont += 1
        return cont

    def arestas_sobre_vertice(self, v):
        asv = []
        for i, j in self.A.items():
            v1, v2 = j.split("-")

            if (v == v1) or (v == v2):
                asv.append(i)
        return asv

    def eh_completo(self):
        combinacoes = []
        combinacoes2 = []
        for i in range(len(self.N)):
            for j in range(i + 1, len(self.N)):
                combinacoes.append(self.N[i] + '-' + self.N[j])
                combinacoes2.append(self.N[j] + '-' + self.N[i])

        for i in range(len(combinacoes)):
            if combinacoes[i] not in list(self.A.values()) and combinacoes2[i] not in list(self.A.values()):
                return False
        return True

    def busca_em_profundidade_recursiva(self,r, vertices_percorridos = None, arestas_analisadas = None):

        # Verificando se primeira chamada e setando as listas vazias(Correção do problema do acumulo)
        if arestas_analisadas is None:
            arestas_analisadas = []
            vertices_percorridos = []

        arvore_dfs = list() # Arvore DFS = []
        arvore_dfs.append(r) # Adionando raiz
        vertices_percorridos.append(r) # Adicionando vertice a lista de vertices percorridos
        for aresta in self.arestas_sobre_vertice(r): # Percorrendo todas as arestas
            if(aresta in arestas_analisadas): # Verificando se aresta ja foi analisada
              continue
            else:
                v1, v2 = self.A[aresta].split("-") #Atribuindo vertice 1 a v1 2 vertice2 a v2)

                if(v1 == r): # Se v1 é a raiz
                    if(v2 in vertices_percorridos): # Se v2 ja foi percorrido continua para a proxima iteração
                        continue
                    else:
                        arvore_dfs.append(aresta) # Adicionando aresta a arvore dfs
                        arestas_analisadas.append(aresta) # Adicionanco aresta a lista de arestas analidas
                        arvore_dfs += self.busca_em_profundidade_recursiva(v2,vertices_percorridos,arestas_analisadas) # Chamada recursiva e adicionado resultado a arvore dfz

                #Mesma coisa do vertice acima, mas para ovetice 2
                else:
                    if(v1 in vertices_percorridos):
                        continue
                    else:
                        arvore_dfs.append(aresta)
                        arestas_analisadas.append(aresta)
                        arvore_dfs += self.busca_em_profundidade_recursiva(v1,vertices_percorridos,arestas_analisadas)

        #Verifica se já terminou todas(está novamente na primeira chamada, o vertice atual e o orimeiro a ser percorridos) e caso tenha vertice não percorrido
        if(vertices_percorridos[0] == arvore_dfs[0] and len(vertices_percorridos) < len(self.N)):
          return "Grafo não conexo!" # Retorne Grafo nao conexo

        return arvore_dfs # Retorna arvore gerada


    def ha_ciclo(self):

        for v in self.N: # verificando apartir de  todos os vertices( casos dos grafos deconexos
            retorno = self.ha_ciclo_aux(v,[],[]) # recebe o resultado da funcao quando chamada
            if(retorno == False): # se false pular para proxima iteração
                continue
            else:
                return retorno # retorne o resiltad
        return False

    def ha_ciclo_aux(self, vertice = None, vertices_percorridos = None, arestas_percorridas =  None):

        if vertice is None:
            vertices_percorridos = []
            arestas_percorridas = []
            vertice = self.N[0]

        vertices_percorridos.append(vertice)

        for aresta in self.arestas_sobre_vertice(vertice):
            ciclo = []
            if aresta not in arestas_percorridas:

                v1, v2 = self.A[aresta].split('-')
                arestas_percorridas.append(aresta)
                # vertice 1 é o vertice de partida
                if(v1 == vertice):
                    # Encontrou um ciclo
                    if(v2 in vertices_percorridos):
                        vertices_percorridos.append(v2)
                        ciclo.append(v2) # Adiciona o ultimo vertice do ciclo = ao primeiro
                        ciclo.append(aresta) # adiciona aresta
                        ciclo.append(vertice) # adiciona o verice atual
                        return ciclo

                    # Não encontrou um ciclo
                    else:
                        ciclo.append(aresta)
                        ciclo.append(vertice)
                        resposta = self.ha_ciclo_aux(v2, vertices_percorridos, arestas_percorridas)
                        if(resposta != False):
                            if(resposta[0] != resposta[-1]):
                                resposta += ciclo
                            return resposta

                # vertice 2 é o vertice de partida
                if (v2 == vertice):
                    # Encontrou um ciclo
                    if (v1 in vertices_percorridos):

                        vertices_percorridos.append(v1)
                        ciclo.append(v1)  # Adiciona o ultimo vertice do ciclo = ao primeiro
                        ciclo.append(aresta)  # adiciona aresta
                        ciclo.append(vertice)  # adiciona o verice atual
                        return ciclo

                    # Não encontrou um ciclo
                    else:
                        ciclo.append(aresta)
                        ciclo.append(vertice)
                        resposta = self.ha_ciclo_aux(v1, vertices_percorridos, arestas_percorridas)
                        if (resposta != False):
                            if (resposta[0] != resposta[-1]):
                                resposta += ciclo
                            return resposta


        return False

    def caminho(self,n):
        if(n == 0): return False
        if(n >= len(self.N) or n > len(self.A)):
            return False
        for v in self.N:
            retorno = self.caminho_aux(n,v,[],[])
            if(retorno == False):
                continue
            else:
                return retorno
        return False

    def caminho_aux(self,n, vertice=None, vertices_percorridos=None, arestas_percorridas=None):
        if vertice is None:
            vertices_percorridos = []
            arestas_percorridas = []
            vertice = self.N[0]
        if(n == 0):
            return vertice

        # Adiciona o vertice aos vertices percorridos
        vertices_percorridos.append(vertice)

        # Caminho encontrado
        caminho = []

        for aresta in self.arestas_sobre_vertice(vertice):
            vertices_percorridos_copia = vertices_percorridos.copy()
            arestas_percorridas_copia = arestas_percorridas.copy()
            if aresta not in arestas_percorridas:
                caminho = [vertice]
                arestas_percorridas.append(aresta)
                v1, v2 = self.A[aresta].split('-')
                if(v1 == vertice):
                    if v2 not in vertices_percorridos:
                        caminho.append(aresta)
                        resposta = self.caminho_aux(n-1, v2, vertices_percorridos_copia, arestas_percorridas_copia)
                        if(resposta == False):
                            continue
                        else:
                            caminho += resposta
                            return caminho

                elif (v2 == vertice):
                    if v1 not in vertices_percorridos:
                        caminho.append(aresta)

                        resposta = self.caminho_aux(n - 1, v1, vertices_percorridos_copia, arestas_percorridas_copia)
                        if (resposta == False):
                            continue
                        else:
                            caminho += resposta
                            return caminho
        return False

    def conexo(self,r = None, vertices_percorridos = None, arestas_analisadas = None):

      if r is None:
          r = self.N[0]
          arestas_analisadas = []
          vertices_percorridos = []

      arvore_dfs = list()
      arvore_dfs.append(r)
      vertices_percorridos.append(r)
      for aresta in self.arestas_sobre_vertice(r):
        if(aresta in arestas_analisadas):
          continue
        else:
          v1, v2 = self.A[aresta].split("-")
          if(v1 == r):
            if(v2 in vertices_percorridos):
              continue
            else:
              arvore_dfs.append(aresta)
              arestas_analisadas.append(aresta)
              arvore_dfs += self.busca_em_profundidade_recursiva(v2,vertices_percorridos,arestas_analisadas)
          else:
            if(v1 in vertices_percorridos):
              continue
            else:
              arvore_dfs.append(aresta)
              arestas_analisadas.append(aresta)
              arvore_dfs += self.busca_em_profundidade_recursiva(v1,vertices_percorridos,arestas_analisadas)

      if(vertices_percorridos[0] == arvore_dfs[0] and len(vertices_percorridos) < len(self.N)):
          return False
      elif(vertices_percorridos[0] == arvore_dfs[0] and len(vertices_percorridos) == len(self.N)):
          return True

      return arvore_dfs


    '''
    @:param u = Vertice incial, v = vertice final, w = vertice atual, beta = lista dos betas,
     fi = lista que representa se é temporario ou permanetnte,
      pi = lista de precededores, arestas_percooridas = lista das arestas percorridas
    '''
    def dakjastra(self, u, v, w = "", betaParametro = {}, fiParametro = [], piParametro = {}, arestas_percorridasParametro = []):

        fi = fiParametro.copy()
        beta = betaParametro.copy()
        pi = piParametro.copy()
        arestas_percorridas = arestas_percorridasParametro.copy()

        if (beta == {}): # Iniciando variaveis, beta, fi e e pi
            for vertice in self.N:
                if vertice == u:
                    beta[vertice] = 0
                else:
                    beta[vertice] = 9999

                fi.append(vertice)
                pi[vertice] = ''
            w = u # O primeiro w é vertice inicial

        if (w == v):
            # fim da busca, menor caminho encontrado
            menor_caminho = [w]

            while(w != u):
                menor_caminho.append(pi[w])
                w = pi[w]

            beta = {}
            fi = []
            pi = {}
            return menor_caminho



        arestas_u = self.arestas_sobre_vertice(w)
        for aresta in arestas_u:
            if(aresta in arestas_percorridas):
                continue

            v1, outroVertice = self.A[aresta].split("-")


            if (outroVertice == w):
                outroVertice = v1

            arestas_percorridas.append(aresta)
            if (beta[outroVertice] > beta[w] + 1):
                beta[outroVertice] = beta[w] + 1
                pi[outroVertice] = w

        menor_beta = 999
        vertice_menor = ''
        for vertice in fi:
            if(beta[vertice] < menor_beta):
                menor_beta = beta[vertice]
                vertice_menor = vertice

        if(vertice_menor == ''):
            return []
        fi.remove(vertice_menor)

        return self.dakjastra(u,v,vertice_menor, beta, fi, pi, arestas_percorridas)

    '''
       @:param u = Vertice incial, v = vertice final, w = vertice atual, beta = lista dos betas,
        fi = lista que representa se é temporario ou permanetnte,
         pi = lista de precededores, arestas_percooridas = lista das arestas percorridas
       '''

    def dakjastraDrone(self, u, v, carga_inicial, carga_maxima, pontos_recarga, w="", carga_atual = 0, betaParametro={}, fiParametro=[], piParametro={}, gamaParametro={}, arestas_percorridasParametro=[]):

        fi = fiParametro.copy()
        beta = betaParametro.copy()
        pi = piParametro.copy()
        gama = gamaParametro.copy()
        arestas_percorridas = arestas_percorridasParametro.copy()


        print("W", w)
        print("Pi", pi)
        print("Beta", beta)
        print("fi", fi)
        print("areata", arestas_percorridas, len(arestas_percorridas))

        if (beta == {}):  # Iniciando variaveis, beta, fi e e pi
            for vertice in self.N:
                if vertice == u:
                    beta[vertice] = 0
                else:
                    beta[vertice] = 9999

                fi.append(vertice)
                pi[vertice] = ''
                gama[vertice] = 0
            w = u  # O primeiro w é vertice inicial
            carga_atual = carga_inicial

        if (w == v):
            # fim da busca, menor caminho encontrado
            menor_caminho = [w]

            while (w != u):
                menor_caminho.append(pi[w])
                w = pi[w]

            beta = {}
            fi = []
            pi = {}
            gama = {}

            return menor_caminho



        arestas_u = self.arestas_sobre_vertice(w)
        for aresta in arestas_u:
            if (aresta in arestas_percorridas):
                continue

            v1, outroVertice = self.A[aresta].split("-")

            if (outroVertice == w):
                outroVertice = v1

            arestas_percorridas.append(aresta) # Analisando as arestas
            if (beta[outroVertice] > beta[w] + 1): # VErificacao do menor caminho
                beta[outroVertice] = beta[w] + 1
                pi[outroVertice] = w
                if (outroVertice in pontos_recarga):  # Ponto de recarga
                    gama[outroVertice] = carga_maxima
                elif(carga_atual - 1 == 0 and outroVertice != v): # Não vale apena ir para um vertice, com carga zero, que não é o final
                    gama[outroVertice] = carga_atual - 1
                    beta[outroVertice] = 9999 # Pela razão dita acima aumentamos o beta para um valor muito alto
                else:
                    gama[outroVertice] = carga_atual - 1

        vertice_menor = '' # Vertice de menor beta
        while (vertice_menor == ''): # loop para garantir que será buscada todas as opcoes

            menor_beta = 999 # menor beta inicia um valor muito alto
            for vertice in fi: # vendo menor beta na lista fi (vertices com fi temporario)
                if (beta[vertice] < menor_beta):
                    if(vertice != v):
                        if (gama[vertice] > 0):
                            menor_beta = beta[vertice]
                            vertice_menor = vertice
                    else:
                        menor_beta = beta[vertice]
                        vertice_menor = vertice

            if(vertice_menor == ''): # Se nehum vertice atende aos requisitos, não da para prosseguir. Caminho errado ou inexistente
                beta[w] = 9999 # beta do vertice atual volta para um valor alto, afim de ser desconsiderado nesse caminho
                gama[w] = 0 #gama  retorna para valor incial = 0

                return []

            else: # Vertice de menor beta encontrado
                fi_aux = [] # criando lista auxiliar de fi, para guardar os dados em caso de não achar caminho

                for n in fi: # Copiando lista
                    if(n != vertice_menor):
                        fi_aux.append(n)

                resposta = self.dakjastraDrone(u, v, carga_inicial,carga_maxima, pontos_recarga, vertice_menor, gama[vertice_menor],
                                               beta, fi_aux, pi, gama, arestas_percorridas) # Repete-se o  algoritmo

                if(resposta != []): # Se nao for encontrado o caminho então ele é retornado
                    return resposta
                vertice_menor = '' # EM caso de não enontrar nada o valor volta o menor vertice volta ser '' e é buscado mais uma vez o vertice de menor beta



