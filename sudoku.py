board=[
		[0,0,0,0,0,0,0,0,0],
		[5,0,3,0,6,7,0,0,0],
	   	[9,0,0,3,4,2,1,0,0],
	   	[0,0,0,0,0,4,0,0,0],
	   	[0,0,1,0,0,0,7,2,0],
	   	[0,0,2,0,1,0,0,0,0],
	   	[0,3,0,0,0,0,0,0,9],
	   	[0,8,0,1,0,0,2,0,0],
	   	[0,0,0,7,5,0,8,0,6]
	   	]
def solve(board):
	find=emptychk(board)
	if not find:
		return True
	else:
		row,col= find
	for i in range (1,10):
		if valchk(board,i,(row,col)):
			board[row][col]=i
			if solve(board):
				return True
			board[row][col]=0
	return False
    #global board
def valchk(board,num,pos):
	#check in row
	for i in range(0,9):
		if board[pos[0]][i]==num and pos[1]!=i:
			return False
	#check in column
	for i in range(0,9):
		if board[i][pos[1]]==num and pos[0]!=i:
			return False
	#check in same 3x3 box
	box_x=pos[1]//3*3
	box_y=pos[0]//3*3
	for i in range(box_y,box_y+3):
		for j in range(box_x,box_x+3):
			if board[i][j]==num and (i,j)!=pos:
				return False
	return True
def emptychk(board):
	for i in range(0,9):
		for j in range(0,9):
			if board[i][j]==0:
				return (i,j)
	return False
def printboard(board):
	#global board
	for i in range(0,9):
		if i%3==0 and i!=0:
			print("---------------------------------")
		for j in range(0,9):
			if j%3==0 and j!=0:
				print("|   ",end="")
			print(board[i][j]," ",end="")
		print("")
printboard(board)
solve(board)
print("\n\n\n")
printboard(board)