from world.dtypes import Tenant, Location, Tile, World, Tenants
from agent.dtypes import Agent

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

    @property
    def overflow(self) -> bool: return sum(1 for tile in self.tiles if tile.tenant != Tenants.VACANT) > (self.size[0] * self.size[1])

    def build(self) -> World:
        struct_itr = dict(zip(Tenants, [0, self.no_commercials, self.no_employments, self.no_residences]))
        _id = 0
        for tenant in Tenants:
            if tenant == Tenants.VACANT: continue
            for _ in range(struct_itr[tenant]):
                while (loc := self._rloc_gen()) not in [tile.location.loc for tile in self.tiles]:
                    if len([tile for tile in self.tiles if tile.tenant.tenant == tenant]) >= struct_itr[tenant]: continue
                    self.tiles.add(Tile(Location(*loc), Tenant(_id, tenant)))
                    _id += 1

        return World(size=self.size,
                     tiles=self.tiles,
                     agents=None)

    def _rloc_gen(self) -> tuple[int, int]: return (random.randint(0, self.size[0]), random.randint(0, self.size[0]))
    def tile_serialiser(self) -> list[int]: return [tile.tenant.serial for tile in self.tiles]
    def _get_empty(self) -> set[Tile]: return set(tile for tile in self.tiles if tile.tenant==Tenants.VACANT)

if __name__ == "__main__":
    world = WorldGenerator(
        size=(50, 50),
        population=100,
        no_residences=25,
        no_employments=25,
        no_commercials=25
    ).build()
    world.plot()