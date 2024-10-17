from enum import  IntEnum


class ServiceTypes(IntEnum):
    LAVAGEMACHINE = 1
    LAVAGEMCOMPLETA = 2
    LAVAGEMSECA = 3
    LAVAGEMMOTOR = 4
    LAVAGEMINTERNA = 5
    REPARO = 6

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class StatusTypes(IntEnum):
    PENDENTE = 1
    EMANDAMENTO= 2
    FINALIZADO = 3
    CANCELADO = 4


    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]