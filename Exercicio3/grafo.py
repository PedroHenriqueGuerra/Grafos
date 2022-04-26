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
            if v in j:
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

      if arestas_analisadas is None:
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
          return "Grafo não conexo!"
      return arvore_dfs

    def busca_em_profundidade(self, r):

        arvore_dfs = []

        # Copia das arestas
        arestas_do_grafo = list(self.A.keys())

        # arestas_de_retorno
        arestas_de_retorno = []

        # Vertices Percorridos
        vertices_percorridos = {}
        # Vertice Raiz
        vertices_percorridos[r] = {"arestas_percorridas": [], "pai": None}

        # No observado
        vertice_observado = r
        arvore_dfs.append(r)

        contador = len(arestas_do_grafo)
        #Percoorendo arestas
        while(contador > 0):
            if(vertice_observado == None):
                return "Grafo não conexo!"
            arestas_do_vertice_observado = self.arestas_sobre_vertice(vertice_observado)

            aresta_analisada = None

            for aresta in arestas_do_vertice_observado:
                if(aresta in vertices_percorridos[vertice_observado]["arestas_percorridas"] or aresta in arestas_de_retorno):
                    continue
                else:
                    aresta_analisada = aresta
                    contador -= 1
                    break


            if(aresta_analisada != None):

                v1,v2 = self.A[aresta].split('-')

                if(v1 == vertice_observado):
                    if(v2 in vertices_percorridos.keys()):
                        arestas_de_retorno.append(aresta)
                    else:
                        vertices_percorridos[vertice_observado]["arestas_percorridas"].append(aresta)
                        vertices_percorridos[v2] = {"arestas_percorridas": [aresta], "pai": vertice_observado}

                        # Novo vertice a ser analisado
                        vertice_observado = v2

                        #Adicionar na arvore
                        arvore_dfs.append(aresta)
                        arvore_dfs.append(v2)

                elif(v2 == vertice_observado):
                    if (v1 in vertices_percorridos.keys()):
                        arestas_de_retorno.append(aresta)
                    else:
                        vertices_percorridos[vertice_observado]["arestas_percorridas"].append(aresta)
                        vertices_percorridos[v1] = {"arestas_percorridas": [aresta], "pai": vertice_observado}

                        # Novo vertice a ser analisado
                        vertice_observado = v1


                        #Adicionar na arvore
                        arvore_dfs.append(aresta)
                        arvore_dfs.append(v1)

            else:
                vertice_observado = vertices_percorridos[vertice_observado]["pai"]

        return arvore_dfs
