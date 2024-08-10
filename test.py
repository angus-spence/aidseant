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
