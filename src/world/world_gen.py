from world.dtypes import Residence, Commercial, Employment, Location, Tile, World
from general.dtypes import Agent

from dataclasses import dataclass, field
import random

@dataclass	
class WorldGenerator:
    size: tuple
    population: int
    no_residences: int
    no_employments: int
    no_commercials: int
    tiles: set[Tile] = field(default_factory=set)
    is_built: bool = False
    
    def __post_init__(self) -> None:
        if not self._check_inputs(): raise ValueError(f"Property overload: sum of inputs greater than size of world ({self.no_commercials + self.no_employments + self.no_residences + self.population} / {self.size[0] * self.size[1]})")

    def _check_inputs(self) -> bool: return True if self.no_commercials + self.no_employments + self.no_residences + self.population < self.size[0] * self.size[1] else False

    def build(self) -> World:
        for struct in [Residence, Employment, Commercial]: self._build_structures(struct)
        self.is_built = True

    def _build_structures(self, structure: Residence |  Employment | Commercial, *args):
        for i in range(self.no_residences):
            while (loc := self._rloc_gen()) not in [tile.location() for tile in self.tiles]:
                self.tiles.add(structure(i, Location(*loc), random.randint(1, 5)))

    def _partition_structures(self):
        raise NotImplementedError

    def _build_agents(self) -> list[Agent]:
        pass

    def _rloc_gen(self) -> tuple[int, int]: return (random.randint(0, self.size[0]), random.randint(0, self.size[0]))

if __name__ == "__main__":
    gen = WorldGenerator(
        size=(200, 200),
        population=100,
        no_residences=100,
        no_employments=0,
        no_commercials=0
    )
    gen.build()
    print(gen.tiles)