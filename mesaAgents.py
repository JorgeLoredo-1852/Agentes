from random import random
from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import SimultaneousActivation
from mesa.datacollection import DataCollector
import numpy as np

with open('movement.txt', 'w') as f:
    f.write("")
with open('boxes.txt', 'w') as f:
    f.write("")

class Robot(Agent):
    
    def __init__(self, unique_id, model, direction=None):
        super().__init__(unique_id, model)
        self.stepX = 0
        self.stepY = 0
        self.validDirections = ['right', 'down', 'left', 'up']
        self.currDirection = 'right'
        self.binded_box = None
        self.target = None
        self.hasBox = False
        self.next_pos = None
        self.pos = model.grid.find_empty()
        
    @property
    def direction(self):
        return self.currDirection
    
    @direction.setter
    def direction(self, newDirection):
        self.currDirection = newDirection
        if self.currDirection == 'up':
            self.stepX = -1 
            self.stepY = 0
            return
        elif self.currDirection == 'down':
            self.stepX = 1
            self.stepY = 0
            return
        elif self.currDirection == 'right':
            self.stepX = 0
            self.stepY = 1
            return
        elif self.currDirection == 'left':
            self.stepX = 0
            self.stepY = -1
            return
        
    def move(self):

        if self.target:
            if self.hasBox:
                if self.target.full:
                    self.target = None
                    return
            if self.pos[0] < self.target.pos[0]:
                self.direction = "down"
                return
            elif self.pos[0] > self.target.pos[0]:
                self.direction = "up"
                return
            elif self.pos[1] < self.target.pos[1]:
                self.direction = "right"
                return
            elif self.pos[1] > self.target.pos[1]:
                self.direction = "left"
                return
            
            # TAKE BOX
            if not self.hasBox:
                self.target.binded = True
                self.hasBox = True
                self.binded_box = self.target
                self.target = None
                return

            # DROP BOX
            else:
                self.binded_box.delivered = True
                self.binded_box = None
                self.hasBox = False
                self.target.quantity += 1
                self.target = None
                self.direction = "left"

        for agent in self.model.schedule.agents:
            if self.hasBox:
                if isinstance(agent, Pila):
                    if agent.full:
                        continue
                    self.target = agent
                    return
            else:
                if isinstance(agent, Box) and not agent.targeted and not agent.binded and not agent.delivered:
                    self.target = agent
                    agent.targeted = True
                    return
        
    def advance(self):
        if self.binded_box:
            self.model.grid.move_agent(self.binded_box, self.next_pos)
        self.model.grid.move_agent(self, self.next_pos)
            
    def step(self):
        self.move()
        next_pos = (self.pos[0] + self.stepX, self.pos[1] + self.stepY)
        while (self.model.grid.out_of_bounds(next_pos)):
            self.direction = self.random.choice(self.validDirections)
            next_pos = (self.pos[0] + self.stepX, self.pos[1] + self.stepY)
        self.next_pos = next_pos
        nextCoordinate = str(self.pos[0] + self.stepX) + "," + str(self.pos[1] + self.stepY) + "," + str(self.unique_id) + "," + str(self.hasBox) + ","
        with open('movement.txt', 'a') as f:
            f.write(nextCoordinate)
            f.write('\n')

class Pila(Agent):
    def __init__(self, unique_id, model, pos = None):
        super().__init__(unique_id, model)
        self.pos = pos if pos else self.random.choice(self.model.grid.coord_iter())
        self.full = False
        self._quantity = 0
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity
        if self._quantity == 5:
            self.full = True
        else:
            self.full = False
            
    def step(self):
        pass

class Box(Agent):
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.pos = self.model.grid.find_empty()
        self.binded = False
        self.delivered = False
        self.targeted = False
        self.model.grid.place_agent(self, (self.pos))
        
    def step(self):
        nextCordinate = str(self.pos[0]) + "," + str(self.pos[1]) + "," + str(self.binded) + ","
        with open('boxes.txt', 'a') as f:
            f.write(nextCordinate)
            f.write('\n')
        pass
    
    def hasDelivered(self):
        return self.delivered

def get_matrix(model):
    grid = np.zeros((model.grid.width, model.grid.height))
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell        
        for agent in cell_content:
            if isinstance(agent, Box):
                grid[x][y] = 1
                continue
            if isinstance(agent, Pila):
                if agent.quantity == 0: grid[x][y] = 2
                elif agent.quantity == 1: grid[x][y] = 3
                elif agent.quantity == 2: grid[x][y] = 4
                elif agent.quantity == 3: grid[x][y] = 5
                elif agent.quantity == 4: grid[x][y] = 6
                elif agent.quantity == 5: grid[x][y] = 7
                break

        for agent in cell_content:
            if isinstance(agent, Robot):
                if agent.hasBox: grid[x][y] = 8
                else: grid[x][y] = 9
                break
    return grid

class Almacen(Model):
    def __init__(self, nRobots, nBoxes, width, height):
        self.grid = MultiGrid(width, height, torus = False)
        self.schedule = SimultaneousActivation(self)
        self.width = width
        self.height = height
        self.nRobots = nRobots
        self.nBoxes = nBoxes
        self.createAgents()
        self.datacollector = DataCollector(model_reporters = {"Grid": get_matrix})
        
    def createAgents(self):
        for i in range(0, self.width):
            pila = Pila((i, 0), self, (i, 0))
            self.schedule.add(pila)
            self.grid.place_agent(pila,(i,0))
            
        for i in range(self.nRobots,self.nRobots+self.nBoxes):
            caja = Box(i, self)
            self.grid.place_agent(caja, caja.pos)
            self.schedule.add(caja)
            
        for i in range(self.nRobots):
            robot = Robot(i, self)
            self.grid.place_agent(robot, robot.pos)
            self.schedule.add(robot)
            
    def allClean(self):
        for (content, x, y) in self.grid.coord_iter():
            for obj in content:
                if isinstance(obj, Box) and obj.hasDelivered() == False:
                    return False
        return True
    
    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

almacen = Almacen(5,15, 20, 20)
totalSteps = 0
while not almacen.allClean():
    totalSteps=totalSteps + 1
    almacen.step()
print(totalSteps)