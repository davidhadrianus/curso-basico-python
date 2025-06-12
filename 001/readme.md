## Módulo 1: Introdução ao Python


---

### **Aula 1: O que é Python? Instalação e Primeiros Passos**

**O que é Python?**
Python é uma linguagem de programação de alto nível, interpretada, de fácil leitura e escrita, muito usada em ciência de dados, inteligência artificial, automação, web, entre outras áreas. Seu código é limpo e possui uma sintaxe simples, o que facilita o aprendizado.

**Vantagens:**

- Sintaxe simples e legível
- Comunidade ativa e vasta documentação
- Grande variedade de bibliotecas

**Instalação:**

- Acesse [python.org](https://www.python.org/downloads/) e baixe a versão mais recente para seu sistema operacional.
- Siga as instruções do instalador (marque a opção “Add Python to PATH” no Windows).
- Para verificar a instalação, abra o terminal (Prompt de Comando ou Terminal) e digite:

```bash
python --version
```

- Para executar o interpretador interativo, digite:

```bash
python
```

- Para rodar um arquivo `.py`, use:

```bash
python nome_do_arquivo.py
```


**Primeiro programa:**

```python
print("Olá, mundo!")
```


---

### **Variáveis, Tipos de Dados e Operadores**

**Variáveis:**
São espaços na memória para armazenar valores. Basta atribuir um valor a um nome:

```python
nome = "Ana"
idade = 25
```

**Tipos de Dados:**

- `int` (inteiro): 10, -5, 0
- `float` (decimal): 3.14, -0.1
- `str` (texto): "Python", 'curso'
- `bool` (booleano): True, False

**Operadores:**

- Aritméticos: `+`, `-`, `*`, `/`, `//` (divisão inteira), `%` (resto), `**` (potência)
- Relacionais: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Lógicos: `and`, `or`, `not`

**Exemplo:**

```python
a = 10
b = 3
print(a + b)      # 13
print(a / b)      # 3.333...
print(a ** b)     # 1000
```


---

### **Entrada e Saída de Dados**

**Saída de dados:**
Usa-se a função `print()` para mostrar informações na tela.

```python
print("Bem-vindo ao curso de Python!")
```

**Entrada de dados:**
Usa-se a função `input()` para receber dados do usuário (sempre retorna uma string).

```python
nome = input("Digite seu nome: ")
print("Olá,", nome)
```

Para converter para número:

```python
idade = int(input("Digite sua idade: "))
```


---

### **Aula 4: Estruturas Condicionais (if, elif, else)**

Permitem executar diferentes blocos de código conforme condições.

**Sintaxe:**

```python
if condição:
    # bloco se condição for verdadeira
elif outra_condição:
    # outro bloco
else:
    # bloco se nenhuma condição for verdadeira
```

**Exemplo:**

```python
idade = int(input("Qual sua idade? "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```


---

### **Estruturas de Repetição (for, while)**

Permitem executar um bloco de código várias vezes.

**For:**
Usado para percorrer sequências (listas, strings, intervalos).

```python
for i in range(5):
    print(i)  # Imprime 0 a 4
```

**While:**
Repete enquanto a condição for verdadeira.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```


---

## Exercícios Práticos

1. Escreva um programa que peça o nome e a idade do usuário e exiba uma mensagem personalizada.
2. Faça um programa que leia dois números, some-os e mostre o resultado.
3. Peça um número ao usuário e diga se ele é par ou ímpar.
4. Imprima os números de 1 a 10 usando um `for`.
5. Crie um programa que peça notas até que o usuário digite -1 e, ao final, mostre a média das notas.

Se quiser exemplos resolvidos ou mais exercícios, é só pedir!

