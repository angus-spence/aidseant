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
    tiles: dict[int: Tile] = Field(default_factory=dict)
    is_built: bool = False
    
    def __post_init__(self) -> None:
        if not self._check_inputs(): raise ValueError(f"Property overload: sum of inputs greater than size of world ({self.no_commercials + self.no_employments + self.no_residences + self.population} / {self.size[0] * self.size[1]})")

    def _check_inputs(self) -> bool: return True if self.no_commercials + self.no_employments + self.no_residences + self.population < self.size[0] * self.size[1] else False

    def build(self, seed: int) -> World:
        residents, employments, commercials, agents = self._build_residences(), self._build_employments(), self._build_commercials(), self._build_agents()
        world = World(size=self.size)
        self.is_built = True
    
    def _is_ocuppied(self, location: Location) -> bool:
        return location in self.tiles

    def _return_empty_tiles(self) -> list:
        return [tile for tile in list(self.tiles.values()) if tile._is_vacant()]

    def _build_residences(self) -> list[Residence]: 
        for i in range(self.no_residences):
            loc = (random.randint(0, self.size[0]), random.randint(0, self.size[0]))
            residents = [Residence(id=i, location=Location(id=i, x=random.randint(), y=0), capacity=1) for i in range(self.no_residences)]
        
        return [Residence(id=i, location=Location(id=i, x=random.randint(), y=0), capacity=1) for i in range(self.no_residences)]

    def _build_employments(self) -> list[Employment]:
        pass

    def _build_commercials(self) -> list[Commercial]:
        pass

    def _build_agents(self) -> list[Agent]:
        pass