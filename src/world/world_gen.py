from world.dtypes import Residence, Commercial, Employment, Location, Tile, World, Tenants
from general.dtypes import Agent

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


    # TODO: FIX THIS
    def build(self) -> World:
        for struct_count in self.no_commercials, self.no_employments, self.no_residences:
            while (loc := self._rloc_gen()) not in [tile.location.loc for tile in self.tiles if tile.tenant != Tenants.VACANT]:
                for _ in range(struct_count):
                    self.tiles.add(Tile(Location(*loc), structure(i, Location(*loc), random.randint(1, 5))))

        return World(size=self.size,
                     tiles=self.tiles,
                     agents=None,
                     residences=None,
                     employments=None,
                     commercials=None)

    def _partition_structures(self): raise NotImplementedError
    def _build_agents(self) -> list[Agent]: raise NotImplementedError
    def _rloc_gen(self) -> tuple[int, int]: return (random.randint(0, self.size[0]), random.randint(0, self.size[0]))
    def _get_empty(self) -> set[Tile]: return set(tile for tile in self.tiles if tile.tenant==Tenants.VACANT)
    def tile_serialiser(self) -> list[int]: return [tile.tenant.serial for tile in self.tiles]

if __name__ == "__main__":
    world = WorldGenerator(
        size=(200, 200),
        population=100,
        no_residences=100,
        no_employments=0,
        no_commercials=0
    ).build()

    print(world)