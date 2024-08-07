from agent.neurons import Sensors, Actions, Internal

from typing import Self
from dataclasses import dataclass, field
import struct
import random

from viznet import NodeBrush, DynamicShow, EdgeBrush

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
    classification: Sensors | Actions | Internal
    x: float = 0.0

    def __hash__(self) -> int: return hash(self.byte)
    def __eq__(self, value: Self) -> bool: return True if self.byte == value.byte else False
    @property
    def byte(self) -> bytes: return struct.pack('ii', self.classification_type, self.classification.value)
    @property
    def classification_type(self) -> bool: return 1 if isinstance(self.classification, Sensors) else 0

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
    def source_type(self) -> bool: return 1 if isinstance(self.source.classification, Sensors) else 0
    @property
    def destination_type(self) -> bool: return 1 if isinstance(self.destination, Sensors) else 0
    @property
    def byte(self) -> bytes: return struct.pack('iiii', self.source_type, self.destination_type, self.source.classification.value, self.destination.classification.value)

@dataclass
class Genome:
    gene_sequence: set[Gene]

    def plot(self) -> None:
        with DynamicShow((5, 5), f'Agent Neural Network.png') as d:
            for gene in self.gene_sequence:
                print(f'SOURCE: {gene.source} TYPE: {type(gene.source.classification)} {isinstance(gene.source.classification, Sensors)}')
                print(f'DESTINATION {gene.destination} TYPE: {type(gene.destination.classification)} {isinstance(gene.destination.classification, Actions)}')
                brush_s = NodeBrush('nn.input' if isinstance(gene.source.classification, Sensors) else 'nn.recurrent', size='normal')
                source = brush_s >> (gene.source.classification.value, 5 if isinstance(gene.source.classification, Sensors) else 0)
                brush_d = NodeBrush('nn.output' if isinstance(gene.destination.classification, Actions) else 'nn.recurrent', size='normal')
                destination = brush_d >> (gene.destination.classification.value, -5 if isinstance(gene.destination.classification, Actions) else 0)
                edge = EdgeBrush('->-', lw=gene.w)
                edge >> (source, destination)
                source.text(gene.source.classification, 'top', text_offset=0.5, fontsize=6, rotation=45)
                destination.text(gene.destination.classification, 'bottom', text_offset=0.5, fontsize=6, rotation=45)

@dataclass
class GenomeGenerator:
    no_neurons: int
    no_connections: int
    neurons: list[Neuron] = field(default_factory=list)
    genome: set[Gene] = field(default_factory=set)

    def build(self) -> Genome:
        for i in range(self.no_neurons): self.neurons.append(Neuron(i, random.choice((*list(Sensors), *list(Actions), *list(Internal)))))
        for _ in range(self.no_connections): self.genome.add(Gene(random.choice(self.neurons), random.choice(self.neurons), Gene.random_weight()))
        self._remove_invalid_connections()
        return Genome(self.genome)

    def _remove_invalid_connections(self) -> None: [self.genome.remove(g) for g in list(self.genome) if not GenomeGenerator._valid_gene(g)]
    @staticmethod
    def _valid_gene(gene: Gene) -> bool:
        return (
        (isinstance(gene.source.classification, Sensors) or isinstance(gene.source.classification, Internal)) and
        (isinstance(gene.destination.classification, Actions) or isinstance(gene.destination.classification, Internal))
    )

@dataclass
class NeuralNetwork:
    pass

@dataclass
class Perceptron:
    inputs: Genome

if __name__ == "__main__":
    g = GenomeGenerator(80, 80)
    g1 = g.build()
    g1.plot()
    