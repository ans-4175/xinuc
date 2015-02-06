import socket
import sys

class Chessboard:
	server_address = ""
	server_port = 80
	server_sock = None
	board = []
	rawBoard = None

	def __init__(self,address,port):
		self.server_address = address
		self.serrver_port = port
		self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_sock.connect((address,port))
		for i in range(0,8):
		    row = []
		    for j in range(0,8):
		        row.append('')
		    self.board.append(row)

	def clearBoard(self):
		for i in range(0,8):
		    row = []
		    for j in range(0,8):
		    	self.board[j][i] = ""

	def getRaw(self):
		data = self.server_sock.recv(1024)
		strdata = data.decode('utf-8')
		strdata = strdata.rstrip("\r\n")
		self.rawBoard = strdata
		coord = strdata.split(" ")
		return coord

	def parseCoord(self,coord):
		self.clearBoard()
		for pawn in coord:
			#print pawn[0]+ord(pawn[0]).__str__()
			col = ord(pawn[1])-97
			row = int(pawn[2])-1
			#print "(%d,%d)" % (col,row)
			self.board[row][col] = pawn[0]