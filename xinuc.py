#!/usr/bin/python

import socket
import sys
from chessboard import Chessboard
from cui import CUI

chessboard = Chessboard('xinuc.org', 7387)
cui = CUI()
while 1:
	coord = chessboard.getRaw()
	if (len(coord)==10):
		print chessboard.rawBoard
		chessboard.parseCoord(coord)
		cui.printBoard(chessboard.board)