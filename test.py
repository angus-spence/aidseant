from dataclasses import dataclass
from typing import Generator
import contextlib
import random
import time

@contextlib.contextmanager
def timing(fnc_name: str) -> Generator[None, None, None]:
    t0 = time.monotonic()
    print(f'LOG: STARTING PROCESS {fnc_name}')
    try: yield
    finally: print(f' ---> {fnc_name} TOOK {round(time.monotonic() - t0, 4)} SECONDS')

NO_TILES = int(1e6)

@dataclass(frozen=True)
class Residence:
    id: int
    capacity: int

@dataclass(frozen=True)
class Employment:
    id: int
    capacity: int

@dataclass(frozen=True)
class Commercial:
    id: int
    capacity: int

@dataclass
class Tile:
    location: tuple[int, int]
    tenant: Residence | Employment | Commercial | None

    def _is_vacant(self) -> bool: return False if self.tenant is False else True

@timing("tile_scout")
def scout_tiles(tiles: list[Tile]) -> list:
    return [tile.location for tile in tiles if tile._is_vacant()]

if __name__ == "__main__":
    tiles = [Tile(location=(random.randint(0, 500), random.randint(0, 500)), tenant=(random.choice([Residence, Employment, Commercial, None]))) for _ in range(NO_TILES)]
    scout_tiles(tiles)