from grafo import Grafo

g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],{'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T','a8': 'M-T', 'a9': 'T-Z'})

g_2 = Grafo(["A","B","C","D","E","F","G","H","I","J","K"],{"1": "A-B", "2": "A-G", "3": "A-J", "4": "G-K", "5": "J-K", "6": "G-J", "7": "I-J", "8": "G-I", "9": "G-H", "10": "F-H", "11": "B-F", "12": "B-G", "13": "B-C", "14": "C-D", "15": "D-E", "16": "B-D", "17": "B-E"})

#

g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
print(g_l3.busca_em_profundidade("A"))
