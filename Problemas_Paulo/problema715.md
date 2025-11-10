# [715. Módulo de Intervalos(Range Module)](https://leetcode.com/problems/range-module/description/)

**Dificuldade:** Difícil  
**Tópicos:** Árvores Balanceadas
**Descrição:**

Um Módulo de Intervalos é um módulo que rastreia intervalos de números. Projete uma estrutura de dados para rastrear os intervalos representados como intervalos semiabertos e realizar consultas sobre eles.

Um intervalo semiaberto `[left, right)` denota todos os números reais `x` onde `left <= x < right`.

Implemente a classe `RangeModule`:

- `RangeModule()` Inicializa o objeto da estrutura de dados.

- `void addRange(int left, int right)` Adiciona o intervalo semiaberto `[left, right)`, rastreando cada número real nesse intervalo. Adicionar um intervalo que se sobrepõe parcialmente com números atualmente rastreados deve adicionar quaisquer números no intervalo `[left, right)` que ainda não estejam rastreados (realizando a fusão).

- `boolean queryRange(int left, int right)` Retorna `true` se cada número real no intervalo `[left, right)` estiver atualmente sendo rastreado, e `false` caso contrário.

- `void removeRange(int left, int right)` Para de rastrear todos os números reais atualmente rastreados no intervalo semiaberto `[left, right)`.

---

## Exemplos:

### Exemplo 1:

**Entrada:** `["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]`

**Saída:** `[null, null, null, true, false, true]`

**Explicação:**  
- `RangeModule rangeModule = new RangeModule();`
- `rangeModule.addRange(10, 20);`
- `rangeModule.removeRange(14, 16);`
- `rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)`
- `rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)`
- `rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)`
---

## Restrições:

- `1 <= left < right <= 10^9`.
- No máximo `10^4` chamadas serão feitas para `addRange` e `queryRange` e `removeRange`.