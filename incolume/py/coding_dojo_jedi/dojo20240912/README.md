# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Faturar pythonicamente solução csharp**

Transforme em Python a implementação CShap abaixo.

```cs 
using System;

class Program
{
    public static void Main()
    {
        var stack = new Stack<object>();
        stack.Push(new
        {
            a = 1,
            b = 2
        });

        stack.Push(@"Como a pilha é genérica, podemos inserir quaisquer elementos,
                     até objetos heterogêneos");

        stack.Push(new
        {
            MadeIn = "Brazil"
        });

        stack.Push("Execute esse código para ver a pilha ser invertida");

        while (stack.Count > 0)
        {
            Console.WriteLine(stack.Pop());
        }
    }
}


public class Stack<T>
{
    private StackItem<T> topo; // Utilizado para vincular os elementos
    private bool isPilhaVazia
    {
        get { return this.Count == 0; } // Determina se temos itens na pilha
    }
    public int Count;

    // Método que empilha
    public void Push(T item)
    {
        if (isPilhaVazia)
            this.topo = new StackItem<T>(item); // Pilha contém um único elemento
        else
        {
            var stackItem = new StackItem<T>(topo, item); // Inserimos um novo topo vinculado ao antigo
            this.topo = stackItem; // Declaramos o novo topo
        }
        this.Count++;
    }

    // Método que desempilha
    public T Pop()
    {
        if (isPilhaVazia)
            throw new IndexOutOfRangeException(); // Não é possível remover itens de uma pilha vazia
        else
        {
            T item = this.topo.item; // Obtemos o valor armazenado no topo
            this.topo = this.topo.anterior; // Movemos o ponteiro do topo para o item anterior

            this.Count--;
            return item; //Retornamos o valor armazenado
        }
    }

    //Classe de suporte as operações da pilha, responsável por vincular os elementos e armazenar valores
    private class StackItem<T>
    {
        public T item; // Valor, genérico
        public StackItem<T> anterior; // Vinculo com o item anterior ou abaixo da pilha

        public StackItem(T item)
        { // Constructor de uma pilha vazia
            this.item = item;
        }

        public StackItem(StackItem<T> anterior, T item)
        { // Constructor de uma pilha com elementos
            this.anterior = anterior; // Vincula o atual com o anterior
            this.item = item; // Armazena o valor
        }
    }
}
```

## Exemplos

<details> 
  <summary>Spoiler?</summary> 
   Considerar em caso de fatoração:

    > modo pythônico
    > sem condicionais 
    > estruturas performáticas
    > redução de complexidade ciclomática 
    > análise assintótica de algoritmos (big O)

</details>

N/A - Exemplos de solução e resposta do problema. Geralmente utilizado para validar os testes do TDD.

## Artefatos

- [dojo](__init__.py)
- [tests](test_20240912.py)


## Referências

- https://gist.github.com/cfguimaraes/4a286c64b0194e668b9e6fd86ae1f7a4

N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright &copy; **incolume.com.br** since 2010