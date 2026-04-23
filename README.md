# Constante de Kaprekar (6174)

Projeto desenvolvido em Python que demonstra a **Constante de Kaprekar**, um fenômeno matemático curioso: dado qualquer número de 4 dígitos (com algumas restrições), ao repetir um processo simples de subtração, sempre chegamos ao número **6174**.

---

## O que é a Constante de Kaprekar?

A constante de Kaprekar foi descoberta pelo matemático indiano D. R. Kaprekar em 1949. O processo funciona assim:

1. Escolha um número de até 4 dígitos.
2. Organize seus dígitos em ordem **decrescente** → forma o número maior.
3. Organize seus dígitos em ordem **crescente** → forma o número menor.
4. Subtraia o menor do maior.
5. Repita o processo com o resultado.

Em no máximo **7 iterações**, o resultado sempre será **6174**.

**Exemplo:**
```
3524 → 5432 - 2345 = 3087
3087 → 8730 - 0378 = 8352
8352 → 8532 - 2358 = 6174 ✓
```

---

## Como funciona o programa

O programa solicita um número ao usuário e realiza três validações antes de iniciar o processo:

- O número deve ser **positivo**.
- O número deve ter no **máximo 4 dígitos** (0000 a 9999).
- O número não pode ter **3 ou mais dígitos iguais** (ex: 1112 ou 5555 não convergem para 6174).

Após as validações, o programa executa o laço de Kaprekar e exibe cada iteração até atingir 6174.

---

## Como executar

Certifique-se de ter o **Python 3** instalado. Em seguida, execute:

```bash
python kaprekar.py
```

O programa pedirá um número e exibirá o passo a passo até a constante.

---

## Exemplo de saída

```
Digite um número de até 4 dígitos: 1234

Número informado: 1234

Iteração 1 : 4321 - 1234 = 3087
Iteração 2 : 8730 - 0378 = 8352
Iteração 3 : 8532 - 2358 = 6174

Constante de Kaprekar (6174) atingida em 3 iterações.
```

---

## Tecnologias

- **Python 3** — sem dependências externas, apenas a biblioteca padrão.

---

## Autor

Desenvolvido como exercício de lógica de programação.
