from world.dtypes import Residence, Commercial, Employment, Location, Tile, World
from general.dtypes import Agent

from dataclasses import dataclass, Field
import random

@dataclass	
class WorldGenerator:
    size: tuple
    population: int
    no_residences: int
    no_employments: int
    no_commercials: int
    tiles: set[Tile] = Field(default_factory=dict)
    is_built: bool = False
    
    def __post_init__(self) -> None:
        if not self._check_inputs(): raise ValueError(f"Property overload: sum of inputs greater than size of world ({self.no_commercials + self.no_employments + self.no_residences + self.population} / {self.size[0] * self.size[1]})")

    def _check_inputs(self) -> bool: return True if self.no_commercials + self.no_employments + self.no_residences + self.population < self.size[0] * self.size[1] else False

    def build(self) -> World:
        pass



    def _return_empty_tiles(self) -> list:
        return [tile for tile in list(self.tiles.values()) if tile._is_vacant()]

    def _build_residences(self) -> list[Residence]: 
        for i in range(self.no_residences):
            while (loc := self._rloc_gen()) not in [tile.location.__repr__() for tile in self.tiles]:
                self.tiles.add(Residence(i, Location(*loc)))
        
        return [Residence(id=i, location=Location(id=i, x=random.randint(), y=0), capacity=1) for i in range(self.no_residences)]

    def _build_employments(self) -> list[Employment]:
        pass

    def _build_commercials(self) -> list[Commercial]:
        pass

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
    gen._build_residences()
    print(gen.tiles)