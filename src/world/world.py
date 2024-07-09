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
    object: Residence | Employment | Commercial

@dataclass	
class WorldGenerator:
    size: tuple
    population: int
    no_residences: int
    no_employments: int
    no_commercials: int
    objects: dict[int: Tile] = Field(default_factory=dict)
    is_built: bool = False
    
    def build(self, seed: int) -> World:
        residents, employments, commercials, agents = self._build_residences(), self._build_employments(), self._build_commercials(), self._build_agents()
        world = World(size=self.size)
        self.is_built = True
    
    def _is_ocuppied(self, location: Location) -> bool:
        return location in self.objects

    def _build_residences(self) -> list[Residence]: 
        for i in range(self.no_residences):
            loc = 
            residents = [Residence(id=i, location=Location(id=i, x=random.randint(), y=0), capacity=1) for i in range(self.no_residences)]
        
        return [Residence(id=i, location=Location(id=i, x=random.randint(), y=0), capacity=1) for i in range(self.no_residences)]

    def _build_employments(self) -> list[Employment]:
        pass

    def _build_commercials(self) -> list[Commercial]:
        pass

    def _build_agents(self) -> list[Agent]:
        pass