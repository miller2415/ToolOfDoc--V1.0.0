import datetime
import csv
import tkinter as tk

#tutorial-env\Scripts\activate #使用虛擬環境windows 在終端機選擇當前目錄 使用虛擬環境
#source tutorial-env/bin/activate #使用虛擬環境MacOS 在終端機選擇當前目錄 使用虛擬環境
#print(tk.TkVersion)版本8.6
#-------------------------------------------------------------------------------------------------------------------------------#
def CreateCSV (title) :
  # 開啟輸出的 CSV 檔案
  with open(title, 'a', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 寫入一列資料
    writer.writerow(['時間', '伺服器', '方塊','起始顆數','最後顆數','總計顆數','總計價格'])

def WriteCSV (title,time,Server,type,E1,E2,E12,money):
  with open(title, 'a', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 寫入一列資料
    writer.writerow([time, Server, type,E1,E2,E12,money])

CSVTitle = (str(datetime.datetime.now().year)    + '-' + 
         str(datetime.datetime.now().month)   + '-' +
         str(datetime.datetime.now().day)     + '_' +
         str(datetime.datetime.now().hour)    + '.csv')


CreateCSV(CSVTitle)
#-------------------------------------------------------------------------------------------------------------------------------#
root = tk.Tk()
root.title('RecordTool')#title

bg = "#323232" #323232
fg = "#FCFCFC" #FCFCFC #FFFFFF
#root.configure(bg=bg1)#背景顏色 macOS 原色HEX #323232 RGB (50,50,50)

fontType = 'Arial'

#print(root.winfo_screenwidth()) #輸出螢幕寬度
#print(root.winfo_screenheight()) #輸出螢幕高度
#Count=0    #count
w=650  #width
r=250  #height
x=500  #與視窗左上x的距離
y=200  #與視窗左上y的距離
root.geometry('%dx%d+%d+%d' % (w,r,x,y))
#-------------------------------------------------------------------------------------------------------------------------------#
TopLabel    =   tk.Label(root,text="洗方塊紀錄工具",font=(fontType,18,"bold"),bg=bg,fg=fg)
ValueLabel  =   tk.Label(root,text='顆數 : ',font=(fontType,12,"bold"),bg=bg,fg=fg)
ServerLabel =   tk.Label(root,text='伺服器 : ',font=(fontType,12,"bold"),bg=bg,fg=fg)
TypeLabel   =   tk.Label(root,text='方塊型態 : ',font=(fontType,12,"bold"),bg=bg,fg=fg)
LondaLabel  =   tk.Label(root,text='~',font=(fontType,14,"bold"),bg=bg,fg=fg)
L12         =   tk.Label(root,font=(fontType,14,"bold"),bg=bg,fg=fg)
L5ans       =   tk.Label(root,font=(fontType,14,"bold"),bg=bg,fg=fg)
TimeInfo    =   tk.Label(root,font=(fontType,14,"bold"),bg=bg,fg=fg)
#CountInfo   =   tk.Label(root,font=('',16,"bold"))

#-------------------------------------------------------------------------------------------------------------------------------#
E1=tk.Entry(root,width=6,bg="#FFFFFF",fg="#000000",border=1)
E2=tk.Entry(root,width=6,bg="#FFFFFF",fg="#000000",border=1)
#-------------------------------------------------------------------------------------------------------------------------------#

Server      =    {0:"艾麗亞",1:"普力特",2:"琉德",3:"優依娜",4:"愛麗西亞",5:"殺人鯨"}
ServerVar   =    tk.IntVar()
ServerVar.set(0)
def Selection1 ():
    print(Server.get(ServerVar.get()))

Type        =   {0:"閃炫",1:"結合"}
TypeVar     =   tk.IntVar()
TypeVar.set(0)
def Selection2 ():
    print(Type.get(TypeVar.get())) 

#-------------------------------------------------------------------------------------------------------------------------------#
def math():
    if TypeVar.get():
        money = 105
    else:
        money = 52

    text = (str(datetime.datetime.now().year) + '/' + 
                              str(datetime.datetime.now().month)+ '/' +
                              str(datetime.datetime.now().day)  + '/' +
                              str(datetime.datetime.now().hour) + ':' +
                              str(datetime.datetime.now().minute))
    TimeInfo.configure(text=text)

    try:
        value1 = int(E1.get())
        value2 = int(E2.get())
    except ValueError:
    # Handle the case where the input is not a valid integer
    # You may want to display an error message or take appropriate action.
        L12.configure(text='請輸入數字!')
        L5ans.configure(text='') 
        return

    if isinstance(eval(E1.get()),int) & isinstance(eval(E2.get()),int):
        if (eval(E1.get())<eval(E2.get())):
            L12.configure(text='顆數錯誤!')
            L5ans.configure(text='') 
        else:
            L12.configure(text =  '顆數 : '+ str(eval(E1.get())-eval(E2.get())) + ' * ' + str(money))
            L5ans.configure(text = '價格計算 : '+ str((eval(E1.get())-eval(E2.get()))*money))
            #Count = Count + 1
            #CountInfo.configure(text= '完成次數 : ' + str(Count))
            #寫入檔案
            WriteCSV(CSVTitle,
                     text,
                     Server.get(ServerVar.get()),
                     Type.get(TypeVar.get()),
                     E1.get(),
                     E2.get(),
                     (eval(E1.get())-eval(E2.get())),
                     str((eval(E1.get())-eval(E2.get()))*money))
            
    
    


CheckButtom=tk.Button(root,text='Enter',relief="ridge",
            background=fg,
            border=2,
            activebackground='#191970',#設定滑鼠位於按鈕時的背景顏色
            activeforeground='#191970',#設定滑鼠位於按鈕時的前景顏色
            state=tk.NORMAL,#設定按鈕的狀態
            cursor='heart',
            command=math)

#-------------------------------------------------------------------------------------------------------------------------------#
TopLabel.grid(row=0,column=0)#顯示的位置
ServerLabel.grid(row=1,column=0)

for val1, Server1 in Server.items():
    R1=tk.Radiobutton(root,text=Server1,variable=ServerVar,value=val1,command=Selection1,font=(fontType,10,"bold"),bg=bg,fg=fg)
    R1.grid(row=1,column=1+val1)

TypeLabel.grid(row=2,column=0)
for val2, Tpye in Type.items():
    R2=tk.Radiobutton (root,text=Tpye,variable=TypeVar, value=val2,command=Selection2,font=(fontType,10,"bold"),bg=bg,fg=fg)
    R2.grid(row=2,column=1+val2)

ValueLabel.grid(row=3,column=0)
E1.grid(row=3,column=1)
LondaLabel.grid(row=3,column=2)
E2.grid(row=3,column=3)
CheckButtom.grid(row=3,column=4)
#CountInfo.grid(row=3,column=5)
L12.grid(row=5,column=0)
L5ans.grid(row=6,column=0)
TimeInfo.grid(row=7,column=0)
#-------------------------------------------------------------------------------------------------------------------------------#
root.mainloop()

