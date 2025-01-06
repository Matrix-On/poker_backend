import enum

class GameOperations(str, enum.Enum):
    start = "Start"
    end = "End"
    pause = "Pause"
    next_level = "Next level"
    time_break = "Time break"
