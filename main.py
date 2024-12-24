from settings import Settings
from entity.Population import Population
import numpy as np
import matplotlib.pyplot as plt

class Algorithm(Settings):
    def __init__(self):
        super().__init__()
        self.population = Population()
        self.population.updateVel()
    
    def __runEpoch(self):
        self.population.updateVel()
        self.population.move()
    

            
    
    def run(self):
        epochValues = list(range(1, 50, 1))
        dataListByM = {4: [], 16: [], 32: [], 64: []}
        for M in dataListByM.keys():
            Settings.M = M
            self.__init__()

            for _ in epochValues:
                dataListByM[M].append(self.targetFunction.getValue(self.population.getBest().point))
                self.__runEpoch()

            plt.plot(epochValues, dataListByM[M], label=f"M={M}")

        plt.legend()
        plt.grid()
        plt.show()

        # self.__draw()
        # for _ in range(self.epochCount//2): self.__runEpoch()
        # self.__draw()
        # for _ in range(self.epochCount//2): self.__runEpoch()
        # self.__draw()
        # plt.show()
    
    def __draw(self):
        plt.figure(figsize=(5, 5))

        xRange, yRange = self.targetFunctionArea
        x = np.linspace(*xRange, int((xRange[1]-xRange[0])/0.1))
        y = np.linspace(*yRange, int((yRange[1]-yRange[0])/0.1))
        x, y = np.meshgrid(x, y)

        # Вычисляем значения z для каждой точки сетки
        z = np.array([[self.targetFunction.getValue((xi, yi)) for xi, yi in zip(x_row, y_row)] for x_row, y_row in zip(x, y)])

        cont = plt.contour(x, y, z, levels=30, cmap='viridis')
        plt.clabel(cont)

        px = [agent.point[0] for agent in self.population]
        py = [agent.point[1] for agent in self.population]
        plt.scatter(px, py, color='blue', label='Initial Population', s=20)

        for agent in self.population:
            pointTo = agent.point+agent.vel
            plt.plot(
                [agent.point[0], pointTo[0]], 
                [agent.point[1], pointTo[1]],
                color="red", linewidth=0.5
            )

        plt.grid()



if __name__=="__main__":
    Algorithm().run()
