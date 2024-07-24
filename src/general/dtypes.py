from world.dtypes import Residence

from dataclasses import dataclass

class Oscilator:
    def init(self) -> None: pass 

@dataclass
class AgentGenome:
    id: int
    genome: str

@dataclass
class Agent:
    id: int
    genome: AgentGenome
    osc: Oscilator
    age: int
    residence: Residence