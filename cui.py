import sys

class CUI:
	def getPawn(self,chr):
		pawn = ""
		if (chr=="K" or chr=="k"):
			pawn = "K"
			pawn = "B"+pawn if ord(chr)>96 else "W"+pawn
		elif (chr=="Q" or chr=="q"):
			pawn = "Q"
			pawn = "B"+pawn if ord(chr)>96 else "W"+pawn
		elif (chr=="B" or chr=="b"):
			pawn = "B"
			pawn = "B"+pawn if ord(chr)>96 else "W"+pawn
		elif (chr=="N" or chr=="n"):
			pawn = "N"
			pawn = "B"+pawn if ord(chr)>96 else "W"+pawn
		elif (chr=="R" or chr=="r"):
			pawn = "R"
			pawn = "B"+pawn if ord(chr)>96 else "W"+pawn
		else:
			pawn = "__"

		return pawn

	def printBoard(self,board):
		fullboard = ""
		for row in reversed(board):
			#print row
			strow = "| "
			for pawn in row:
				strow += self.getPawn(pawn)+" | "
			print strow
		print ""