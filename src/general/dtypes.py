from world.world import Residence

from dataclasses import dataclass

@dataclass
class Location:
    id: int
    x: int
    y: int

@dataclass
class AgentGenome:
    id: int
    genome: str

@dataclass
class Agent:
    id: int
    age: int
    genome: AgentGenome
    residence: Residence