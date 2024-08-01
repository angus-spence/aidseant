from general.dtypes import Agent

from dataclasses import dataclass
from enum import Enum, auto
from typing import Self

import matplotlib.pyplot as plt
import numpy as np

class Tenants(Enum):
    VACANT = auto()
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
    @property
    def loc(self) -> tuple[int, int]: return (self.x, self.y)

@dataclass
class Tenant:
    id: int
    tenant: Tenants
    location: Location

    def __hash__(self) -> int: return hash((self.id, self.serial, self.location.loc))

    @property
    def serial(self) -> int: return Tenants[self.tenant.name].value

@dataclass(kw_only=True)
class Residence(Tenant):
    pass

@dataclass(kw_only=True)
class Employment(Tenant):
    pass

@dataclass(kw_only=True)
class Commercial(Tenant):
    pass

@dataclass
class Tile:
    location: Location
    tenant: Tenant

    #ASSUME: __hash__() -> YOU CANNOT HAVE MULTIPLE TENANTS WITH THE SAME TYPE

    def __hash__(self) -> int: return hash((self.location.x, self.location.y, self.tenant.serial))
    def update(self, tenant: Tenant): self.tenant = tenant
    def _is_vacant(self) -> bool: return False if self.tenant is not None else True

@dataclass(frozen=True)
class World:
    size: tuple
    tiles: set[Tile]
    agents: list[Agent]

    def __str__(self) -> None: 
        bmap = np.zeros(self.size)
        for x, y, tennant in [(*tile.location.loc, tile.tenant) for tile in self.tiles]: bmap[x-1, y-1] = tennant.serial
        plt.matshow(bmap, cmap='Paired')
        plt.show()