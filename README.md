# Introdução à Inteligencia Artificial
Repositório dos trabalhos da matéria de introdução à Inteligência Artificial - Professor Arnaldo - Fatec São Carlos

# Algoritmos de Busca Informada no Mapa da Romênia (A* e Busca Gulosa)

Este repositório contém as implementações e análises comparativas de algoritmos de busca informada aplicados ao clássico problema do **Mapa da Romênia**, baseado no Capítulo 3 do livro clássico *“Inteligência Artificial: Uma Abordagem Moderna”* de Stuart Russell e Peter Norvig.

O objetivo do projeto é determinar caminhos eficientes partindo de qualquer cidade válida dentro do grafo e chegando obrigatoriamente à capital, **Bucareste (Bucharest)**, utilizando abordagens heurísticas distintas.

---

## 🛠️ Descrição do Projeto

O sistema é composto por dois scripts executáveis em ambiente de terminal de linha de comando:
1. **`busca_a_estrela.py`**: Implementa o algoritmo de busca ótima **A***. Ele utiliza uma fila de prioridade para balancear o custo real já percorrido do caminho ($g(n)$) com a estimativa heurística da distância restante em linha reta ($h(n)$), resultando na função de avaliação estável $f(n) = g(n) + h(n)$.
   
2. **`busca_gulosa.py`**: Implementa e confronta duas perspectivas lógicas distintas do algoritmo **Busca Gulosa (Greedy Best-First Search)**:
   * **Abordagem IA**: Implementação padrão estruturada através de uma fronteira ordenada iterativamente que simula uma árvore ou grafo de estados com histórico global de nós visitados.
   * **Abordagem "By Zé"**: Uma rotina de aprendizado com foco puramente procedural e didático desenvolvida pelo programador José Ferrazza. Ela foca no menor valor local de heurística e remove manualmente nós do conjunto de vizinhos dinâmicos baseando-se estritamente nas adjacências imediatas da última cidade visitada.

---

## 📋 Requisitos Funcionais (RF)

* **RF01 - Entrada Interativa de Origem**: O sistema deve permitir que o operador insira via console (`input`) o nome da cidade de partida da busca.
* **RF02 - Validação do Ponto de Partida**: O sistema deve checar obrigatoriamente se a cidade digitada consta na base de dados (heurística/grafo). Se for inválida, exibirá um alerta e repetirá a entrada em loop até o recebimento de um dado válido.
* **RF03 - Destino Imutável**: O alvo final e critério de parada padrão de sucesso para ambos os algoritmos deve ser fixado estritamente na cidade de **'Bucharest'**.
* **RF04 - Cálculo do Caminho Ótimo pelo A***: O script `busca_a_estrela.py` deve processar a malha do mapa, computar a menor rota total possível e imprimir na tela a sequência exata de cidades adjacentes e o custo numérico cumulativo em quilômetros.
* **RF05 - Execução Comparativa na Busca Gulosa**: O script `busca_gulosa.py` deve processar simultaneamente a entrada do usuário através das duas funções internas (`busca_gulosa` e `busca_gulosa_by_ze`), exibindo as rotas geradas por ambas para fins de contraste pedagógico.
* **RF06 - Logs de Expansão em Tempo Real**: Ambos os scripts devem documentar no terminal a sequência de nós expandidos e seus respectivos pesos heurísticos ($h$) no exato momento da operação de remoção da fronteira ou seleção local.

---

## 🛡️ Requisitos Não Funcionais (RNF)

* **RNF01 - Desempenho**: O cálculo do A* e da Busca Gulosa para a malha de dados proposta deve ser concluído e impresso em tempo de execução inferior a 100 milissegundos após a validação da entrada.
* **RNF02 - Segurança**: O sistema deve rodar isolado em escopo de usuário local, sem necessidade de privilégios de administrador (`root`/`sudo`) e sem comunicação externa de rede.
* **RNF03 - Usabilidade**: A interação com o console deve ser simples e autoexplicativa, utilizando menus em caixas de texto ASCII formatadas para melhorar o foco visual do usuário.
* **RNF04 - Disponibilidade**: Os scripts devem operar de maneira totalmente offline (standalone), garantindo 100% de disponibilidade operacional independente de servidores externos.
* **RNF05 - Escalabilidade**: A estrutura de dados baseada em Listas de Adjacência (`dict` contendo `list` de `tuples`) deve permitir o escalonamento e inserção de novas cidades e custos rodoviários sem necessidade de reconfiguração lógica das funções de busca.
* **RNF06 - Manutenabilidade**: O código-fonte deve conter comentários claros separando as regras de negócio de IA das estruturas acessórias, facilitando refatorações futuras ou uso como material didático.
* **RNF07 - Confiabilidade**: O algoritmo A* deve ser matematicamente garantido como completo e ótimo devido à natureza admissível e consistente da tabela de heurísticas fornecida (distância em linha reta).
* **RNF08 - Compatibilidade**: Os arquivos do projeto devem ser compatíveis e interpretados nativamente em qualquer ambiente operacional que possua suporte ao **Python 3.6 ou superior**, utilizando apenas módulos nativos (como o `heapq`).

---

## 📊 Diagramas do Sistema

### 1. Diagrama de Casos de Uso (UML)
O diagrama abaixo mapeia os limites do sistema e o papel do Professor/Aluno (Usuário) ao interagir com as rotinas de busca.

```mermaid
graph TD
    User((Usuário / Aluno))
    
    subgraph Sistema de Busca Informada
        UC1(Informar Cidade de Partida)
        UC2(Validar Cidade no Mapa)
        UC3(Executar Busca A*)
        UC4(Executar Busca Gulosa Comparativa)
        UC5(Visualizar Rota e Custo Total)
        UC6(Visualizar Logs de Expansão)
    end
    
    User --> UC1
    UC1 --> UC2
    User --> UC3
    User --> UC4
    UC3 --> UC5
    UC4 --> UC5
    UC4 --> UC6
