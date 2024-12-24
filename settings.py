from ShekelFoxholeFunction import ShekelFoxholeFunction
from entity.TargetFunction import TargetFunction

class Settings:
    popSize = 20
    phi_g = .2
    phi_p = .2
    def __init__(self):
        self.targetFunctionArea = (-5, 5), (-5, 5)
        self.popSize = Settings.popSize
        self.targetFunction: TargetFunction = ShekelFoxholeFunction()
        self.epochCount = 6

        self.phi_g = Settings.phi_g
        self.phi_p = Settings.phi_p

        self.omega_max = 2
        self.omega_min = 0.2

        self.alpha = 0.9
