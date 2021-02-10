from tkinter import *
r=Tk()
r.title("Feedback Form")
r.geometry("500x500")

canvas=Canvas(r,height=300,width=200)
canvas.grid(padx=20,pady=10,row=0)
Label(canvas,text="Feedback Form",bd=2,font=("Calibri",12),relief="solid",bg="yellow").grid()

Label(r,text="Name").grid(padx=20,pady=10,row=1,column=0)
Label(r,text="Roll No.").grid(padx=20,pady=10,row=2,column=0)
Label(r,text="Email address").grid(padx=20,pady=10,row=3,column=0)

Entry(r).grid(row=1,column=1)
Entry(r).grid(row=2,column=1)
Entry(r).grid(row=3,column=1)

Button(r,text="Submit",command=r.destroy).grid(row=4,column=1)

mainloop()