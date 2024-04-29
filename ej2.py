from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class BidirectionalIterator(Iterator):
    """
    Implementa un iterador que puede recorrer una cadena en sentido directo e inverso.
    """

    def __init__(self, collection: str, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0
        self._step = -1 if reverse else 1

    def __next__(self) -> str:
        """
        El método __next__() debe devolver el siguiente elemento en la secuencia.
        Al alcanzar el final, y en llamadas posteriores, debe lanzar StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += self._step
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    La clase WordsCollection almacena una cadena de caracteres y proporciona métodos para
    obtener iteradores en sentido directo y reverso.
    """

    def __init__(self, collection: str = "") -> None:
        self._collection = collection

    def __iter__(self) -> BidirectionalIterator:
        """
        Devuelve un iterador en sentido directo.
        """
        return BidirectionalIterator(self._collection)

    def get_reverse_iterator(self) -> BidirectionalIterator:
        """
        Devuelve un iterador en sentido inverso.
        """
        return BidirectionalIterator(self._collection, reverse=True)

    def add_item(self, item: str):
        """
        Agrega un carácter a la cadena.
        """
        self._collection += item


if __name__ == "__main__":
    collection = WordsCollection("iterator")

    print("Recorrido en sentido directo:")
    direct_iterator = iter(collection)
    for char in direct_iterator:
        print(char, end=" ")

    print("\nRecorrido en sentido inverso:")
    reverse_iterator = collection.get_reverse_iterator()
    for char in reverse_iterator:
        print(char, end=" ")
