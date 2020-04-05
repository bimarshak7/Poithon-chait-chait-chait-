import random
from tkinter import *
from tkinter import messagebox
root=Tk()
icon=PhotoImage(file="pass.png")
root.iconphoto(True,icon)
root.minsize(650,100)
root.maxsize(800,200)
root.title("Random Password Generator")
slider=Scale(root,from_=5,to=55,sliderlength=10,orient=HORIZONTAL,activebackground="blue",troughcolor="brown",
relief=FLAT,cursor="cross",length=350,tick=5)
slider.grid(row=0,column=1)
fdp=Entry(root,width=57)
fdp.grid(row=2,column=1,columnspan=2)
def genr():
	psw=""
	n=slider.get()
	str="!£$%&*@#abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ;,?+=()"
	for i in range(0,n):
		ch=random.choice(str)
		psw+=ch
		fdp.delete(0,END)
		fdp.insert(0,psw)
		done=Label(text="Password Generated",fg="green").grid(row=4,column=1)		
def copy_button():
	if fdp.get()!="":
		clip = Tk()
		clip.withdraw()
		clip.clipboard_clear()
		clip.clipboard_append(fdp.get())
		clip.destroy()
		Label(text="Password copied to clipboard",fg="green").grid(row=6,column=1)
		Label(text="Paste it before you close this program!!!",fg="red").grid(row=7,column=0,columnspan=3)
		
	else:
		Label(text="Generate Password first",fg="red").grid(row=6,column=1)
Label(text="Set Length").grid(row=0,column=0)
Label(text="Generated Password").grid(row=2,column=0)
Button(text="Generate",command=genr,bg="green",fg="white",border=5,padx=32,relief=GROOVE).grid(row=0,column=2)
Button(text="COPY password",command=copy_button,fg="blue").grid(row=5,column=1)

def qtclk():
	qtv=messagebox.askokcancel("QUIT!","Are you sure?")
	if qtv==1:
		quit()


Button(text="QUIT!",command=qtclk,fg="white",bg="red").grid(row=6,column=2)
root.mainloop()