from general.dtypes import Agent

from dataclasses import dataclass
from enum import Enum, auto
from typing import Self

class structures(Enum):
    RESIDENCE = auto()
    EMPLOYMENT = auto()
    COMMERCIAL = auto()

@dataclass(repr=False)
class Location:
    x: int
    y: int

    def __post_init__(self) -> None: self.full = (self.x, self.y)
    def __hash__(self) -> int: return hash((self.x, self.y))
    def __repr__(self) -> str: return f'(x={self.x}, y={self.y})'
    def __eq__(self, value: Self) -> bool: return True if value.x == self.x and value.y == self.y else False
    def __ne__(self, value: Self) -> bool: return True if not self.__eq__(value) else False

@dataclass(frozen=True)
class Residence:
    id: int
    location: Location
    density: int

    def serial(self) -> int: return structures.RESIDENCE.value

@dataclass(frozen=True)
class Employment:
    id: int
    location: Location
    density: int

    def serial(self) -> int: return structures.EMPLOYMENT.value

@dataclass(frozen=True)
class Commercial:
    id: int
    location: Location
    density: int

    def serial(self) -> int: return structures.COMMERCIAL.value

@dataclass
class Tile:
    location: Location
    tenant: Residence | Employment | Commercial | Agent | None

    def __post_init__(self) -> None: raise TypeError(f"invalid tenant {type(self.tenant)}") if not self._valid_tenant() else None
    def _is_vacant(self) -> bool: return False if self.tenant is not None else True
    def _valid_tenant(self) -> bool: return any([isinstance(self.tenant, valids) for valids in [Residence, Employment, Commercial, Agent]])

@dataclass(frozen=True)
class World:
    size: tuple
    tiles: dict[int, Tile]
    agents: list[Agent]
    residences: list[Residence]
    employments: list[Employment]
    commercials: list[Commercial]