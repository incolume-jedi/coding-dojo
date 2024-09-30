"""dojo module."""

import logging
from dataclasses import dataclass
from typing import Any, Self


class SizeError(Exception):
    """Size error."""


@dataclass
class Rules:
    """Rules."""


def is_validate(value: list) -> bool:
    """Validade entrance."""
    rules = Rules()
    rules.max_value = 100
    rules.max_size = 30
    rules.merr_value = f'Somente valores entre 0 e {rules.max_value}'
    rules.merr_sz = f'Quantidade maxima de nodos é {rules.max_size}'

    if len(value) > rules.max_size:
        raise SizeError(rules.merr_sz)

    if any(x for x in value if x > rules.max_value or x < 0):
        raise ValueError(rules.merr_value)

    return bool(value)


def dojo(lista: list, nodo: int) -> list[int]:
    """Dojo solution."""
    is_validate(lista)
    try:
        lista.pop(nodo)
    except IndexError:
        lista.pop(-1)
    return lista


@dataclass
class Node:
    """Nodo."""

    data: Any
    index: int = -1
    next: Self | None = None


@dataclass
class LinkedList:
    """Linked list."""

    head: Node = None
    length: int = 0

    def push(self, data):
        """Push values."""
        new_node = Node(data)
        new_node.next = self.head
        try:
            new_node.index = self.head.index + 1
        except ArithmeticError:
            logging.exception()
        except AttributeError:
            new_node.index += 1

        self.head = new_node
        self.length += 1

    def display(self):
        """Show elements."""
        temp = self.head
        while temp:
            print(temp.data)  # noqa: T201
            temp = temp.next

    def pop(self, n):
        """Pop values."""
        parent, temp = self.head, self.head
        while temp:
            if temp.index == n:
                self.head = temp.next.next
            temp = temp.next
