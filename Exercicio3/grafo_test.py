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

    def test_busca_em_profundidade(self):

        # Grafo da paraiba
        self.assertEqual(self.g_p.busca_em_profundidade("J"), ['J', 'a1', 'C', 'a2', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertEqual(self.g_p.busca_em_profundidade("C"), ['C', 'a1', 'J', 'a2', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertEqual(self.g_p.busca_em_profundidade("Z"), ['Z', 'a9', 'T', 'a7', 'C', 'a1', 'J', 'a2', 'E', 'a4', 'P', 'a6', 'M'])
        self.assertEqual(self.g_p.busca_em_profundidade("M"), ['M', 'a6', 'C', 'a1', 'J', 'a2', 'E', 'a4', 'P', 'a7', 'T', 'a9', 'Z'])

        # Grafo exemplo 2
        self.assertEqual(self.g_2.busca_em_profundidade("A"), ['A', '1', 'B', '11', 'F', '10', 'H', '9', 'G', '4', 'K', '5', 'J', '7', 'I', '13', 'C', '14', 'D', '15', 'E'])
        self.assertEqual(self.g_2.busca_em_profundidade("K"), ['K', '4', 'G', '2', 'A', '1', 'B', '11', 'F', '10', 'H', '13', 'C', '14', 'D', '15', 'E', '3', 'J', '7', 'I'])
        self.assertEqual(self.g_2.busca_em_profundidade("B"), ['B', '1', 'A', '2', 'G', '4', 'K', '5', 'J', '7', 'I', '9', 'H', '10', 'F', '13', 'C', '14', 'D', '15', 'E'])

        # Grafo não conexo
        self.assertEqual(self.g_l3.busca_em_profundidade("A"), "Grafo não conexo!")

        # Grafo completo
        self.assertEqual(self.g_c.busca_em_profundidade("C"), ['C', 'a1', 'J', 'a3', 'E', 'a8', 'P'])

        # Grafo sem paralelas
        self.assertEqual(self.g_p_sem_paralelas.busca_em_profundidade("J"), ['J', 'a1', 'C', 'a3', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'])

        #Grafo com muitos retornos para os pais
        g_mp = Grafo(['A','B','C','D','E','F','G','H','I','J','K','L','M'], {"a1": 'A-B', "a2": "B-C", "a3": "B-J", 'a4': "C-B", "a5": "D-C", "a6": "D-E", "a7": "F-E", "a8": "E-A", "a9": "B-F", "a10": "G-F", "a11": "H-G", "a12": "I-H", "a13": "J-K", "a14": "L-K", "a15": "A-M"})
        self.assertEqual(g_mp.busca_em_profundidade("A"), ['A', 'a1', "B", 'a2', 'C', 'a5', 'D', 'a6', 'E', 'a7', 'F', 'a10', 'G', 'a11', 'H', 'a12', 'I', 'a3', 'J', 'a13', 'K', 'a14', 'L', 'a15', 'M'])


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
        g_mp = Grafo(['A','B','C','D','E','F','G','H','I','J','K','L','M'], {"a1": 'A-B', "a2": "B-C", "a3": "B-J", 'a4': "C-B", "a5": "D-C", "a6": "D-E", "a7": "F-E", "a8": "E-A", "a9": "B-F", "a10": "G-F", "a11": "H-G", "a12": "I-H", "a13": "J-K", "a14": "L-K", "a15": "A-M"})
        self.assertEqual(g_mp.busca_em_profundidade_recursiva("A"), ['A', 'a1', "B", 'a2', 'C', 'a5', 'D', 'a6', 'E', 'a7', 'F', 'a10', 'G', 'a11', 'H', 'a12', 'I', 'a3', 'J', 'a13', 'K', 'a14', 'L', 'a15', 'M'])
