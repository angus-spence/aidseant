from general.dtypes import Agent

import random
from dataclasses import dataclass, field
from enum import Enum

class structures(Enum):
    RESIDENCE = 1
    EMPLOYMENT = 2
    COMMERCIAL = 3
@dataclass(frozen=True)
class Location:
    x: int
    y: int

    def __call__(self) -> tuple[int, int]: return (self.x, self.y)
@dataclass(frozen=True)
class Residence:
    id: int
    location: Location
    density: int

@dataclass(frozen=True)
class Employment:
    id: int
    location: Location
    density: int

@dataclass(frozen=True)
class Commercial:
    id: int
    location: Location
    density: int

@dataclass
class Tile:
    location: Location
    tenant: Residence | Employment | Commercial | Agent | None

    def __post_init__(self) -> None: raise TypeError("invalid tenant") if not self._valid_tenant() else None
    def _is_vacant(self) -> bool: return False if self.tenant is not None else True
    def _valid_tenant(self) -> bool: return any([isinstance(self.tenant, regulated) for regulated in [Residence, Employment, Commercial, Agent]])

@dataclass(frozen=True)
class World:
    size: tuple
    tiles: dict[int, Tile]
    agents: list[Agent]
    residences: list[Residence]
    employments: list[Employment]
    commercials: list[Commercial]