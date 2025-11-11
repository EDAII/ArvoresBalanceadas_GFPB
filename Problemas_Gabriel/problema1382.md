# [1382. Balancear uma Árvore de Busca Binária (Balance a Binary Search Tree)](https://leetcode.com/problems/balance-a-binary-search-tree/)

**Dificuldade:** Médio  
**Tópicos:** Árvores, Árvores Binárias, Árvores de Busca Binária, DFS  

---

## Descrição

Dado o nó raiz de uma **árvore de busca binária (BST)**, retorne **uma BST balanceada** que contenha os **mesmos valores de nós**.  
Se houver mais de uma resposta válida, **qualquer uma** pode ser retornada.

Uma **árvore de busca binária é balanceada** se, para **todo nó**, a profundidade de suas duas subárvores **não diferir por mais de 1**.

---

## Exemplo 1

**Entrada:**  
`root = [1,null,2,null,3,null,4,null,null]`

**Saída:**  
`[2,1,3,null,null,null,4]`

**Explicação:**  
Esta não é a única resposta correta — por exemplo, `[3,1,4,null,2]` também é válida.

---

## Exemplo 2

**Entrada:**  
`root = [2,1,3]`

**Saída:**  
`[2,1,3]`

---

## Restrições

- O número de nós na árvore está no intervalo `[1, 10^4]`.  
- `1 <= Node.val <= 10^5`.
