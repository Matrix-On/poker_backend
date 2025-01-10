import enum

class GameOperationsEnum(enum.Enum):
    start = 1
    end = 2
    pause = 3
    unpause = 4
    next_level = 5
    time_break = 6

class HeroOpertaionsEnum(enum.Enum):
    rebuy = 1
    end_game = 2
