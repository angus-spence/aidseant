from agent.neurons import Sensors, Actions, Internal

from typing import Self
from dataclasses import dataclass, field
import struct
import random

from viznet import NodeBrush, DynamicShow, EdgeBrush

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
    def random_weight() -> float: return random.randint(0, 1000) / 1000
    @property
    def source_type(self) -> bool: return 1 if isinstance(self.source.classification, Sensors) else 0 if isinstance(self.source.classification, Actions) else 2
    @property
    def destination_type(self) -> bool: return 1 if isinstance(self.destination, Sensors) else 0 if isinstance(self.destination.classification, Actions) else 2
    @staticmethod
    def hex_encode(w: float, source: Neuron, destination: Neuron) -> str: return hex(int(round(w, 5)*1e10+source.id*1e6+source.classification.value*1e4+destination.id*1e2+destination.classification.value))
    @staticmethod
    def hex_decode(x: str) -> tuple[float, Neuron, Neuron]: return (x[:3], Neuron(x[4]))
    @property
    def hex(self) -> str: return self.hex_encode(self.w, self.source, self.destination)
    @property
    def byte(self) -> bytes: return struct.pack('iiiii', self.source_type, self.destination_type, self.source.classification.value, self.destination.classification.value, int(round(self.w, 3)*1e4))

@dataclass
class Genome:
    gene_sequence: set[Gene]

    @property
    def serial(self) -> str: return ''.join(gene.hex + '|' for gene in self.gene_sequence).removesuffix('|')
    def plot(self) -> None:
        with DynamicShow((5, 5), f'Agent Neural Network.png'):
            for gene in self.gene_sequence:
                brush_s = NodeBrush('nn.input' if isinstance(gene.source.classification, Sensors) else 'nn.recurrent', size='normal')
                source = brush_s >> (gene.source.id, 5 if isinstance(gene.source.classification, Sensors) else 0)
                brush_d = NodeBrush('nn.output' if isinstance(gene.destination.classification, Actions) else 'nn.recurrent', size='normal')
                destination = brush_d >> (gene.destination.id, -5 if isinstance(gene.destination.classification, Actions) else 0)
                edge = EdgeBrush('->-', lw=gene.w)
                edge >> (source, destination)
                source.text(gene.source.classification, 'top', text_offset=0.5, fontsize=6, rotation=45)
                destination.text(gene.destination.classification, 'bottom', text_offset=0.5, fontsize=6, rotation=45)

@dataclass
class GenomeGenerator:
    no_neurons: int
    no_internal_neurons: int
    genome_length: int
    
    neurons: list[Neuron] = field(default_factory=list)
    genome: set[Gene] = field(default_factory=set)

    def build(self) -> Genome:
        for i in range(self.no_neurons): self.neurons.append(Neuron(i, random.choice((*list(Sensors), *list(Actions)))))
        for i in range(self.no_internal_neurons): self.neurons.append(Neuron(int(i*(self.no_neurons/self.no_internal_neurons)), Internal.INTERNAL))
        for _ in range(self.genome_length): self.genome.add(Gene(random.choice(self.neurons), random.choice(self.neurons), Gene.random_weight()))
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
    g = GenomeGenerator(80, 20, 120)
    g1 = g.build()
    a = list(g1.gene_sequence)
    print(g1.serial)