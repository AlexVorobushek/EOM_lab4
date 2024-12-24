from settings import Settings
import random
import numpy as np

class Agent(Settings):
    def __init__(self) -> None:
        super().__init__()
        self.point = np.array([random.randint(self.targetFunctionArea[0][0], self.targetFunctionArea[0][1]-1)+random.random(),
                      random.randint(self.targetFunctionArea[1][0], self.targetFunctionArea[1][1]-1)])+random.random()
        self.vel = np.array([0., 0.])
        self.fitness = self.targetFunction.getPointFitness(self.point)
        self.omega = self.omega_max

        self.P = self.point  # координаты лучшего найденного решения этого агента
    
    def updateVel(self, G):
        self.omega -= (self.omega_max-self.omega_min)/self.epochCount
        K = 2*self.alpha/(self.phi_g+self.phi_p-2)
        self.vel =  self.vel*self.omega + \
                    self.phi_p*random.random()*(self.P - self.point) + \
                    self.phi_g*random.random()*(     G - self.point)
        self.vel *= K
    
    def move(self):
        self.point += self.vel
        if self.targetFunction.getPointFitness(self.point) > self.fitness: self.P = self.point
        self.point[0] = max(min(self.point[0], self.targetFunctionArea[0][1]), self.targetFunctionArea[0][0])
        self.point[1] = max(min(self.point[1], self.targetFunctionArea[1][1]), self.targetFunctionArea[1][0])

        self.fitness = self.targetFunction.getPointFitness(self.point)

        