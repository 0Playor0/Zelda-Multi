import pygame,sys
from settings import *
from level import Level
from network import Network
#import random
#from enum import Enum
#from collections import namedtuple
#import numpy as np

#class Moves(Enum):
#    RIGHT = 1
#    LEFT = 2
#    UP = 3
#    DOWN = 4
#    ATK = 5
#    MAGIC = 6
#    SWITCH_ATK = 7
#    SWITCH_MAGIC = 8

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda - AI')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)

	def read_pos(self,str):
		str = str.split(",")
		return int(str[0]), int(str[1])
	
	def run(self):
		n = Network()
		start_Pos = self.read_pos(n.getPos())
		while True:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run(n)
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()