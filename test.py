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

def main():
    while (a := random.randint(1, 20)) != 20:
        print(a)
        print("I am not 20")
    print(f"{a}! I am 20")

if __name__ == "__main__":
    main()