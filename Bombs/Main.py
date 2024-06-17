# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:42:19 2024

@author: balbi
"""

'''
Os vértices representam produtos químicos
necessários em algum processo de produção.

Existe uma aresta ligando cada par de produtos
que podem explodir, se combinados.

O número cromático representa o número
mínimo de compartimentos para guardar estes
produtos químicos em segurança.
'''

import networkx as nx
import matplotlib.pyplot as plt


incompatibilidade_quimica = {
    "Ácido acético": ["Ácido nítrico", "Peróxidos", "Hipoclorito de sódio"],
    "Ácido nítrico": ["Ácido acético", "Ácido clorídrico", "Metanol"],
    "Amônia": ["Cloro", "Bromo", "Ácido fluorídrico", "Iodo"],
    "Cloro": ["Amônia", "Acetileno", "Éter", "Hidrogênio"],
    "Hidróxido de sódio": ["Ácidos", "Água", "Alumínio em pó"],
    "Peróxidos orgânicos": ["Ácidos", "Materiais combustíveis", "Cobre"],
    "Hipoclorito de sódio": ["Ácido acético", "Amônia", "Acetona"],
    "Metanol": ["Ácido nítrico", "Bleach", "Peróxido de hidrogênio"],
    "Iodo": ["Amônia", "Acetona", "Hidrazina"],
    "Acetileno": ["Cloro", "Fluor", "Cobre", "Prata"],
    "Bromo": ["Amônia", "Acetona", "Hidrogênio"],
}
quimicos_armazenados_alto = [
    "Acetona",
    "Ácido acético",
    "Ácido clorídrico",
    "Ácido fluorídrico",
    "Amônia",
    "Cloro",
    "Hidróxido de sódio",
    "Peróxidos orgânicos",
    "Hipoclorito de sódio",
    "Metanol",
    "Iodo",
    "Ácido nítrico", 
    "Peróxidos", 
    "Éter", 
    "Hidrogênio", 
    "Ácidos", 
    "Água", 
    "Alumínio em pó", 
    "Materiais combustíveis", 
    "Bleach", 
    "Peróxido de hidrogênio", 
    "Hidrazina"
]
quimicos_nao_armazenados_alto = [
    "Acetileno",  # Armazenar em local fresco e ventilado, longe de oxidantes
    "Bromo",      # Armazenar em local fresco, fora da luz direta do sol
    "Cobre",      # Armazenar em local seco
    "Prata"       # Armazenar longe da luz e fontes de contaminação
    "Cilindros de gás",
    "Tanques de armazenamento de ácido",
    "Barril de solventes",
    "Centrífugas de laboratório",
    "Espectrômetros de massa",
    "Autoclaves",
    "Reatores de vidro grandes",
    "Sistemas de purificação de água",
    "Estufas de secagem"
]
class Estante:
    
    def __init__(self):
        self.G = nx.Graph()
        self.pode_colocar_no_alto = set()
        self.nao_pode_colocar_no_alto = set()

    def adicionarMaterial(self, material, pode_colocar_no_alto):
        self.G.add_node(material)
        if pode_colocar_no_alto:
            self.pode_colocar_no_alto.add(material)
        else:
            self.nao_pode_colocar_no_alto.add(material)

    def conectar(self, materialA, materialB):
        if materialA in self.G.nodes() and materialB in self.G.nodes():
            self.G.add_edge(materialA, materialB)
        else:
            print("Algum dos materiais fornecidos nao existe")

    def mostrarGrafo(self):
        nx.draw(self.G, with_labels=True)
        plt.show()
def coloracao(G):
    colors = {}
    for node in sorted(G.nodes(), key=lambda x: len(G[x]), reverse=True):
        neighbor_colors = {colors[neighbor] for neighbor in G[node] if neighbor in colors}
        for color in range(len(G)):
            if color not in neighbor_colors:
                break
        colors[node] = color
    return colors
# Instanciando a classe Estante
estante = Estante()

# Adicionando materiais à estante e definindo se podem ser colocados no alto
for material in quimicos_armazenados_alto:
    estante.adicionarMaterial(material, True)

for material in quimicos_nao_armazenados_alto:
    estante.adicionarMaterial(material, False)

# Conectando materiais incompatíveis
for material, incompativeis in incompatibilidade_quimica.items():
    for incompativel in incompativeis:
        estante.conectar(material, incompativel)
# Colorindo o grafo
colors = coloracao(estante.G)
nx.draw(estante.G, node_color=[colors[node] for node in estante.G.nodes()], with_labels=True)
plt.show()

# Imprimindo o número cromático do grafo
print(f"O número mínimo de compartimentos para guardar estes produtos químicos em segurança é: {max(colors.values()) + 1}")


