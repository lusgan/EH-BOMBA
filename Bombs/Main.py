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
    "Ácido acético": ["Ácido nítrico", "Peróxidos"],
    "Ácido nítrico": ["Ácido acético", "Ácido clorídrico"],
    "Amônia": ["Cloro", "Bromo", "Ácido fluorídrico"],
    "Cloro": ["Amônia", "Acetileno", "Éter"],
    "Hidróxido de sódio": ["Ácidos", "Água"],
    "Peróxidos orgânicos": ["Ácidos", "Materiais combustíveis"]
}

class Estante:
    
    
    def __init__(self):
        self.G = nx.Graph()

        
    def adicionarMaterial(self, material, pode_colocar_no_alto):
        self.G.add_node(material)

    
    def conectar(self, materialA, materialB):
        
        if materialA in self.G.nodes() and materialB in self.G.nodes():
            self.G.add_edge(materialA, materialB)
            
        else:
            print("Algum dos materiais fornecidos nao existe")

    
    def mostrarGrafo(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


estante = Estante()
estante.adicionarMaterial("polvora", True)
estante.adicionarMaterial("faisca", True)
estante.conectar("faisca", "polvora")
estante.mostrarGrafo()


