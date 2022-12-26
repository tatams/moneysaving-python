from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook
from tkinter import font
import csv
import tkinter.messagebox

GUI=Tk()
GUI.option_add('*font', 'AngsanaUPC 13')
GUI.title('มันนี่มา')
GUI.minsize(530,400)
Tab=Notebook(GUI)
F1=Frame(Tab,width=500,height=600)
F2=Frame(Tab,width=500,height=600)
F3=Frame(Tab,width=500,height=600)
F4=Frame(Tab,width=500,height=600)
#พื้นหลัง----------------------------
photo=PhotoImage(file="1.png")
photoo=Label(F1,image=photo)
photoo.place(x=0,y=0)
photo2=PhotoImage(file="2.png")
photoo2=Label(F2,image=photo2)
photoo2.place(x=0,y=0)
photo3=PhotoImage(file="3.png")
photoo3=Label(F3,image=photo3)
photoo3.place(x=0,y=0)
photo4=PhotoImage(file="4.png")
photoo4=Label(F4,image=photo4)
photoo4.place(x=0,y=0)
#-----------------------------------

Tab.add(F1,text='Income/Expense')
Tab.add(F2,text='History')
Tab.add(F3,text='Goal')
Tab.add(F4,text='Paid')
Tab.pack(fill=BOTH, expand=1)

Big=[]
Listincome=[]
Listexpense=[]
Listaom=[]
lstcsv_data=[]

lstcsv_income=[]
lstcsv_expense=[]
lstcsv_aom=[]
alllstcsv_g=[]
lstcsv_g=[]

sumicsv=0
sumecsv=0
sumacsv=0

r=0

#F1 : บันทึกรับจ่าย +++++++++++++++++++++++++++++++++++++++++++++++

#เขียนไฟล์ csv----------------------------------------------
f_data="data.csv"
with open(f_data,"a",encoding="utf-8") as outfile:
    writer=csv.writer(outfile)
f_income="income.csv"
with open(f_income,"a",encoding="utf-8") as outfile:
    writer=csv.writer(outfile)
f_expense="expense.csv"
with open(f_expense,"a",encoding="utf-8") as outfile:
    writer=csv.writer(outfile)
f_aom="aom.csv"
with open(f_aom,"a",encoding="utf-8") as outfile:
    writer=csv.writer(outfile)
f_goal="goal.csv"
with open(f_goal,"a",encoding="utf-8") as infile:
    writer=csv.writer(outfile)
#-----------------------------------------------------    
#อ่านไฟล์ csv เก่า-------------------------------------------
f_income="income.csv"
with open(f_income,"r",encoding="utf-8") as infile:
    rdi = csv.reader(infile)
    mylisti=list(rdi)
sumicsv=0
for row in mylisti:
    sumicsv+=eval(row[0])

f_expense="expense.csv"
with open(f_expense,"r",encoding="utf-8") as infile:
    rde = csv.reader(infile)
    myliste=list(rde)
sumecsv=0
for row in myliste:
    sumecsv+=eval(row[0])

f_aom="aom.csv"
with open(f_aom,"r",encoding="utf-8") as infile:
    rda = csv.reader(infile)
    mylista=list(rda)
sumacsv=0
for row in mylista:
    sumacsv+=eval(row[0])
#------------------------------------------------------
f2=Frame(F2)
f2.grid(row=1,column=2,padx=5,pady=5)
listbox_Big = Listbox(f2, height=12, width=35, selectmode=SINGLE, exportselection=0)
#เปิด file data csv -------------------------------------
f_data="data.csv"
with open(f_data,"r",encoding="utf-8") as infile:
    rdd = csv.reader(infile)
    mylistd=list(rdd)
count_mylistd = len(mylistd)
for i in range (count_mylistd):
    listbox_Big.insert(0,mylistd[i])
    listbox_Big.pack()
#------------------------------------------------------
listbox_Big.grid(row=0, column=0)

scroll_y = Scrollbar(f2, orient=VERTICAL, command=listbox_Big.yview)
scroll_y.grid(row=0, column=1, stick=N + S)
listbox_Big.config(yscrollcommand=scroll_y.set)

scroll_x = Scrollbar(f2, orient=HORIZONTAL, command=listbox_Big.xview)
scroll_x.grid(row=1, column=0, stick=E + W)
listbox_Big.config(xscrollcommand=scroll_x.set)


def save():
    try:
        global r
        List=[]
        a=day.get()
        b=month.get()
        c=year.get()
        d=mycombo.get()
        e=ETittle.get()
        f=Eb.get()
        f_eval=eval(f)
        si=sum(Listincome)
        
        dayy_eval=eval(a)
        c_eval=eval(c)
        yr=(c_eval/4)-(c_eval//4)
        
        countoption= options.index(d)
        #แจ้งเตือนวันเดือนปีผิด-----------------------
        
        if f == "0" or e == "" or f_eval<0 or (yr==0.75 and b == "กุมภาพันธ์"
        and dayy_eval >= 30) or (b == "กุมภาพันธ์" and dayy_eval >= 29)\
        or ((b == "เมษายน" or b == 'กันยายน' or b == 'มิถุนายน' or b == 'พฤษจิกายน')\
        and(dayy_eval > 30)):
        #28 29 กุมภา
            if yr==0.75 and b == "กุมภาพันธ์" and dayy_eval >= 30 :
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","เดือนกุมภาพันธ์ของปีนี้มีแค่ 29 วัน")

            elif b == "กุมภาพันธ์" and dayy_eval >= 29 :
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","เดือนกุมภาพันธ์ของปีนี้มีแค่ 28 วัน")
                
        #30 31 วัน        
            elif ((b == "เมษายน" or b == 'กันยายน' or b == 'มิถุนายน' or b == 'พฤษจิกายน')and(dayy_eval > 30)):
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","เดือนนี้มีแค่ 30 วัน")
        #--------------------------------------
    #เงื่อนไขให้ใส่จำนวนเงินและข้อความ
            elif f == "0" :
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","กรุณาใส่จำนวนเงิน")
            elif f_eval<0:
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","จำนวนเงินติดลบ")
            else:
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","กรุณาบันทึก \n หมายเหตุ:ไม่มีใส่ขีด")
        else:
            #เก็บประวัติรวม
            List.append(a)
            List.append(b)
            List.append(c)
            List.append(d)
            List.append(e)
            List.append(str(f))
            Big.append(List)
            lstcsv_data.append(List)
            
            file=open('data.txt','a')
            file.write(a)
            file.write(b)
            file.write(c)
            file.write('\t')
            file.write(d)
            file.write('\t')
            file.write(e)
            file.write('\t')
            file.write(f)
            file.write('บาท')
            file.write('\n')
            file.close()
            #เพิ่มเข้า file csv----------------------------------------
            f_data="data.csv"
            with open(f_data,"a",encoding="utf-8") as outfile:
                writer = csv.writer(outfile,lineterminator="\n")
                writer.writerows(lstcsv_data)
            lstcsv_data.pop(0)
            #-----------------------------------------------------
            #เก็บlistรายรับ รายจ่าย เงินออม
            countoption= options.index(d) #จะอ่านค่าเป็น 0 1 2 เรียงตามลำดับ combobox
            if countoption == 0: #รายรับ
                Listincome.append(eval(f))
                
                file=open('data2.txt','a')
                file.write('รายรับ')
                g=str(f)
                file.write(g)
                file.write('บาท')
                file.write('\n')
                file.close()
                
                #เพิ่มเข้า file csv---------------------------------------
                f_income="income.csv"
                allincomecsv=[]
                allincomecsv.append(f)
                lstcsv_income.append(allincomecsv)
                with open(f_income,"a",encoding="utf-8") as outfile:
                    writer = csv.writer(outfile,lineterminator="\n")
                    writer.writerows(lstcsv_income)
                lstcsv_income.pop(0)
                #---------------------------------------------------
            elif countoption == 1: #รายจ่าย
                Listexpense.append(eval(f))
                file=open('data3.txt','a')
                file.write('รายจ่าย')
                h=str(f)
                file.write(h)
                file.write('บาท')
                file.write('\n')
                file.close()
                
                #เพิ่มเข้า file csv---------------------------------------
                f_expense="expense.csv"
                allexpensecsv=[]
                allexpensecsv.append(f)
                lstcsv_expense.append(allexpensecsv)
                with open(f_expense,"a",encoding="utf-8") as outfile:
                    writer = csv.writer(outfile,lineterminator="\n")
                    writer.writerows(lstcsv_expense)
                lstcsv_expense.pop(0)
                #---------------------------------------------------
            else: #เงินออม
                Listaom.append(eval(f))
                file=open('data4.txt','a')
                file.write('ออมเงิน')
                i=str(f)
                file.write(i)
                file.write('บาท')
                file.write('\n')
                file.close()
                #เพิ่มเข้า file csv---------------------------------------
                f_aom="aom.csv"
                allaomcsv=[]
                allaomcsv.append(f)
                lstcsv_aom.append(allaomcsv)
                with open(f_aom,"a",encoding="utf-8") as outfile:
                    writer = csv.writer(outfile,lineterminator="\n")
                    writer.writerows(lstcsv_aom)
                lstcsv_aom.pop(0)
                #---------------------------------------------------
            
            #F2 : ประวัติ
            listbox_Big.insert(0,Big[r])
            listbox_Big.grid(row=0, column=0)
            r+=1
            display2.set("{} {} {}  {} {} {} บาท".format(a,b,c,d,e,f))
            
    except Exception as e: #ดักerror
            import tkinter.messagebox
            tkinter.messagebox.showerror("ERROR","กรุณาลองใหม่อีกครั้ง") 
            print(e)
    
display2=StringVar() 
f1=Frame(F1)
f1.grid(row=1,column=2,padx=5,pady=5)

dp2=Label(F1,textvariable=display2,font="AngsanaUPC 20",background='#FBF1D5')
dp2.grid(row=5,column=2,pady=5)

month_list = ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม', 'กันยายน',
              'ตุลาคม', 'พฤษจิกายน','ธันวาคม']

day = ttk.Combobox(f1, values=list(range(1, 32)), width=3, state="readonly")
day.current(0)
day.pack(side=LEFT)

month = ttk.Combobox(f1, values=month_list, width=8, state="readonly")
month.current(0)
month.pack(side=LEFT)

year = ttk.Combobox(f1, values=list(range(2563, 2591)), width=5)
year.current(0)
year.pack(side=LEFT)

L=Label(F1,text="บันทึกรายรับ - รายจ่าย",font='AngsanaUPC 18 bold',bg='#F4CC84')
L.grid(row=0,column=2,padx=5,pady=5)
        

LDate=ttk.Label(F1,text='วัน/เดือน/ปี \t',font = 'AngsanaUPC 18 bold',background='#FFFFFF')
LDate.grid(row=1,column=1,sticky=E)
Date = StringVar()

LTittle=ttk.Label(F1,text='บันทึก',font = 'AngsanaUPC 18 bold',background='#FFFFFF')
LTittle.grid(row=4,column=1,padx=5,pady=5)
Title = StringVar()
ETittle = ttk.Entry(F1, textvariable=Title ,font='AngsanaUPC 14',background='#FFFFFF')
ETittle.grid(row=4,column=2,padx=5,pady=5)
ETittle.focus()
            
options=["รายรับ","รายจ่าย","เงินออม"]
  
L=L=Label(F1,text="เลือกประเภททำรายการ",font='AngsanaUPC 18 bold',background='#FFFFFF')
L.grid(row=2,column=1,padx=5,pady=5)
        
mycombo=ttk.Combobox(F1,value=options,state="readonly")
mycombo.current(0)
mycombo.grid(row=2,column=2,pady=20)
        
Lb=ttk.Label(F1,text='จำนวนเงิน',font = 'AngsanaUPC 18 bold',background='#FFFFFF')
Lb.grid(row=3,column=1,padx=5,pady=5)
bun = IntVar()
Eb = Entry(F1, textvariable=bun ,font='AngsanaUPC 14')
Eb.grid(row=3,column=2,padx=5,pady=5)
Eb.focus()

BAdd = Button(F1,text='SAVE', font = 'AngsanaUPC 18 bold',command=save,background='#EEB189')
BAdd.grid(row=6,column=2,padx=5,pady=5)

#F2 : ประวัติ +++++++++++++++++++++++++++++++++++++++++++++++
f2=Frame(F2)
f2.grid(row=1,column=2,padx=5,pady=5)

f22=Frame(F2)
f22.grid(row=1,column=3,padx=5,pady=5)

f221=Frame(f22)
f221.pack(side=TOP)

f222=Frame(f22)
f222.pack(side=TOP)

f223=Frame(f22)
f223.pack(side=TOP)

f224=Frame(f22)
f224.pack(side=TOP)

f225=Frame(f22)
f225.pack(side=TOP)

displayh=StringVar()
displayg=StringVar() #ของเป้าหมาย

LD=Label(F2,text="ประวัติการบันทึก",font='AngsanaUPC 18 bold',background='#D1EAF5')
LD.grid(row=0,column=2,padx=5,pady=5)

def incomef ():
    i=sum(Listincome) + sumicsv
    displayh.set("รายรับทั้งหมด {:.2f} บาท".format(i))
    
def expensef ():
    e=sum(Listexpense) + sumecsv
    displayh.set("รายจ่ายทั้งหมด {:.2f} บาท".format(e))
    
def aomf ():
    a=sum(Listaom) + sumacsv
    displayh.set("เงินออมทั้งหมด {:.2f} บาท".format(a))
    
def math(a,b):
    total=a-b
    return total

def totalf ():
    i=sum(Listincome) + sumicsv
    e=sum(Listexpense) + sumecsv
    sum1=math(i,e)
    displayh.set("เงินคงเหลือทั้งหมด {:.2f} บาท".format(sum1))

bt_income=Button(f221,text='รายรับ', font = 'AngsanaUPC 18 bold',width=8,command=incomef,background='#AACCE2')
bt_income.pack(side=LEFT)
bt_expense=Button(f221,text='รายจ่าย', font = 'AngsanaUPC 18 bold',width=8,command=expensef,background='#AACCE2')
bt_expense.pack(side=LEFT)
bt_aom=Button(f222,text='เงินออม', font = 'AngsanaUPC 18 bold',width=8,command=aomf,background='#AACCE2')
bt_aom.pack(side=LEFT)
bt_total=Button(f222,text='คงเหลือ', font = 'AngsanaUPC 18 bold',width=8,command=totalf,background='#AACCE2')
bt_total.pack(side=LEFT)

#อ่าน file csv goal (หน้าเป้าหมาย)----------------------------------------

f_goal="goal.csv"
with open(f_goal,"r",encoding="utf-8") as infile:
    rdg = csv.reader(infile)
    mylistg=list(rdg)
Gcsv=""
Gcsv2=0
for row in mylistg:
    Gcsv=str(row[0])
    Gcsv2=eval(row[1])

#--------------------------------------------------------

dpbt=Label(f223,textvariable=displayh,font="AngsanaUPC 20",background='#FBF1D5')
dpbt.pack(side=BOTTOM)

#F3 : เป้าหมาย +++++++++++++++++++++++++++++++++++++++++++++++
f3=Frame(F3)
f3.grid(row=6,column=1,padx=5,pady=5)

def saveg():       
    try:
        global Gcsv,Gcsv2
        input_goal = str(Goal.get()) #เป้าหมาย str
        input_goal2 = str(Goal2.get()) #จำนวนเงิน str
        goal2_eval = eval(input_goal2) #จำนวนเงิน eval
        if input_goal == "" or input_goal2 == "0" or goal2_eval < 0 : #เงื่อนไขให้ใส่จำนวนเงินและเป้าหมาย
            if input_goal == "":
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","กรุณาใส่เป้าหมาย")
            elif goal2_eval < 0:
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","จำนวนเงินติดลบ")
            else:
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","กรุณาใส่จำนวนเงิน")
        else:
            file=open('dataGoal.txt','w')
            file.write("เป้าหมายที่ได้ตั้งไว้ : {} \n".format(input_goal))
            file.write("ราคา : {} บาท".format(input_goal2))
            file.close()
            display.set("{} ราคา {} บาท".format(input_goal,input_goal2))
            #เก็บ csv goal-------
            f_goal="goal.csv"
            alllstcsv_g=[]
            lstcsv_g=[]
            lstcsv_g.append(input_goal)
            lstcsv_g.append(goal2_eval)
            alllstcsv_g.append(lstcsv_g)
            with open(f_goal,"a",encoding="utf-8") as outfile:
                writer = csv.writer(outfile,lineterminator="\n")
                writer.writerows(alllstcsv_g)
            #------------------
            a=sum(Listaom) + sumacsv
            Gcsv=input_goal
            Gcsv2=goal2_eval
            wantincsvs= Gcsv2 - a
            if wantincsvs<=0:
                displayg.set("ถึงเป้าหมายแล้ว")
            else:
                displayg.set("อีก {} บาท ถึงเป้าหมาย".format(wantincsvs))
        return Gcsv,Gcsv2
    except Exception as e: #ดักerror รับค่าตัวเลข (ถ้าปล่อยช่องใส่ตัวเลขเปล่าๆจะเกิดerror)
            import tkinter.messagebox
            tkinter.messagebox.showerror("Error","กรุณาลองใหม่อีกครั้ง") 
            print(e)
            
Goal=StringVar()
Goal2=IntVar()
aompaid=IntVar()
display=StringVar()
displaytotalpaid=StringVar()

#csv----------------------------------------------
if Gcsv=="" and Gcsv2==0:
    display.set("ยังไม่ได้ตั้งเป้าหมาย")
else:
    display.set("{} ราคา {} บาท".format(Gcsv,Gcsv2))
#-------------------------------------------------    

L=Label(F3,text="เป้าหมายการออม",font='AngsanaUPC 18 bold',background='#FFD6DA')
L.grid(row=0,column=1,padx=5,pady=5)
    
LGoal=ttk.Label(F3,text='เป้าหมาย \t',font = 'AngsanaUPC 18 bold',background='#FFFFFF')
LGoal.grid(row=1,column=0,padx=5,pady=5)
   
EGoal = ttk.Entry(F3, textvariable= Goal ,font='AngsanaUPC 14')
EGoal.grid(row=1,column=1,padx=5,pady=5 )
EGoal.focus()

LGoal2=ttk.Label(F3,text='จำนวนเงิน',font = 'AngsanaUPC 18 bold',background='#FFFFFF')
LGoal2.grid(row=2,column=0,padx=5,pady=5)
    
EGoal2 = ttk.Entry(F3, textvariable=Goal2 ,font='AngsanaUPC 14')
EGoal2.grid(row=2,column=1,padx=5,pady=5 )


dp=Label(F3,textvariable=display,font="AngsanaUPC 20",background='#FBF1D5')
dp.grid(row=3,column=1,pady=5)

dpg=Label(f224,textvariable=displayg,font="AngsanaUPC 20",background='#FBF1D5') #ไปแสดงที่หน้าประวัติ
dpg.pack(side=TOP)

B2Add = Button(F3,text='SAVE',font = 'AngsanaUPC 18 bold',command=saveg,background='#F7B2A9')
B2Add.grid(row=4,column=1,padx=5,pady=5)

#เลื่อนลงมาเพราะตัวแปร (หน้าประวัติ)------------
def re (): #รีเป้าหมาย อัพเดตให้เป็นล่าสุด
    global Gcsv2
    a=sum(Listaom) + sumacsv
    wantincsv= Gcsv2 - a
    if Gcsv2==0:
        displayg.set("ยังไม่ได้ตั้งเป้าหมาย")
    elif wantincsv<=0 :
        displayg.set("ถึงเป้าหมายแล้ว")
    else:
        displayg.set("อีก {} บาท ถึงเป้าหมาย".format(wantincsv))
        
bt_re=Button(f225,text='อัพเดตเป้าหมายล่าสุด', font = 'AngsanaUPC 18 bold',width=16,command=re,background='#ABBDEE')
bt_re.pack(side=BOTTOM)
#------------
#F4 : ใช้เงินออม
def aom_p():
    try:
        ap=aompaid.get()
        a=sum(Listaom) + sumacsv
        if ap<0 or a==0 or ap>a or ap==0 :
            if ap<0:
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","จำนวนติดลบ")
            elif ap==0:
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","กรุณาใส่จำนวนเงิน")
            else:
                import tkinter.messagebox
                tkinter.messagebox.showwarning("Warning","เงินออมไม่พอ")
        else:
            paid= a-ap
            Listaom.append(-ap)
            displaytotalpaid.set("เงินออมคงเหลือ {} บาท".format(paid))

    except Exception as e: #ดักerror รับค่าตัวเลข (ถ้าปล่อยช่องใส่ตัวเลขเปล่าๆจะเกิดerror)
            import tkinter.messagebox
            tkinter.messagebox.showerror("Error","กรุณาลองใหม่อีกครั้ง") 
            print(e)

Laom=ttk.Label(F4,text='ใช้เงินออม',font = 'AngsanaUPC 18 bold',background='#E7D2EF')
Laom.grid(row=1,column=1,padx=5,pady=5)

Lmaom=ttk.Label(F4,text='จำนวนเงิน\t',font = 'AngsanaUPC 18 bold',background='#FFFFFF')
Lmaom.grid(row=2,column=0,padx=5,pady=5)

Eaom = ttk.Entry(F4, textvariable=aompaid ,font='AngsanaUPC 14')
Eaom.grid(row=2,column=1,padx=5,pady=5)

B2Add = Button(F4,text='SAVE',font = 'AngsanaUPC 18 bold',command=aom_p,background='#C6A5C7')
B2Add.grid(row=4,column=1,padx=5,pady=5)

dpa=Label(F4,textvariable=displaytotalpaid,font="AngsanaUPC 20",background='#FBF1D5')
dpa.grid(row=3,column=1,padx=5,pady=5)

GUI.mainloop()

























