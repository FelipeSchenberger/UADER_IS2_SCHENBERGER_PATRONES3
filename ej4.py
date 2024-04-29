import os

class State:
    """
    Clase State base
    """

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))


class AmState(State):
    """
    Implementa cómo barrer las estaciones de AM
    """

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def scan_memories(self):
        print("Escaneando memorias AM...")
        for memory in self.radio.am_memories:
            print("Recuperando memoria AM: {}".format(memory))


class FmState(State):
    """
    Implementa cómo barrer las estaciones de FM
    """

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def scan_memories(self):
        print("Escaneando memorias FM...")
        for memory in self.radio.fm_memories:
            print("Recuperando memoria FM: {}".format(memory))


class Radio:
    """
    Construye la radio con todas sus formas de sintonía
    """

    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.am_memories = ["M1", "M2", "M3", "M4"]
        self.fm_memories = ["M1", "M2", "M3", "M4"]
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    def scan_memories(self):
        self.state.scan_memories()


if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3 + [radio.scan_memories]

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
