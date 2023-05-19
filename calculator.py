from tkinter import *
def bracket1():#this is basically how you define a function
    usertext.insert(END,"(") # we have created a test (white space) and this is used to enter the text into our line
def bracket2():
    usertext.insert(END,")")
def C():#removing last character
    b=usertext.get("1.0",END)#this takes our string value from the usertext
    f=b.strip() #when we use get function \n is applied towards end , we use strfip to remove it
    k=(len(f)-1) #finds len -1 for string slicing
    m=b[0:k] #we get all value until the end , if 78 is out value then m =7
    usertext.delete("1.0",END) #delete our textbox
    usertext.insert(END,m) #insert m value
    
def delete():
    usertext.delete("1.0",END) #deletes the whole thing
def number7():
    usertext.insert(END,"7")
def number8():
    usertext.insert(END,"8")
def number9():
    usertext.insert(END,"9")
def numberx():
    usertext.insert(END,"*")
def number4():
    usertext.insert(END,"4")
def number5():
    usertext.insert(END,"5")
def number6():
    usertext.insert(END,"6")
def minus():
    usertext.insert(END,"-")   
def number3():
    usertext.insert(END,"3")   
def number2():
    usertext.insert(END,"2")   
def number1():
    usertext.insert(END,"1")   
def addition():
    usertext.insert(END,"+")  
def number0():
    usertext.insert(END,"0")   
def dot():
    usertext.insert(END,".")   
def divison():
    usertext.insert(END,"/")   
def equal():
    b=usertext.get("1.0",END)
    h=b.strip()
    k=" "
    for i in h:
        if i.isalpha()==True:
            usertext.delete("1.0",END)
            k=0
            break
        else: 
            k=k+i
    if k==0:
        usertext.insert(END,"")
    if k!=0:   
        c=eval(k)#coverts our string into integer or float because it only contains expression and integers
        usertext.delete("1.0",END)
        usertext.insert(END,c)
def top1():
    global btn1,btn2,btn3,btn4
    btn1=Button(root,text="(",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=bracket1)
    btn1.place(x=5,y=190)
    btn2=Button(root,text=")",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=bracket2)
    btn2.place(x=75,y=190)
    btn3=Button(root,text="C",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=C)
    btn3.place(x=145,y=190)
    btn4=Button(root,text="Del",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=delete)
    btn4.place(x=215,y=190)
def top2():
    global btn5,btn6,btn7,btn8
    btn5=Button(root,text="7",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number7)
    btn5.place(x=5,y=240)
    btn6=Button(root,text="8",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number8)
    btn6.place(x=75,y=240)
    btn7=Button(root,text="9",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number9)
    btn7.place(x=145,y=240)
    btn8=Button(root,text="x",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=numberx)
    btn8.place(x=215,y=240)
def top3():
    global btn9,btn10,btn11,btn12
    btn9=Button(root,text="4",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number4)
    btn9.place(x=5,y=290)
    btn10=Button(root,text="5",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number5)
    btn10.place(x=75,y=290)
    btn11=Button(root,text="6",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number6)
    btn11.place(x=145,y=290)
    btn12=Button(root,text="-",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=minus)
    btn12.place(x=215,y=290)
def top4():
    global btn13,btn14,btn15,btn16
    btn13=Button(root,text="1",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number1)
    btn13.place(x=5,y=340)
    btn14=Button(root,text="2",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number2)
    btn14.place(x=75,y=340)
    btn15=Button(root,text="3",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number3)
    btn15.place(x=145,y=340)
    btn16=Button(root,text="+",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=addition)
    btn16.place(x=215,y=340)
def top5():
    global btn17,btn18,btn19,btn20
    btn17=Button(root,text="0",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=number0)
    btn17.place(x=5,y=390)
    btn18=Button(root,text=".",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=dot)
    btn18.place(x=75,y=390)
    btn19=Button(root,text="÷",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=divison)
    btn19.place(x=145,y=390)
    btn20=Button(root,text="=",height="2",width="7",fg="white",font=("Scientific",10),bg='#303030',command=equal)
    btn20.place(x=215,y=390)   
root=Tk()
a=StringVar()
root.geometry("287x440")
root.title("Calculator")
canvas=Canvas(root,bg='#1b1b1b')
canvas.pack(fill=BOTH,expand=TRUE)
label1=Label(text="Calculator",fg="white",font=("Scientific",16),bg='#1b1b1b')
label1.place(x=5,y=15)
usertext=Text(root,height="3",width="21",font=("Arial",18),highlightthickness=0)
usertext.place(x=5,y=50)
top1()
top2()
top3()
top4()
top5()
root.mainloop()
