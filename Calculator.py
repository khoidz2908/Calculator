from tkinter import *
#hàm tính toán

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    txt_Input.set(operator)
def btnDelete():
    global operator
    operator=operator[:-1]
    txt_Input.set(operator)
def btnClear():
    global operator
    operator=""
    txt_Input.set("")
def btnEqualsInput():
    global operator
    result=str(eval(operator))
    txt_Input.set(result)


cal=Tk()
cal.title('Calculator By 2KPCL')
operator=''
txt_Input=StringVar()
#tạo các dãy số
#hàng 1
txtDisplay=Entry(cal,width=30,font=('arial',15,'bold'),textvariable=txt_Input,bd=20,insertwidth=4,bg='white',justify='right').grid(columnspan=5)
line1_OpenNgoac=Button(cal,padx=15,bd=4,fg='black',font=('arial',10,'bold'),text='(',command=lambda:btnClick('('),bg='light green').grid(row=1,column=0)
line1_CloseNgoac=Button(cal,padx=10,bd=8,fg='black',font=('arial',10,'bold'),text=')',command=lambda:btnClick(')'),bg='light green').grid(row=1,column=1)
line1_Del=Button(cal,padx=45,bd=8,fg='black',font=('arial',15,'bold'),text='Del',command=btnDelete,bg='light green').grid(row=1,column=2,columnspan=2)
#hàng 2
line2_7=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='7',command=lambda:btnClick(7),bg='silver').grid(row=2,column=0)
line2_8=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='8',command=lambda:btnClick(8),bg='silver').grid(row=2,column=1)
line2_9=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='9',command=lambda:btnClick(9),bg='silver').grid(row=2,column=2)
line2_Chia=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='/',command=lambda:btnClick('/'),bg='light green').grid(row=2,column=3)
#hàng 3
line3_4=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='4',command=lambda:btnClick(4),bg='silver').grid(row=3,column=0)
line3_5=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='5',command=lambda:btnClick(5),bg='silver').grid(row=3,column=1)
line3_6=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='6',command=lambda:btnClick(6),bg='silver').grid(row=3,column=2)
line2_Chia=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='*',command=lambda:btnClick('*'),bg='light green').grid(row=3,column=3)
#hàng 4
line4_1=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='1',command=lambda:btnClick(1),bg='silver').grid(row=4,column=0)
line4_2=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='2',command=lambda:btnClick(2),bg='silver').grid(row=4,column=1)
line4_3=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='3',command=lambda:btnClick(3),bg='silver').grid(row=4,column=2)
line4_Tru=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='-',command=lambda:btnClick('-'),bg='light green').grid(row=4,column=3)
#hàng 5
line5_Clear=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='C',command=btnClear,bg='light green').grid(row=5,column=0)
line5_0=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='0',command=lambda:btnClick(0),bg='silver').grid(row=5,column=1)
line5_Cham=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='.',command=lambda:btnClick('.'),bg='light green').grid(row=5,column=2)
line5_Cong=Button(cal,padx=10,bd=8,fg='black',font=('arial',15,'bold'),text='+',command=lambda:btnClick('+'),bg='light green').grid(row=5,column=3)
line5_Bang=Button(cal,padx=160,bd=8,fg='black',font=('arial',15,'bold'),text='=',command=btnEqualsInput,bg='light green').grid(row=6,columnspan=4)
cal.mainloop()
