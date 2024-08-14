from enum import Enum, auto

"""
POTENTIAL SENSORS / MOTOR NEURONS

SENSORS
- AGENT FORWARD VECTOR
- OBJECT AHEAD BOOL 
- OBJECT AHEAD SYMBOL           # IF SYMBOL OF OBJECT DOES NOT EXIST IN GENOME, BUILD IT UP TO SOME NEURON CAP
"""  

class Sensors(Enum):
    LOC_X = auto()
    LOC_Y = auto()
    BOUNDARY_DIST_X = auto()
    BOUNDARY_DIST_Y = auto()
    BOUNDARY_DIST = auto()
    LAST_MOVE_DIR_X = auto()
    LAST_MOVE_DIR_Y = auto()
    POP_FORWARD = auto()        
    BAR_FORWARD = auto()        
    TIME_OF_DAY = auto()
    ENERGY = auto()
    HUNGER = auto()
    SLEEP = auto()
    PLAY = auto()
    AGE = auto()
    POPULATION = auto()         # POPULATION DENSITY IN NEIGHBOURHOOD
    POPULATION_FB = auto()      # POPULATION DENSITY IN FORWARD / BACKWARD AXIS
    POPULATION_LR = auto()      # POPULATION DENSITY IN LEFT / RIGHT AXIS    

class MN(Enum):                 # MOTOR NEURONS
    MOVE_FORWARD = auto()
    MOVE_BACKWARD = auto()
    ROTATE_LEFT = auto()
    ROTATE_RIGHT = auto()
    EAT = auto()                # EAT, SLEEP, WORK AND PLAY WILL BE REPLACED IN BETA
    SLEEP = auto()              # FOR MORE GENERALISED ACTIONS -> INTERACT
    WORK = auto()
    PLAY = auto()

class Internal(Enum):   
    INTERNAL = auto()           # INTERNAL NEURONS NEED REFACTORS TO SUPPORT REWRITES FOR SYMBOL EMBEDDING