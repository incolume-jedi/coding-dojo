"""dojo module."""

# This code is using a custom stack implementation in Python

import logging


class Program:
    """Program class."""

    @staticmethod
    def main():
        """Main method."""
        stack = Stack()
        stack.push({'a': 1, 'b': 2})

        stack.push(
            'Como a pilha é genérica, podemos inserir quaisquer elementos,\n'
            'até objetos heterogêneos',
        )

        stack.push({'MadeIn': 'Brazil'})

        stack.push('Execute esse código para ver a pilha ser invertida')

        while stack.count > 0:
            logging.debug(stack.pop())


class Stack:
    """Stack class.

    Class to support stack operations, responsible for
    linking elements and storing values
    """

    def __init__(self):
        """Init this."""
        self.top = None  # Used to link the elements
        self.count = 0

    @property
    def is_empty(self):
        """Check empty."""
        return self.count == 0  # Determines if there are items in the stack

    # Method to push an item onto the stack
    def push(self, item):
        """Push method."""
        if self.is_empty:
            self.top = StackItem(item)  # Stack contains a single element
        else:
            self.top = StackItem(
                self.top,
                item,
            )
        self.count += 1

    # Method to pop an item from the stack
    def pop(self):
        """Pop method."""
        msg = 'Cannot remove items from an empty stack'
        if self.is_empty:
            raise IndexError(msg)  # Cannot remove items from an empty stack
        item = self.top.item  # Get the value stored at the top
        self.top = (
            self.top.previous
        )  # Move the top pointer to the previous item
        self.count -= 1
        return item  # Return the stored value


class StackItem:
    """StackItem class."""

    def __init__(self, item, previous=None):
        """Init this."""
        self.item = item  # Generic value
        self.previous = (
            previous  # Link to the previous item or below in the stack
        )
