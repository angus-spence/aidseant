from general_dtypes import Location, Agent

import random
from dataclasses import dataclass, Field

@dataclass(frozen=True)
class Residence:
    id: int
    location: Location
    capacity: int

@dataclass(frozen=True)
class Employment:
    id: int
    location: Location
    capacity: int

@dataclass(frozen=True)
class Commercial:
    id: int
    location: Location

@dataclass(frozen=True)
class World:
    size: tuple
    agents: list = Field(default_factory=list)
    residences: list[Residence] = Field(default_factory=list)
    employments: list[Employment] = Field(default_factory=list)
    commercials: list[Commercial] = Field(default_factory=list)

@dataclass
class Tile:
    location: Location
    tenant: Residence | Employment | Commercial | Agent | None

    def _is_vacant(self) -> bool: return False if self.tenant is not None else True
    def _valid_tenant(self) -> bool: return any([isinstance(self.tenant, regulated) for regulated in [Residence, Employment, Commercial, Agent]])

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