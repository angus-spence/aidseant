from general.dtypes import Agent

from dataclasses import dataclass
from enum import Enum, auto
from typing import Self

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

class Tenants(Enum):
    VACANT = auto()
    RESIDENCE = auto()
    EMPLOYMENT = auto()
    COMMERCIAL = auto()

TenantCMAP = {
    Tenants.VACANT:     (240/255,   240/255,    240/255,    240/255),
    Tenants.RESIDENCE:  (48/255,    227/255,    116/255,    255/255),
    Tenants.COMMERCIAL: (15/255,    235/255,    255/255,    255/255),
    Tenants.EMPLOYMENT: (255/255,   219/255,    15/255,     255/255)
}

@dataclass(repr=False)
class Location:
    x: int
    y: int

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

    def __hash__(self) -> int: return hash((self.id, self.serial))

    @property
    def serial(self) -> int: return Tenants[self.tenant.name].value

@dataclass(kw_only=True)
class Residence(Tenant):
    C: tuple = (48, 227, 116)
    pass

@dataclass(kw_only=True)
class Employment(Tenant):
    C: tuple = (255, 219, 15)
    pass

@dataclass(kw_only=True)
class Commercial(Tenant):
    C: tuple = (80, 199, 193) 
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

    def plot(self) -> None: 
        tenant_map = np.zeros(self.size)
        for x, y, tennant in [(*tile.location.loc, tile.tenant) for tile in self.tiles]: tenant_map[x-1, y-1] = tennant.serial
        cmap = ListedColormap(list(TenantCMAP.values()))
        plt.matshow(tenant_map, cmap='Paired')
        plt.show()