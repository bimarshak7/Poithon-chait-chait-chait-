from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("CALCULATOR")
root.maxsize(800,1200)
#root.iconbitmap("calc.ico")
#display widget
fd1=Entry(root,width=15,font=("Arial",28))
fd1.grid(row=0,column=0,columnspan=3,pady=7)
#read number clicked
def btn_clk(num):
	curr=fd1.get()
	fd1.delete(0,END)
	fd1.insert(0,str(curr) + str(num))	
#clear display
def btn_clr():
	fd1.delete(0,END)
#read operations
def btn_add():
	prev=fd1.get()
	global fnum
	global math
	math="add"
	fnum=int(prev)
	fd1.delete(0,END)
def btn_sub():
	prev=fd1.get()
	global fnum
	global math
	math="sub"
	fnum=int(prev)
	fd1.delete(0,END)
def btn_mul():
	prev=fd1.get()
	global fnum
	global math
	math="mul"
	fnum=int(prev)
	fd1.delete(0,END)
def btn_div():
	prev=fd1.get()
	global fnum
	global math
	math="div"
	fnum=int(prev)
	fd1.delete(0,END)
#pidentify operation, do calculation and display result
def btn_eql():
	snum=fd1.get()
	fd1.delete(0,END)
	if math=="add":
		fd1.insert(0,fnum+int(snum))
	elif math=="sub":
		fd1.insert(0,fnum-int(snum))
	elif math=="mul":
		fd1.insert(0,fnum*int(snum))
	elif math=="div":
		fd1.insert(0,fnum/int(snum))
	else:
		pass
#button creation	
bt0=Button(root,text="0",padx=20,pady=22,command=lambda: btn_clk(0))
bt1=Button(root,text="1",padx=20,pady=22,command=lambda: btn_clk(1))
bt2=Button(root,text="2",padx=20,pady=22,command=lambda: btn_clk(2))
bt3=Button(root,text="3",padx=20,pady=22,command=lambda: btn_clk(3))
bt4=Button(root,text="4",padx=20,pady=22,command=lambda: btn_clk(4))
bt5=Button(root,text="5",padx=20,pady=22,command=lambda: btn_clk(5))
bt6=Button(root,text="6",padx=20,pady=22,command=lambda: btn_clk(6))
bt7=Button(root,text="7",padx=20,pady=22,command=lambda: btn_clk(7))
bt8=Button(root,text="8",padx=20,pady=22,command=lambda: btn_clk(8))
bt9=Button(root,text="9",padx=20,pady=22,command=lambda: btn_clk(9))
btad=Button(root,text="+",padx=20,pady=22,command=lambda: btn_add())
btsub=Button(root,text="-",padx=20,pady=22,command=lambda: btn_sub())
btmul=Button(root,text="X",padx=20,pady=22,command=lambda: btn_mul())
btdiv=Button(root,text="/",padx=20,pady=22,command=lambda: btn_div())

bteql=Button(root,text="=",padx=57,pady=20,command=lambda: btn_eql(),bg="blue",fg="white")
btclr=Button(root,text="Clr",padx=20,pady=22,command=lambda: btn_clr(),bg="red",fg="white")
#button placement
bt0.grid(row=6,column=0)

bt1.grid(row=4,column=0)
bt2.grid(row=4,column=1)
bt3.grid(row=4,column=2)

bt4.grid(row=3,column=0)
bt5.grid(row=3,column=1)
bt6.grid(row=3,column=2)

bt7.grid(row=2,column=0)
bt8.grid(row=2,column=1)
bt9.grid(row=2,column=2)

btad.grid(row=5,column=1)
btsub.grid(row=5,column=0)
btmul.grid(row=5,column=2)
btdiv.grid(row=6,column=1)

bteql.grid(row=7,column=0,columnspan=2)
btclr.grid(row=6,column=2)

def qtclk():
	qtv=messagebox.askokcancel("QUIT!","Are you sure?")
	if qtv==1:
		quit()
btquit=Button(root,text="QUIT!",padx=20,pady=22,command=qtclk,bg="red",fg="white")
btquit.grid(row=7,column=2)

root.mainloop()