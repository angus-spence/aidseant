from world.dtypes import Location
from typing import overload, Optional, Union

def loc2tuple(loc: Location) -> tuple[int, int]: return (loc.x, loc.y)
