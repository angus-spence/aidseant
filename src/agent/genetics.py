from agent.sensors_actions import Sensors, Actions, Internal

from typing import Self
from dataclasses import dataclass, field
import struct
import random


# --------------------------------------------------------- # 
# - GENOME SPECIFIES WIRING OF NEURONS                      #
# - EACH GENONE SPECIFIES 1 NURUAL CONNECTION               #
# - WE START HERE ASSUMING ONLY PAIRWISE SENSOR -> ACTION   #
#   CONNECTIONS ARE POSSIBLE                                #
#                                                           #
#                                                           #
#                                                           #
# TODO: BUILD A PERCEPTRON NETWORK FROM GENOME              #
# --------------------------------------------------------- #


@dataclass
class Neuron:
    id: int
    classifcaiton: Sensors | Actions | Internal
    x: float = 0.0

    def __hash__(self) -> int: return hash(self.byte)
    def __eq__(self, value: Self) -> bool: return True if self.byte == value.byte else False
    @property
    def byte(self) -> bytes: return struct.pack('ii', self.classification_type, self.classifcaiton.value)
    @property
    def classification_type(self) -> bool: return 1 if isinstance(self.classifcaiton, Sensors) else 0

@dataclass
class Gene:
    source: Neuron
    destination: Neuron
    w: float
    
    def __hash__(self) -> int: return hash(self.byte)
    def __eq__(self, value: Self) -> bool: return True if self.byte == value.byte else False
    @staticmethod
    def random_weight() -> float: return random.randint(0, 100) / 100
    @property
    def source_type(self) -> bool: return 1 if isinstance(self.source.classifcaiton, Sensors) else 0
    @property
    def destination_type(self) -> bool: return 1 if isinstance(self.destination, Sensors) else 0
    @property
    def byte(self) -> bytes: return struct.pack('iiii', self.source_type, self.destination_type, self.source.classifcaiton.value, self.destination.classifcaiton.value)

@dataclass
class Genome:
    gene_sequence: set[Gene]
    
#@dataclass
#class Genome:
#    gene_sequence: tuple[Gene]
#    connections: set[tuple[Gene, Gene]] = field(default_factory=set)
#
#    def make_random_connections(self, max_connections: int) -> None: [self.connections.add((Gene(random.choice(self.gene_sequence), Gene.random_weight()), Gene(random.choice(self.gene_sequence), Gene.random_weight()))) for _ in range(max_connections)] 
#    def remove_invalid_connections(self) -> None: [self.connections.remove((a, b)) for (a, b) in tuple(self.connections) if (a.source == b.source or not self.valid_pair(a.source, b.source))]
#    def build(self) -> None: self.make_random_connections(self.no_connections); self.remove_invalid_connections()
#    @staticmethod
#    def valid_pair(a: Gene, b: Gene) -> bool: return isinstance(a, Sensors) and isinstance(b, Actions)
#

@dataclass
class GenomeGenorator:
    no_neurons: int
    no_connections: int
    neurons: tuple[Neuron] = field(default_factory=tuple)
    genome: set[Gene] = field(default_factory=tuple)

    def build(no_neurons: int, no_connections: int) -> Genome:
        n = (Neuron(i, random.choice((*list(Sensors), *list(Actions), list(Internal)))) for i in range(no_neurons))
        g = (Gene(random.choice(n), random.choice(n), Gene.random_weight()) for _ in range(no_connections))

    def _remove_invalid_connections(self) -> None: pass
    @staticmethod
    def _valid_gene(self, gene: Gene) -> bool: pass

@dataclass
class NeuralNetwork:
    pass

@dataclass
class Perceptron:
    inputs: Genome

if __name__ == "__main__":
    g = Genome(tuple(random.choices((*list(Sensors), *list(Actions), *list(Internal)), k=30)))
    g.make_random_connections(1000)
    g.remove_invalid_connections()
    print(g.connections)