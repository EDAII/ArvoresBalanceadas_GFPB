# [1383. Desempenho Máximo de uma Equipe (Maximum Performance of a Team)](https://leetcode.com/problems/maximum-performance-of-a-team/)

**Dificuldade:** Difícil  
**Tópicos:** Heap, Ordenação, Greedy, Estruturas de Dados  

---

## Descrição

Você recebe dois inteiros `n` e `k`, além de dois arrays inteiros `speed` e `efficiency`, ambos de tamanho `n`.  
Existem `n` engenheiros numerados de `1` a `n`.  
- `speed[i]` representa a **velocidade** do engenheiro `i`.  
- `efficiency[i]` representa a **eficiência** do engenheiro `i`.

O objetivo é **escolher no máximo `k` engenheiros** dentre os `n` para formar uma equipe com **desempenho máximo**.

O **desempenho de uma equipe** é definido como:

> `(soma das velocidades dos engenheiros) × (menor eficiência entre eles)`

Retorne o **desempenho máximo possível** dessa equipe.  
Como o resultado pode ser muito grande, retorne o valor **módulo (10⁹ + 7)**.

---

## Exemplo 1

**Entrada:**  
`n = 6`  
`speed = [2,10,3,1,5,8]`  
`efficiency = [5,4,3,9,7,2]`  
`k = 2`

**Saída:**  
`60`

**Explicação:**  
A melhor equipe é formada pelos engenheiros **2** (velocidade = 10, eficiência = 4) e **5** (velocidade = 5, eficiência = 7).  
Desempenho = `(10 + 5) × min(4, 7) = 15 × 4 = 60`.

---

## Exemplo 2

**Entrada:**  
`n = 6`  
`speed = [2,10,3,1,5,8]`  
`efficiency = [5,4,3,9,7,2]`  
`k = 3`

**Saída:**  
`68`

**Explicação:**  
Selecionando os engenheiros **1**, **2** e **5**:  
Desempenho = `(2 + 10 + 5) × min(5, 4, 7) = 17 × 4 = 68`.

---

## Exemplo 3

**Entrada:**  
`n = 6`  
`speed = [2,10,3,1,5,8]`  
`efficiency = [5,4,3,9,7,2]`  
`k = 4`

**Saída:**  
`72`

---

## Restrições

- `1 <= k <= n <= 10⁵`  
- `speed.length == n`  
- `efficiency.length == n`  
- `1 <= speed[i] <= 10⁵`  
- `1 <= efficiency[i] <= 10⁸`
