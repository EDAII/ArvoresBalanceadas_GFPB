# [352. Fluxo de Dados como Intervalos Disjuntos (Data Stream as Disjoint Intervals)](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

**Dificuldade:** Difícil  
**Tópicos:** Árvores Balanceadas
**Descrição:**

Dado um fluxo de dados de inteiros não negativos `a_1, a_2, ..., a_n`, sumarize os números vistos até agora como uma lista de intervalos disjuntos.

Implemente a classe `SummaryRanges`:

- `SummaryRanges` Inicializa o objeto com um fluxo vazio.

- `void addNum(int value)` Adiciona o inteiro `value` ao fluxo.

- `int[][] getIntervals()` Retorna um resumo dos inteiros no fluxo atualmente como uma lista de intervalos disjuntos `[start_i, end_i]`. A resposta deve ser ordenada pelo `start_i`. 

---

## Exemplos:

### Exemplo 1:

**Entrada:** `["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]`

**Saída:** `[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]`

**Explicação:**  As listas ligadas são: 
`SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // retorna [[1, 1]]

summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // retorna [[1, 1], [3, 3]]

summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // retorna [[1, 1], [3, 3], [7, 7]]

summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // '2' se junta a [1, 1] e [3, 3] -> [[1, 3], [7, 7]]

summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // '6' se junta a [7, 7] -> [[1, 3], [6, 7]]`

---

## Restrições:

- `0 <= value <= 10^4`.
- No máximo `3 * 10^4` chamadas serão feitas para `addNum` e `getIntervals`.
- No máximo `10^2` chamadas serão feitas para `getIntervals`.