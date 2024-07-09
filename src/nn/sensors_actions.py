from enum import Enum

class MovementSensors(Enum):
    LOC_X = 0
    LOC_Y = 1
    BOUNDARY_DIST_X = 2
    BOUNDARY_DIST_Y = 3
    BOUNDARY_DIST = 4
    LAST_MOVE_DIR_X = 5
    LAST_MOVE_DIR_Y = 6
    POP_FORWARD = 7         # POPULATION FORWARD
    BAR_FORWARD = 8         # BARRIER FORWARD

class SelfSensors(Enum):
    ENERGY = 0
    HUNGER = 1
    SLEEP = 2
    WORK = 3

class Actions(Enum):
    MOVE_X = 0
    MOVE_Y = 1
    MOVE_FORWARD = 2
    MOVE_BACKWARD = 3
    ROTATE_LEFT = 4
    ROTATE_RIGHT = 5
    EAT = 6
    SLEEP = 7
    WORK = 8    