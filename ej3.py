from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice
from string import ascii_uppercase
from typing import List


class Subject(ABC):
    """
    La interfaz Subject declara un conjunto de métodos para manejar suscriptores.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Adjunta un observador al sujeto.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Desvincula un observador del sujeto.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notifica a todos los observadores sobre un evento.
        """
        pass


class ConcreteSubject(Subject):
    """
    ConcreteSubject posee un estado importante y notifica a los observadores cuando el estado cambia.
    """

    _state: int = None
    """
    Por simplicidad, el estado del ConcreteSubject, esencial para todos los suscriptores, se almacena en esta variable.
    """

    _observers: List[Observer] = []
    """
    Lista de suscriptores. En la vida real, la lista de suscriptores puede almacenarse de manera más completa 
    (categorizada por tipo de evento, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Sujeto: Se ha adjuntado un observador.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Métodos de gestión de suscripción.
    """

    def notify(self) -> None:
        """
        Desencadena una actualización en cada suscriptor.
        """
        print("Sujeto: Notificando a los observadores...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Normalmente, la lógica de suscripción es solo una fracción de lo que un Sujeto realmente puede hacer.
        Los Sujetos comúnmente contienen alguna lógica empresarial importante, que desencadena un método de notificación 
        cada vez que algo importante está a punto de suceder (o después).
        """
        print("\nSujeto: Estoy haciendo algo importante.")
        self._state = choice(range(10))
        print(f"Sujeto: Mi estado ha cambiado a: {self._state}")
        self.notify()


class Observer(ABC):
    """
    La interfaz Observer declara el método de actualización, utilizado por los sujetos.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Recibe una actualización del sujeto.
        """
        pass


class ConcreteObserverA(Observer):
    _id: str = "ABCD"

    def update(self, subject: Subject) -> None:
        if self._id in subject._state:
            print(f"ConcreteObserverA: ID coincidente {self._id}")


class ConcreteObserverB(Observer):
    _id: str = "WXYZ"

    def update(self, subject: Subject) -> None:
        if self._id in subject._state:
            print(f"ConcreteObserverB: ID coincidente {self._id}")


class ConcreteObserverC(Observer):
    _id: str = "PQRS"

    def update(self, subject: Subject) -> None:
        if self._id in subject._state:
            print(f"ConcreteObserverC: ID coincidente {self._id}")


class ConcreteObserverD(Observer):
    _id: str = "MNOQ"

    def update(self, subject: Subject) -> None:
        if self._id in subject._state:
            print(f"ConcreteObserverD: ID coincidente {self._id}")


if __name__ == "__main__":
    # Código del cliente.
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    observer_c = ConcreteObserverC()
    subject.attach(observer_c)

    observer_d = ConcreteObserverD()
    subject.attach(observer_d)

    # Emitir 8 ID y notificar a los observadores.
    for _ in range(8):
        subject.some_business_logic()
