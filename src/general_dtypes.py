from dataclasses import dataclass

@dataclass
class Location:
    id: int
    x: int
    y: int

@dataclass
class Residence:
    id: int
    location: Location

@dataclass
class Employment:
    id: int
    location: Location

@dataclass
class Commercial:
    id: int
    location: Location

@dataclass
class AgentGenome:
    id: int
    genome: str

@dataclass
class Agent:
    id: int
    age: int
    genome: AgentGenome