import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player
from gameboard import *



def main():
	board = GameBoard(700,20) #boardsize, fps
	board.startScreen()
	while True:
		if board.run() == False:
			break
		board.fpsClock.tick(board.Framepersecond) #limits how fast the screen can updat by framepersecond

		

main()