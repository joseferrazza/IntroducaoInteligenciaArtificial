import heapq

# Grafo representando o mapa da Romênia (Capítulo 3 do Russell & Norvig)
# Formato: 'Cidade_Origem': [('Cidade_Vizinha', custo_real_da_estrada), ...]
mapa_romenia = {
    'Arad':             [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind':           [('Arad', 75), ('Oradea', 71)],
    'Oradea':           [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu':            [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara':        [('Arad', 118), ('Lugoj', 111)],
    'Lugoj':            [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia':          [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta':          [('Mehadia', 75), ('Craiova', 120)],
    'Craiova':          [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea':   [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras':          [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti':          [('Rimnicu Vilcea', 97),    ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest':        [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu':          [('Bucharest', 90)],
    'Urziceni':         [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova':          [('Urziceni', 98), ('Eforie', 86)],
    'Eforie':           [('Hirsova', 86)],
    'Vaslui':           [('Urziceni', 142), ('Iasi', 92)],
    'Iasi':             [('Vaslui', 92), ('Neamt', 87)],
    'Neamt':            [('Iasi', 87)]
}

# Heurística h(n): Distância em linha reta de cada cidade até BUCUBARESTE (Bucharest)
heuristica_bucareste = {
    'Arad': 366,    'Bucharest': 0,   'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77,    'Hirsova': 151, 'Iasi': 226,    'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234,     'Oradea': 380,  'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253,   'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199,  'Zerind': 374
}


def busca_a_estrela(grafo, heuristica, inicio, objetivo):
    # Fila de prioridade armazena: (f_cost, custo_g_atual, cidade_atual, caminho_percorrido)
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]

    # Dicionário para rastrear o menor custo g encontrado para cada cidade
    visitados = {}

    while fronteira:
        # Remove o nó com menor f(n) da fila
        f_atual, g_atual, nodo_atual, caminho = heapq.heappop(fronteira)

        # Teste de objetivo
        if nodo_atual == objetivo:
            return caminho, g_atual

        # Ignora se já encontramos um caminho melhor ou igual para este nó antes
        if nodo_atual in visitados and visitados[nodo_atual] <= g_atual:
            continue

        visitados[nodo_atual] = g_atual

        # Modificação aqui: Iterando sobre a lista de tuplas do novo formato
        for vizinho, distancia_estrada in grafo[nodo_atual]:
            g_novo = g_atual + distancia_estrada
            h_novo = heuristica[vizinho]
            f_novo = g_novo + h_novo

            # Se o vizinho não foi visitado ou encontramos um caminho mais curto
            if vizinho not in visitados or g_novo < visitados[vizinho]:
                heapq.heappush(fronteira, (f_novo, g_novo,
                               vizinho, caminho + [vizinho]))

    return None, float('inf')

# --- Execução do Teste Clássico do Livro (Saindo de Arad para Bucareste) ---


print("┌──────────────────────────────────────────────┐")
print("│                   Busca A*                   │")
print("└──────────────────────────────────────────────┘")

while True:
    partida = input("A partir de qual cidade deseja partir?\n")

    if partida not in heuristica_bucareste:
        print(f"A cidade {partida} não existe. Digite outra cidade.\n")
    else:
        break
print("────────────────────────────────────────────────")
print(f"--> Iniciando Busca A* de {partida} para Bucharest")
print("────────────────────────────────────────────────")

print("\n┌──────────────────────────────────────────────┐")
print("│                   Resultado                  │")
print("└──────────────────────────────────────────────┘")

print("────────────────────────────────────────────────")
print("--> Resultado usando o algoritmo feito pela IA")
print("────────────────────────────────────────────────")

rota_otima, custo_total = busca_a_estrela(
    mapa_romenia, heuristica_bucareste, partida, 'Bucharest')

print(f"Origem: {partida} -> Destino: Bucharest")
print(f"Rota recomendada: {' -> '.join(rota_otima)}")
print(f"Custo total do caminho: {custo_total} km")
