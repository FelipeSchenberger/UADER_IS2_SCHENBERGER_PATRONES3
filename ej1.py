from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class PrimeHandler(AbstractHandler):
    """
    Concrete handler for consuming prime numbers.
    """

    def handle(self, request: Any) -> Optional[str]:
        if self._is_prime(request):
            return f"PrimeHandler: Consumed prime number: {request}"
        else:
            return super().handle(request)

    def _is_prime(self, number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

class EvenHandler(AbstractHandler):
    """
    Concrete handler for consuming even numbers.
    """

    def handle(self, request: Any) -> Optional[str]:
        if self._is_even(request):
            return f"EvenHandler: Consumed even number: {request}"
        else:
            return super().handle(request)

    def _is_even(self, number: int) -> bool:
        return number % 2 == 0

def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for number in range(1, 101):
        result = handler.handle(number)
        if result:
            print(result)
        else:
            print(f"Number {number} was not consumed.")

if __name__ == "__main__":
    prime_handler = PrimeHandler()
    even_handler = EvenHandler()

    prime_handler.set_next(even_handler)

    print("Chain: PrimeHandler > EvenHandler\n")
    client_code(prime_handler)
