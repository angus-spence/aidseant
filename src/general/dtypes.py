

from dataclasses import dataclass

class Oscilator:
    def init(self) -> None: pass 

@dataclass
class AgentGenome:
    id: int
    genome: str

