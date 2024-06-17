import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_large_scale_graph(num_nodes, probability):
    # Gera um grafo aleatório com uma probabilidade definida de arestas entre os nós
    G = nx.erdos_renyi_graph(num_nodes, probability)
    return G

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
def gerar_produtos_quimicos(estante, num_produtos, probabilidade):
    # Adiciona os produtos químicos à estante
    for i in range(num_produtos):
        produto = str(i)
        pode_colocar_no_alto = random.random() < probabilidade
        estante.adicionarMaterial(produto, pode_colocar_no_alto)
    
    # Cria conexões entre produtos químicos que não podem estar juntos
    for i in range(num_produtos):
        for j in range(i+1, num_produtos):
            if random.random() < probabilidade:
                estante.conectar(str(i), str(j))
def coloracao_gulosa(G):
    colors = {}  # Dicionário para armazenar as cores dos nós
    for node in G.nodes():  # Itera sobre cada nó no grafo
        available_colors = set(range(len(G)))  # Cria um conjunto de cores possíveis
        for neighbor in G[node]:  # Verifica as cores dos vizinhos
            if neighbor in colors:  # Se o vizinho já tiver uma cor
                available_colors.discard(colors[neighbor])  # Remove essa cor das disponíveis
        colors[node] = min(available_colors)  # Atribui a menor cor disponível ao nó
    return colors


# Imprimindo o número cromático do grafo
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
print(f"Materias de verdade: O número mínimo de compartimentos para guardar estes produtos químicos em segurança é: {max(colors.values()) + 1}")
estante = Estante()
num_produtos = 100  # Número de produtos químicos
probabilidade = 0.5  # Probabilidade de poderem ou não estar um ao lado do outro
gerar_produtos_quimicos(estante, num_produtos, probabilidade)
estante.mostrarGrafo()
colors = coloracao(estante.G)
nx.draw(estante.G, node_color=[colors[node] for node in estante.G.nodes()], with_labels=True)
plt.show()

# Imprimindo o número cromático do grafo
print(f"Ideal: O número mínimo de compartimentos para guardar estes produtos químicos em segurança é: {max(colors.values()) + 1}")


colors = coloracao_gulosa(estante.G)
nx.draw(estante.G, node_color=[colors[node] for node in estante.G.nodes()], with_labels=True)
plt.show()

# Imprimindo o número cromático do grafo
print(f"Gulosa: O número mínimo de compartimentos para guardar estes produtos químicos em segurança é: {max(colors.values()) + 1}")
