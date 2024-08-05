from agent.sensors_actions import Sensors, Actions

from typing import Self
from dataclasses import dataclass, field
import struct
import random


# ------------------------------------------------------------------------------
# WE START HERE ASSUMING ONLY PAIRWISE SENSOR -> ACTION CONNECTIONS ARE POSSIBLE
#
# TODO: BUILD A PERCEPTRON NETWORK FROM GENOME
# ------------------------------------------------------------------------------


@dataclass
class Gene:
    source: Sensors | Actions
    weight: float
    
    def __hash__(self) -> int: return hash(self.byte)
    def __eq__(self, value: Self) -> bool: return True if self.byte == value.byte else False
    @staticmethod
    def random_weight() -> float: return random.randint(0, 100) / 100
    @property
    def sa(self) -> bool: return 1 if isinstance(self.source, Sensors) else 0
    @property
    def byte(self) -> bytes: return struct.pack('ii', self.sa, self.source.value)

@dataclass
class Genome:
    gene_sequence: tuple[Gene]
    connections: dict[int, tuple[Gene]] = field(default_factory=dict)

    def make_random_connections(self, max_connections: int) -> None: self.connections.update({i: (random.choice(self.gene_sequence), random.choice(self.gene_sequence)) for i in range(max_connections)}) 
    def remove_invalid_connections(self) -> None: self.connections.pop(i for i, (a, b) in self.connections.items() if a == b or not self._valid_pair(a, b))
    def _valid_pair(a: Gene, b: Gene) -> bool: return isinstance(a, Sensors) and isinstance(b, Actions)

@dataclass
class Perceptron:
    inputs: Genome

@dataclass
class NeuralNetwork:
    pass

if __name__ == "__main__":
    g = Genome(tuple(random.choices((*list(Sensors), *list(Actions)), k=30)))
    g.make_random_connections(10)
    g.remove_invalid_connections()