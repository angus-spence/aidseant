from general.dtypes import Agent

import random
from dataclasses import dataclass, Field

@dataclass(repr=False, frozen=True)
class Location:
    x: int
    y: int

    def __repr__(self) -> tuple[int, int]: return (self.x, self.y)

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
    agents: list = Field(default_factory=list)
    residences: list[Residence] = Field(default_factory=list)
    employments: list[Employment] = Field(default_factory=list)
    commercials: list[Commercial] = Field(default_factory=list)