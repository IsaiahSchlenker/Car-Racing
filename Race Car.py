# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:31:04 2024

@author: bluet
"""
import pygame, simpleGE, random
class Game(simpleGE.Sprite):
    def __init__(self):
        super().__init__()
        self.setImage("background-1.png")
        
class Racer(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setimage("TopDownCar.png")
        self.setsize(30,50)
        self.moveSpeed = 10
        self.position = (200,300)
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
class Obstacles(simpleGE.Sprite):
    def __init__():
        super().__init__(self, scene)
        self.setImage("")
        self.setSize(30,50)
        self.minSpeed = 3
        self.maxSpeed = 7
        self.reset()
    def reset(self):
        self.y = 10
        self.x = random.randint(0,)
        self.dy - random.randint(self.minSpeed, self.maxSpeed)
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
def main():
    game = Game()
    game.start
    
if __name__ == "__main__":
    main()