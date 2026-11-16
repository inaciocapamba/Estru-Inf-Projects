# Simulador de Editor de Texto (Undo / Redo com Pilhas)

Projeto desenvolvido em Python para praticar e aplicar o conceito de **Estruturas de Dados**, especificamente o comportamento de **Pilhas (Stacks)** baseado na lógica LIFO (*Last-In, First-Out*).

## 🚀 Sobre o Projeto
Este programa simula um editor de texto via terminal que mantém o controle histórico das alterações efetuadas, permitindo desfazer (`undo`) e refazer (`redo`) ações de forma dinâmica.

## 🧠 Como Funciona
A lógica utiliza duas pilhas principais:
- **Pilha de Undo:** Armazena os estados anteriores do texto a cada nova alteração.
- **Pilha de Redo:** Guarda os estados que foram desfeitos, possibilitando restaurá-los caso necessário.

## 🛠️ Tecnologias Utilizadas
- **Python 3** (Linguagem principal)
- **Conceitos:** Orientação a Objetos e Estruturas de Dados (Pilhas)

## 💻 Como Executar
Certifique-se de ter o Python instalado na sua máquina e execute o seguinte comando no terminal:

```bash
python Gerenciador.py
