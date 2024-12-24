from entity.Agent import Agent
from settings import Settings

class Population(Settings):
    def __init__(self):
        super().__init__()
        self.agents: list[Agent] = [Agent() for _ in range(self.popSize)]

    def __iter__(self):
        return iter(self.agents)
    
    def __getitem__(self, key) -> Agent:
        return self.agents[key]
    
    def move(self):
        for agent in self.agents: agent.move()

    def updateVel(self):
        G = max(self.agents, key=lambda agent: agent.fitness).point
        for agent in self.agents: agent.updateVel(G)
    
    def getAvgByX(self):
        avgX = sum([agent.point[0] for agent in self.agents])/self.popSize
        return min(self.agents, key=lambda agent: abs(agent.point[0] - avgX))
    
    def getAvgByY(self):
        avgX = sum([agent.point[1] for agent in self.agents])/self.popSize
        return min(self.agents, key=lambda agent: abs(agent.point[1] - avgX))
    
    def getBest(self):
        return max(self.agents, key=lambda x: x.fitness)