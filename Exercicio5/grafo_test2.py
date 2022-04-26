import unittest
from grafo import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})


        self.g_2 = Grafo(["A","B","C","D","E","F","G","H","I","J","K"],{"1": "A-B", "2": "A-G", "3": "A-J", "4": "G-K", "5": "J-K", "6": "G-J", "7": "I-J", "8": "G-I", "9": "G-H", "10": "F-H", "11": "B-F", "12": "B-G", "13": "B-C", "14": "C-D", "15": "D-E", "16": "B-D", "17": "B-E"})

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1': 'J-C', 'a3': 'C-E', 'a4': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'})

        # Grafos completos
        self.g_c = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'J-E', 'a4':'J-P', 'a6':'C-E', 'a7':'C-P', 'a8':'E-P'})
        self.g_c2 = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'E-J', 'a4':'J-P', 'a6':'E-C', 'a7':'C-P', 'a8':'P-E'})
        self.g_c3 = Grafo(['J'])

        # Grafos com laco
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
        self.g_l4 = Grafo(['D'], {'a2':'D-D'})
        self.g_l5 = Grafo(['C', 'D'], {'a2':'D-C', 'a3':'C-C'})
        self.g_l6 = Grafo(['A', 'B', 'C', 'D'], {'a1': 'B-A', 'a2': 'C-C', 'a3': 'D-D'})


        # Grafo com muitos pais
        self.g_mp = Grafo(['A','B','C','D','E','F','G','H','I','J','K','L','M'], {"a1": 'A-B', "a2": "B-C", "a3": "B-J", 'a4': "C-B", "a5": "D-C", "a6": "D-E", "a7": "F-E", "a8": "E-A", "a9": "B-F", "a10": "G-F", "a11": "H-G", "a12": "I-H", "a13": "J-K", "a14": "L-K", "a15": "A-M"})


        #Grafo test caminho(vertice A no meio do Grafo)P
        self.g_tc = Grafo(['A','B','C','D'], {'a1':'A-C','a2':'A-B','a3':'B-D'})

        self.g_roteiro7 = Grafo(
            ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10", "v11", "v12", "v13", "v14", "v15", "v16",
             "v17", "v18", "v19", "v20", "v21", "v22", "v23", "v24", "v25", "v26", "v27", "v28", "v29", "v30", "v31",
             "v32", "v33" ],{
            "a1":"v1-v2", "a2": "v1-v3", "a3": "v1-v4", "a4": "v2-v3", "a5": "v2-v8", "a6": "v3-v7", "a7": "v4-v5", "a8": "v4-v6", "a9": "v4-v12", "a10": "v5-v6", "a11": "v6-v7", "a12": "v6-v11", "a13": "v7-v8", "a14": "v7-v10", "a45": "v17-v18", "a15": "v8-v9", "a16": "v9-v16", "a17": "v10-v15", "a18": "v11-v12", "a19": "v11-v14", "a20": "v12-v13", "a21": "v13-v18", "a22": "v13-v20", "a23": "v14-v17", "a24": "v14-v18", "a25": "v14-v19", "a26": "v15-v18", "a27": "v16-v17", "a28": "v18-v19", "a29": "v18-v23", "a30": "v18-v24", "a31": "v19-v20", "a32": "v19-v22", "a33": "v20-v21", "a34": "v21-v28", "a35": "v21-v29", "a36": "v22-v27", "a37": "v22-v28", "a38": "v23-v26", "a39": "v24-v25", "a40": "v24-v26", "a41": "v26-v31", "a42": "v29-v30", "a43": "v30-v31", "a44": "v31-v32", "a46": "v31-v33" })

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J', 'T-E', 'T-P', 'T-T', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                     ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T',
                      'E-Z', 'P-J', 'P-E',
                      'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J', 'T-E', 'T-P', 'T-T',
                      'Z-J', 'Z-C', 'Z-E',
                      'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c2.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), ['J-J'])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 3)
        self.assertEqual(self.g_l2.grau('B'), 3)
        self.assertEqual(self.g_l4.grau('D'), 1)

    def test_arestas_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a6', 'a8']))

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertTrue((self.g_l4.eh_completo()))
        self.assertTrue((self.g_l5.eh_completo()))


    def test_busca_em_profundidade_recursiva(self):

        # Grafo da paraiba
        self.assertEqual(self.g_p.busca_em_profundidade_recursiva("J"), ['J', 'a1', 'C', 'a2', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertEqual(self.g_p.busca_em_profundidade_recursiva("C"), ['C', 'a1', 'J', 'a2', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertEqual(self.g_p.busca_em_profundidade_recursiva("Z"), ['Z', 'a9', 'T', 'a7', 'C', 'a1', 'J', 'a2', 'E', 'a4', 'P', 'a6', 'M'])
        self.assertEqual(self.g_p.busca_em_profundidade_recursiva("M"), ['M', 'a6', 'C', 'a1', 'J', 'a2', 'E', 'a4', 'P', 'a7', 'T', 'a9', 'Z'])

        # Grafo exemplo 2
        self.assertEqual(self.g_2.busca_em_profundidade_recursiva("A"), ['A', '1', 'B', '11', 'F', '10', 'H', '9', 'G', '4', 'K', '5', 'J', '7', 'I', '13', 'C', '14', 'D', '15', 'E'])
        self.assertEqual(self.g_2.busca_em_profundidade_recursiva("K"), ['K', '4', 'G', '2', 'A', '1', 'B', '11', 'F', '10', 'H', '13', 'C', '14', 'D', '15', 'E', '3', 'J', '7', 'I'])
        self.assertEqual(self.g_2.busca_em_profundidade_recursiva("B"), ['B', '1', 'A', '2', 'G', '4', 'K', '5', 'J', '7', 'I', '9', 'H', '10', 'F', '13', 'C', '14', 'D', '15', 'E'])

        # Grafo não conexo
        self.assertEqual(self.g_l3.busca_em_profundidade_recursiva("A"), "Grafo não conexo!")

        # Grafo completo
        self.assertEqual(self.g_c.busca_em_profundidade_recursiva("C"), ['C', 'a1', 'J', 'a3', 'E', 'a8', 'P'])

        # Grafo sem paralelas
        self.assertEqual(self.g_p_sem_paralelas.busca_em_profundidade_recursiva("J"), ['J', 'a1', 'C', 'a3', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'])

        #Grafo com muitos retornos para os pais
        self.assertEqual(self.g_mp.busca_em_profundidade_recursiva("A"), ['A', 'a1', "B", 'a2', 'C', 'a5', 'D', 'a6', 'E', 'a7', 'F', 'a10', 'G', 'a11', 'H', 'a12', 'I', 'a3', 'J', 'a13', 'K', 'a14', 'L', 'a15', 'M'])

    def test_ha_ciclo(self):
        self.assertEqual(self.g_p.ha_ciclo(), ['C','a3', 'E', 'a2', 'C'])

        self.assertEqual(self.g_2.ha_ciclo(), ['A', '2', 'G', '9', 'H', '10', 'F', '11', 'B', '1', 'A'])

        # sem paralelas
        self.assertEqual(self.g_p_sem_paralelas.ha_ciclo(), ['C', 'a7', 'T', 'a8', 'M', 'a6','C'])

        #grafos completos
        self.assertEqual(self.g_c.ha_ciclo(), ['J', 'a3', 'E', 'a6', 'C', 'a1', 'J'])
        self.assertEqual(self.g_c2.ha_ciclo(), ['J', 'a3', 'E', 'a6', 'C', 'a1', 'J'])

        # Grafo sem aresta com 1 vertice
        self.assertEqual(self.g_c3.ha_ciclo(), False)

        # Grafo desconexo com laco
        self.assertEqual(self.g_l1.ha_ciclo(), ['A', 'a1', 'A'])
        self.assertEqual(self.g_l2.ha_ciclo(), ['B', 'a2', 'B'])
        self.assertEqual(self.g_l3.ha_ciclo(),['C', 'a2', 'C'])
        self.assertEqual(self.g_l4.ha_ciclo(),['D', 'a2', 'D'])
        self.assertEqual(self.g_l5.ha_ciclo(),['C', 'a3', 'C'])
        self.assertEqual(self.g_l6.ha_ciclo(), ['C', 'a2', 'C'])

        # Grafo com muitos pais
        self.assertEqual(self.g_mp.ha_ciclo(), ['B', 'a4', 'C', 'a2', 'B'])

        #Grafo test caminho(vertice A no meio do Grafo
        self.assertEqual(self.g_tc.ha_ciclo(), False)

    def test_caminho_grafo_paraiba(self):
        #Grafo Da Paraiba
        self.assertEqual(self.g_p.caminho(-1), False)
        self.assertEqual(self.g_p.caminho(0), False)
        self.assertEqual(self.g_p.caminho(1), ['J', 'a1', 'C'])
        self.assertEqual(self.g_p.caminho(2), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertEqual(self.g_p.caminho(3), ['J', 'a1', 'C', 'a6', 'M', 'a8', 'T'])
        self.assertEqual(self.g_p.caminho(4), ['J', 'a1', 'C', 'a6', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertEqual(self.g_p.caminho(5), False)
        self.assertEqual(self.g_p.caminho(6), False)

    def test_caminho_grafo_2(self):


        self.assertEqual(self.g_2.caminho(-1), False)
        self.assertEqual(self.g_2.caminho(0), False)
        self.assertEqual(self.g_2.caminho(1), ['A', '1', 'B'])
        self.assertEqual(self.g_2.caminho(2), ['A', '1', 'B', '11', 'F'])
        self.assertEqual(self.g_2.caminho(3), ['A', '1', 'B', '11', 'F', '10','H'])
        self.assertEqual(self.g_2.caminho(4), ['A', '1', 'B', '11', 'F', '10','H', '9', 'G'])
        self.assertEqual(self.g_2.caminho(5), ['A', '1', 'B', '11', 'F', '10','H', '9', 'G', '4', 'K'])
        self.assertEqual(self.g_2.caminho(6), ['A', '1', 'B', '11', 'F', '10','H', '9', 'G', '4', 'K', '5', 'J'])
        self.assertEqual(self.g_2.caminho(7), ['A', '1', 'B', '11', 'F', '10','H', '9', 'G', '4', 'K', '5', 'J', '7', 'I'])
        self.assertEqual(self.g_2.caminho(8), ['A', '3', 'J', '5', 'K', '4', 'G', '9', 'H', '10', 'F', '11', 'B', '13', 'C', '14', 'D'])
        self.assertEqual(self.g_2.caminho(9), ['A', '3', 'J', '5', 'K', '4', 'G', '9', 'H', '10', 'F', '11', 'B', '13', 'C', '14', 'D', '15', 'E'])
        self.assertEqual(self.g_2.caminho(10), False)
        self.assertEqual(self.g_2.caminho(11), False)

    def test_caminho_grafo_laco_1(self):
        #Grafo com laços
        self.assertEqual(self.g_l1.caminho(-1),False)
        self.assertEqual(self.g_l1.caminho(0),False)
        self.assertEqual(self.g_l1.caminho(1),['A','a2','B'])
        self.assertEqual(self.g_l1.caminho(2),False)
        self.assertEqual(self.g_l1.caminho(6),False)


    def test_caminho_grafo_laco_2(self):
        #Grafo com laços
        self.assertEqual(self.g_l2.caminho(-1),False)
        self.assertEqual(self.g_l2.caminho(0),False)
        self.assertEqual(self.g_l2.caminho(1),['A','a1','B'])
        self.assertEqual(self.g_l2.caminho(2),False)
        self.assertEqual(self.g_l2.caminho(3),False)

    def test_caminho_grafo_laco_3(self):
        #Grafo com laços
        self.assertEqual(self.g_l3.caminho(-1),False)
        self.assertEqual(self.g_l3.caminho(0),False)
        self.assertEqual(self.g_l3.caminho(1),['A','a1','C'])
        self.assertEqual(self.g_l3.caminho(2),False)
        self.assertEqual(self.g_l3.caminho(99),False)


    def test_caminho_grafo_laco_4(self):
        #Grafo com laços
        self.assertEqual(self.g_l4.caminho(-1),False)
        self.assertEqual(self.g_l4.caminho(0),False)
        self.assertEqual(self.g_l4.caminho(1),False)
        self.assertEqual(self.g_l4.caminho(2),False)
        self.assertEqual(self.g_l4.caminho(9),False)

    def test_caminho_grafo_laco_5(self):
        #Grafo com laços
        self.assertEqual(self.g_l5.caminho(-1),False)
        self.assertEqual(self.g_l5.caminho(0),False)
        self.assertEqual(self.g_l5.caminho(1),['C', 'a2', 'D'])
        self.assertEqual(self.g_l5.caminho(2),False)
        self.assertEqual(self.g_l5.caminho(7),False)


    def test_caminho_grafo_laco_6(self):
        #Grafo com laços
        self.assertEqual(self.g_l6.caminho(-1),False)
        self.assertEqual(self.g_l6.caminho(0),False)
        self.assertEqual(self.g_l6.caminho(1),['A', 'a1', 'B'])
        self.assertEqual(self.g_l6.caminho(2),False)
        self.assertEqual(self.g_l6.caminho(9),False)


    def test_caminho_grafo_completo(self):
        #Grafos completos

        self.assertEqual(self.g_c.caminho(-1),False)
        self.assertEqual(self.g_c.caminho(0),False)
        self.assertEqual(self.g_c.caminho(1),['J', 'a1', 'C'])
        self.assertEqual(self.g_c.caminho(2),['J', 'a1', 'C', 'a6', 'E'])
        self.assertEqual(self.g_c.caminho(3),['J', 'a1', 'C', 'a6', 'E', 'a8', 'P'])
        self.assertEqual(self.g_c.caminho(4),False)
        self.assertEqual(self.g_c.caminho(5),False)

    def test_caminho_grafo_completo_2(self):
        #Grafos completos

        self.assertEqual(self.g_c2.caminho(-1),False)
        self.assertEqual(self.g_c2.caminho(0),False)
        self.assertEqual(self.g_c2.caminho(1),['J', 'a1', 'C'])
        self.assertEqual(self.g_c2.caminho(2),['J', 'a1', 'C', 'a6', 'E'])
        self.assertEqual(self.g_c2.caminho(3),['J', 'a1', 'C', 'a6', 'E', 'a8', 'P'])
        self.assertEqual(self.g_c2.caminho(4),False)
        self.assertEqual(self.g_c2.caminho(5),False)

    def test_caminho_grafo_com_A_meio(self):
        #Grafo Test caminho
        self.assertEqual(self.g_tc.caminho(-1),False)
        self.assertEqual(self.g_tc.caminho(0),False)
        self.assertEqual(self.g_tc.caminho(1),['A', 'a1', 'C'])
        self.assertEqual(self.g_tc.caminho(2),['A', 'a2', 'B', 'a3', 'D'])
        self.assertEqual(self.g_tc.caminho(3),['C', 'a1', 'A', 'a2', 'B', 'a3', 'D'])

    def test_caminho_grafo_muitos_pais(self):
        #Grafo Test caminho
        self.assertEqual(self.g_mp.caminho(-1),False)
        self.assertEqual(self.g_mp.caminho(0),False)
        self.assertEqual(self.g_mp.caminho(1),['A', 'a1', 'B'])
        self.assertEqual(self.g_mp.caminho(2),['A', 'a1', 'B', 'a2', 'C'])
        self.assertEqual(self.g_mp.caminho(3),  ['A', 'a1', 'B', 'a2', 'C', 'a5', 'D'])
        self.assertEqual(self.g_mp.caminho(4),  ['A', 'a1', 'B', 'a2', 'C', 'a5', 'D', 'a6', 'E'])
        self.assertEqual(self.g_mp.caminho(5),  ['A', 'a1', 'B', 'a2', 'C', 'a5', 'D', 'a6', 'E', 'a7', 'F'])
        self.assertEqual(self.g_mp.caminho(6),  ['A', 'a1', 'B', 'a2', 'C', 'a5', 'D','a6', 'E', 'a7', 'F', 'a10', 'G'])


    def test_conexo(self):

        self.assertEqual(self.g_p.conexo(), True)
        self.assertEqual(self.g_2.conexo(), True)


        #Grafo so com 1 vertice sem aresta
        self.assertEqual(self.g_c.conexo(), True)
        self.assertEqual(self.g_c2.conexo(), True)
        self.assertEqual(self.g_c3.conexo(), True)

        #grafo com 1 vertice e uma aresta
        self.assertEqual(self.g_l4.conexo(), True)
        self.assertEqual(self.g_l5.conexo(), True)

        #Grafos desconexos

        self.assertEqual(self.g_l1.conexo(), False)
        self.assertEqual(self.g_l2.conexo(), False)
        self.assertEqual(self.g_l3.conexo(), False)
        self.assertEqual(self.g_l6.conexo(), False)

        self.assertEqual(self.g_mp.conexo(),True)

        self.assertEqual(self.g_tc.conexo(),True)

    def test_dikjstra(self):
        self.assertEqual(self.g_roteiro7.dakjastra("v1", "v32"), ['v32', 'v31', 'v26', 'v23', 'v18', 'v13', 'v12', 'v4', 'v1'])
        self.assertEqual(self.g_roteiro7.dakjastra("v2", "v27"), ['v27', 'v22', 'v19', 'v14', 'v11', 'v6', 'v4', 'v1', 'v2'])
        self.assertEqual(self.g_roteiro7.dakjastra("v3", "v15"), ['v15', 'v10', 'v7', 'v3'])
        self.assertEqual(self.g_roteiro7.dakjastra("v5", "v33"), ['v33', 'v31', 'v26', 'v23', 'v18', 'v13', 'v12', 'v4', 'v5'])
        self.assertEqual(self.g_roteiro7.dakjastra("v4", "v28"), ['v28', 'v21', 'v20', 'v13', 'v12', 'v4'])

    def test_dikjstraDrone(self):
        self.assertEqual(self.g_roteiro7.dakjastraDrone("v1", "v32", 3, 3, ["v9", "v18", "v21", "v30"]),
                         ['v32', 'v31', 'v30', 'v29', 'v21', 'v20', 'v13', 'v18', 'v17', 'v16', 'v9', 'v8', 'v2', 'v1'])
        self.assertEqual(self.g_roteiro7.dakjastraDrone("v2", "v27", 4, 3, ["v9", "v18", "v21", "v30"]),
                         ['v27', 'v22', 'v19', 'v18', 'v17', 'v16', 'v9', 'v8', 'v2'])
        self.assertEqual(self.g_roteiro7.dakjastraDrone("v3", "v21", 3, 3, ["v9", "v18", "v21", "v30"]),
                         ['v21', 'v20', 'v13', 'v18', 'v17', 'v16', 'v9', 'v8', 'v2', 'v3'])
        self.assertEqual(self.g_roteiro7.dakjastraDrone("v4", "v17", 4, 3, ["v9", "v18", "v21", "v30"]), ['v17', 'v14', 'v11', 'v6', 'v4'])
        self.assertEqual(self.g_roteiro7.dakjastraDrone("v6", "v32", 3, 4, ["v9", "v18", "v21", "v30"]), ['v32', 'v31', 'v26', 'v23', 'v18', 'v14', 'v11', 'v6'])
        self.assertEqual(self.g_roteiro7.dakjastraDrone("v6", "v32", 4, 3, ["v9", "v18", "v21", "v30"]),
                         ['v33','v31','v30','v29', 'v21', 'v20', 'v19', 'v18', 'v14', 'v11', 'v6'])
