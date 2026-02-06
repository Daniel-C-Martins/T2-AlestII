# Desafio das Caixas Aninhadas (Maior Caminho em DAG)

Este projeto foi desenvolvido como parte da disciplina de **Algoritmos e Estruturas de Dados II** no curso de Ciência da Computação da **PUCRS**. 

## 📌 Sobre o Projeto
O objetivo principal é encontrar a maior sequência possível de caixas que podem ser colocadas umas dentro das outras (aninhamento), dado um catálogo de dimensões variadas. 

Para resolver este problema, os dados foram modelados como um **Grafo Acíclico Dirigido (DAG)**, onde cada caixa representa um vértice e uma aresta direcionada indica que uma caixa cabe dentro de outra.

### 🛠️ Tecnologias e Conceitos
* **Linguagem:** Python (implementação de grafos e lógica de comparação).
* **Estruturas de Dados:** Grafos, Listas Adjacentes e Dicionários.
* **Algoritmos:** Ordenação Topológica e algoritmo para encontrar o Caminho Máximo em um DAG.
* **Análise de Complexidade:** O algoritmo apresenta complexidade aproximada de $O(n^2)$.

## 📄 Relatório Técnico Completo
Para uma análise detalhada sobre a modelagem da classe `Box`, a lógica de comparação de dimensões, pseudo-códigos e métricas de desempenho (incluindo gráficos de contagem de operações), acesse o documento completo no link abaixo:

👉 **[Clique aqui para ler o Relatório Técnico (PDF)](./Relatório_T2___Alest_II.pdf)**

O relatório inclui:
* Descrição detalhada da solução.
* Metodologia de testes em diferentes tamanhos de catálogos (de 10 a 10.000 caixas).
* Gráficos de eficiência e complexidade algorítmica.

---
**Autores:** Daniel Campos Martins e Gabriel de Cezaro Tomaz.
