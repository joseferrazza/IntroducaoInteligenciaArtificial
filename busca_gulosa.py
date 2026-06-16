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

# Rotina desenvolvida pelo José Ferrazza após entendimento do algoritmo de busca gulosa.
# Foco em fazer um código mais compreemsivel


def busca_gulosa_by_ze(inicio, objetivo, mapa, heuristica):

    # list que armazena os vizinhos de cada cidade pesquisada - convert de dict pra list
    vizinhos_m = set(list([(mapa[inicio])])[0])
    # list que armazena as cidades visitadas
    cidades_v = []
    # variavel que aramazena a melhor cidade em cada iteração
    cidade_m = ""

    # define a primeira cidade visitada como aquela de onde partimos
    cidades_v.append(inicio)

    print(f"Expandindo: {inicio} (h = {heuristica[inicio]})")

    while cidade_m != objetivo:

        # dict que armazena as cidades vizinhas com a distancia da heuristica
        vizinhos_h = dict()
        # laço que percorre os vizinhos e inclui a distância da heuristica (linha reta)
        for c, d in vizinhos_m:
            vizinhos_h[c] = heuristica[c]

        # seleciona a cidade com a menor distância em linha reta
        cidade_m = min(vizinhos_h, key=vizinhos_h.get)
        # insere a cidade com a melhor heuristica na lista de cidades visitadas
        cidades_v.append(cidade_m)
        # lista que armazena os vizinhos da melhor cidade
        vizinhos_m = set(list([(mapa[cidade_m])])[0])
        # lista auxiliar criada para deletar as cidades visitadas da lista dos vizinhos da proxima cidade
        vizinhos_m_aux = set(list(vizinhos_m))
        # laço que remove as cidades já visitadas
        for item in vizinhos_m_aux:
            if item[0] in cidades_v:
                vizinhos_m.remove(item)
        print(f"Expandindo: {cidade_m} (h = {heuristica[cidade_m]})")

    return cidades_v

# Rotina desenvolvida pelo IA que serviu para auxiliar na compreensão do algoritmo de busca gulosa


def busca_gulosa(inicio, objetivo, grafo, heuristica):
    # Cada elemento na fronteira será uma tupla: (valor_h, cidade_atual, caminho_ate_aqui)
    # Começamos com a cidade de origem
    fronteira = [(heuristica[inicio], inicio, [inicio])]

    # Conjunto para armazenar nós já expandidos (evita loops e redundâncias)
    visitados = set()

    while fronteira:
        # Ordena a fronteira com base no valor da heurística h(n) -> Menor primeiro
        fronteira.sort(key=lambda x: x[0])

        # Remove o nó com menor h(n) da fronteira
        h_atual, cidade_atual, caminho = fronteira.pop(0)

        print(f"Expandindo: {cidade_atual} (h = {h_atual})")

        # Teste de Objetivo
        if cidade_atual == objetivo:
            return caminho

        # Se a cidade ainda não foi expandida
        if cidade_atual not in visitados:
            visitados.add(cidade_atual)

            # Varre os vizinhos da cidade atual
            for vizinho, _ in grafo.get(cidade_atual, []):
                if vizinho not in visitados:
                    novo_caminho = caminho + [vizinho]
                    # Insere na fronteira priorizando a heurística h(n) do vizinho
                    fronteira.append(
                        (heuristica[vizinho], vizinho, novo_caminho))

    return None  # Se a fronteira esvaziar e não achar o objetivo


# --- Execução do Teste Clássico do Livro (Saindo de Arad para Bucareste) ---

print("┌──────────────────────────────────────────────┐")
print("│                 Busca Gulosa                 │")
print("└──────────────────────────────────────────────┘")

while True:
    partida = input("A partir de qual cidade deseja partir?\n")

    if partida not in heuristica_bucareste:
        print(f"A cidade {partida} não existe. Digite outra cidade.\n")
    else:
        break
print("────────────────────────────────────────────────")
print(f"--> Iniciando Busca Gulosa de {partida} para Bucharest")
print("────────────────────────────────────────────────")

print("\n┌──────────────────────────────────────────────┐")
print("│                   Resultado                  │")
print("└──────────────────────────────────────────────┘")

print("────────────────────────────────────────────────")
print("--> Resultado usando o algoritmo feito pela IA")
print("────────────────────────────────────────────────")
caminho_final = busca_gulosa(
    partida, 'Bucharest', mapa_romenia, heuristica_bucareste)

if caminho_final:
    print("\nCaminho encontrado (Dev by IA):", " -> ".join(caminho_final))
else:
    print("\nNão foi possível encontrar um caminho.\n")

print("\n────────────────────────────────────────────────")
print("--> Resultado usando o algoritmo feito pelo Zé")
print("────────────────────────────────────────────────")

caminho_final = busca_gulosa_by_ze(
    partida, 'Bucharest', mapa_romenia, heuristica_bucareste)

if caminho_final:
    print("\nCaminho encontrado (Dev by Zé):", " -> ".join(caminho_final))
else:
    print("\nNão foi possível encontrar um caminho.\n")
