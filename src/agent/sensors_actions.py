from enum import Enum, auto

# -----------------------------------
# POTENTIAL SENSORS / ACTIONS
#
# SENSORS
# - AGENTS FORWARD VECTOR

class Sensors(Enum):
    LOC_X = auto()
    LOC_Y = auto()
    BOUNDARY_DIST_X = auto()
    BOUNDARY_DIST_Y = auto()
    BOUNDARY_DIST = auto()
    LAST_MOVE_DIR_X = auto()
    LAST_MOVE_DIR_Y = auto()
    POP_FORWARD = auto()        # POPULATION FORWARD -> DO WE NEED THIS
    BAR_FORWARD = auto()        # BARRIER FORWARD -> DO WE NEED THIS
    ENERGY = auto()
    HUNGER = auto()
    SLEEP = auto()
    PLAY = auto()
    AGE = auto()
    POPULATION = auto()         # POPULATION DENSITY IN NEIGHBOURHOOD
    POPULATION_FB = auto()      # POPULATION DENSITY IN FORWARD / BACKWARD AXIS
    POPULATION_LR = auto()      # POPULATION DENSITY IN LEFT / RIGHT AXIS     

class Actions(Enum):
    MOVE_X = auto()
    MOVE_Y = auto()
    MOVE_FORWARD = auto()
    MOVE_BACKWARD = auto()
    ROTATE_LEFT = auto()
    ROTATE_RIGHT = auto()
    EAT = auto()
    SLEEP = auto()
    WORK = auto()
    PLAY = auto()

class Internal(Enum):
    INTERNAL = auto()