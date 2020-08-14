from random import randint

#board=["0","0","1","0","0","0","","",""]

board=["1","2","3","4","5","6","7","8","9"]

def display():
	for i in range(3):
		for j in range(3):
			print(board[i*3+j],end="  | ")
		print("\n-------------")

def win_chk(player):
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
		if board[match[0]]==board[match[1]]==board[match[2]]==player:
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

def move(turn,pos):
	board[pos]=turn


def main():
	turn=f_turn()
	print("player",turn,"turn first")
	moves=0
	while moves<=9:
		display()
		print("it's",turn, "turn")
		pos=int(input("Enter position(0-8)"))-1
		while pos>9 or board[pos]=="O" or board[pos]=="X" :
			print("Invalid input")
			pos=int(input("Enter position"))-1
		move(turn,pos)
		if win_chk(turn):
			display()
			print(turn,"is the winner")
			return
		turn="O" if turn=="X" else "X"
		moves+=1

	print("It's Draw")	
		

main()


