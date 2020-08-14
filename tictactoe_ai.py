from random import randint
import random

board=["" for x in range(10)]

def display():
	for i in range(3):
		for j in range(3):
			print(board[i*3+j],end="  | ")
		print("\n-------------")

def win_chk(brd,player):
	combn=[
			[0,1,2],
			[3,4,5],
			[6,7,8],
			[0,4,8],
			[0,3,6],
			[1,4,7],
			[2,5,8],
			[2,4,6]
			]
	for match in combn:
		if brd[match[0]]==brd[match[1]]==brd[match[2]]==player:
			return True
	return False

def entry(player,pos):
	print("player is=",player)
	if board[pos]!="":
		board[pos]==player

def f_turn():
	t=randint(0,1)
	if t==1:return "X"
	return "O"



def pc_move():
	move=0
	possible=[x for x,y in enumerate(board) if y==""]
	for plr in ["O","X"]:
		for pos in possible:
			copy=board[:]
			copy[pos]=plr
			if win_chk(copy,plr):
				move=pos
				return move
	
	corners=[x for x in possible if x in [0,2,6,8]]
	if len(corners)>0:
		return random.choice(corners)	
	if 4 in possible:
		return 4
	edges=[x for x in possible if x in [1,3,5,7]]
	if len(edges)>0:
		return random.choice(edges)

def main():
	print("Player: X \n PC: O")
	turn=f_turn()
	print("player",turn,"turn first")
	moves=0
	while moves<=8:
		display()
		print("it's",turn, "turn")
		if turn=="X":
			pos=int(input("Enter position(1-9)"))-1
			while pos>9 or board[pos]=="O" or board[pos]=="X" :
				print("Invalid input")
				pos=int(input("Enter position"))-1
		else:
			pos=pc_move()
		board[pos]=turn
		if win_chk(board,turn):
			display()
			print(turn,"is the winner")
			return
		turn="O" if turn=="X" else "X"
		moves+=1
	display()
	print("It's Draw")	
		
main()