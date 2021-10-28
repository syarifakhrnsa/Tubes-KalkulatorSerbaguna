# import library yang dibutuhkan 
from tkinter import *
import math
import parser 
import tkinter.messagebox
import tkinter.font 

# main aplikasi
root = Tk()
root.title("Kalkulator Cinta <3")
root.resizable(width=False, height=False)
root.geometry('400x492+460+40')

# membuat frame baru untuk aplikasi
MainFrame = Frame(root, pady=2, relief=RIDGE)
MainFrame.grid() 
calFrame = Frame(MainFrame, bd=20, pady=2, relief=RIDGE)
calFrame.grid()

# mendefinisikan fungsi-fungsi untuk perhitungan-perhitungan dalam kalkulator
# kelompokan dalam satu kelas
class Calc():
	def __init__(self): 
		self.total=0
		self.current=''
		self.input_value=True
		self.check_sum=False
		self.op=''
		self.result=False

	# input nilai angka yang akan dihitung 
	def numberEnter(self, num):
		self.result=False
		firstnum=txtResult.get()
		secondnum=str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value=False
		else:
			if secondnum == '.':
				if secondnum in firstnum:
					return
			self.current = firstnum+secondnum
		self.display(self.current)

	# menghitung total nilai
	def sum_of_total(self):
		self.result=True
		self.current=float(self.current)
		if self.check_sum==True:
			self.valid_function()
		else:
			self.total=float(txtResult.get())

	# reset nilai secara otomatis
	def display(self, value):
		txtResult.delete(0, END)
		txtResult.insert(0, value)

	# fungsi perhitungan dengan operasi sederhana
	def valid_function(self): # secara manual tanpa bantuan modul
		if self.op == "add":
			self.total += self.current
		if self.op == "sub":
			self.total -= self.current
		if self.op == "multi":
			self.total *= self.current
		if self.op == "divide":
			self.total /= self.current
		if self.op == "mod":
			self.total %= self.current
		self.input_value=True
		self.check_sum=False
		self.display(self.total)

	# fungsi untuk button per operator
	def operation(self, op):
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total=self.current
			self.input_value=True
		self.check_sum=True
		self.op=op
		self.result=False

	# menghapus entry terakhir yang diinput
	def Clear_Entry(self):
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value=True

	# menghapus entry keseluruhan
	def All_Clear_Entry(self):
		self.Clear_Entry()
		self.total=0

	# konstanta pi 
	def pi(self): # secara manual tanpa bantuan modul
		self.result = False
		self.current = 3.1415926535897932384626433832795
		self.display(self.current)

	# konstanta 2 pi
	def tau(self): # secara manual tanpa bantuan modul
		self.result = False
		self.current = 2*3.1415926535897932384626433832795
		self.display(self.current)

	# konstanta matematika e 
	def e(self): # secara manual tanpa bantuan modul 
		self.result = False
		self.current = 2.718281828459045
		self.display(self.current)

	# mengalikan nilai entry dengan -1
	def mathPM(self): 
		self.result = False
		self.current = -(float(txtResult.get()))
		self.display(self.current)

	# mengembalikan nilai akar dari sebuah bilangan 
	def squared(self): # secara manual tanpa bantuan modul
		self.result = False
		self.current = float(txtResult.get())**(1/2)
		self.display(self.current)

	# mengembalikan nilai sin dari sebuah sudut
	def sin(self): # secara manual tanpa bantuan modul
		pi = 3.1415926535897932384626433832795
		rad = 180/pi
		sudut = float(txtResult.get())
		radian = sudut/rad
		def faktorial (n):
			if n==0 :
				return 1
			else :
				return n*faktorial(n-1)
		deretsin = radian-(1/faktorial(3)*(radian**3))+(1/faktorial(5)*(radian**5))-(1/faktorial(7)*(radian**7))+(1/faktorial(9)*(radian**9))-(1/faktorial(11)*(radian**11))+(1/faktorial(13)*(radian**13))
		self.result = False
		self.display('{0:.4f}'.format(round(deretsin,3)))

	# mengembalikan nilai cos dari sebuah sudut
	def cos(self): # secara manual tanpa bantuan modul
		pi = 3.1415926535897932384626433832795
		rad = 180/pi
		sudut = float(txtResult.get())
		radian = sudut/rad
		def faktorial (n):
			if n==0 :
				return 1
			else :
				return n*faktorial(n-1)
		deretcos = 1-(1/faktorial(2)*(radian**2))+(1/faktorial(4)*(radian**4))-(1/faktorial(6)*(radian**6))+(1/faktorial(8)*(radian**8))-(1/faktorial(10)*(radian**10))+(1/faktorial(12)*(radian**12))
		self.result = False
		self.display('{0:.4f}'.format(round(deretcos,3)))

	# mengembalikan nilai tan dari sebuah sudut
	def tan(self): # secara manual tanpa bantuan modul
		pi = 3.1415926535897932384626433832795
		rad = 180/pi
		sudut = float(txtResult.get())
		radian = sudut/rad
		def faktorial (n):
			if n==0 :
				return 1
			else :
				return n*faktorial(n-1)
		derettan = radian+(1/(3)*(radian**3))+(2/(15)*(radian**5))+(3/(40)*(radian**7))
		self.result = False
		self.display('{0:.4f}'.format(round(derettan,3)))

	# mengembalikan nilai sinus hiperbolik 
	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(float(txtResult.get())))
		self.display(self.current)

	# mengembalikan nilai cos hiperbolik 
	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(txtResult.get())))
		self.display(self.current)

	# mengembalikan nilai tan hiperbolik 
	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(float(txtResult.get())))
		self.display(self.current)

	# mengembalikan nilai logaritma 
	def log(self):
		self.result = False
		self.current = math.log(float(txtResult.get()))
		self.display(self.current)

	# mengembalikan nilai eksponen dari konstanta matematika e
	def exp(self): # secara manual tanpa bantuan modul
		self.result = False
		touchEntry = str(txtResult)
		self.current = 2.718281828459045**(float((txtResult.get())))
		self.display(self.current)

	# mengembalikan nilai inversi cos hiperbolik 
	def acosh(self):
		self.result = False
		self.current = math.acosh(float(txtResult.get()))
		self.display(self.current)

	# mengembalikan nilai inversi sinus hiperbolik 
	def asinh(self):
		self.result = False
		self.current = math.asinh(float(txtResult.get()))
		self.display(self.current)

	# mengembalikan nilai exp(X)-1
	def expm1(self):
		self.result = False
		self.current = math.expm1(float(txtResult.get()))
		self.display(self.current)

	# mengembalikan logaritma natural dari nilai mutlak fungsi gamma di sebuah angka
	def lgamma(self):
		self.result = False
		self.current = math.lgamma(float(txtResult.get()))
		self.display(self.current)

	# mengubah sudut x dari radian menjadi derajat
	def degrees(self):
		self.result = False
		self.current = math.degrees(float(txtResult.get()))
		self.display(self.current)

	# mengembalikan nilai logaritma berbasis 2
	def log2(self):
		self.result = False
		self.current = math.log2(float(txtResult.get()))
		self.display(self.current)

	# mengembalikan nilai logaritma berbasis 10
	def log10(self):
		self.result = False
		self.current = math.log10(float(txtResult.get()))
		self.display(self.current)

	# mengembalikan nilai logaritma natural 1+angka
	def log1p(self):
		self.result = False
		self.current = math.log1p(float(txtResult.get()))
		self.display(self.current)	

added_value = Calc()

# membuat kolom hasil 
txtResult = Entry(calFrame, font=('Arial',16,'bold'),
				bg='white',fg='black',
				bd=30,width=26,justify=RIGHT)
txtResult.grid(row=0,column=0, columnspan=4, pady=1)
txtResult.insert(0,"0")

# membuat tombol-tombol angka
numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
	for k in range(3):
		btn.append(Button(calFrame, width=6, height=2,
						bg='white',fg='black',
						font=('Arial',16,'bold'),
						bd=4,text=numberpad[i]))
		btn[i].grid(row=j, column= k, pady = 1)
		btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
		i+=1


# menbuat tombol-tombol operasi perhitungan pada kalkulator 
btnClear = Button(calFrame, text=chr(67),width=6,
				height=2,bg='rosybrown3',
				font=('Arial',16,'bold')
				,bd=4, command=added_value.Clear_Entry
				).grid(row=1, column= 0, pady = 1)

btnAllClear = Button(calFrame, text=chr(65) + chr(67),
					width=6, height=2,
					bg='antiquewhite3',
					font=('Arial',16,'bold'),
					bd=4,
					command=added_value.All_Clear_Entry
					).grid(row=1, column= 1, pady = 1)

btnsq = Button(calFrame, text="\u221A",width=6, height=2,
			bg='rosybrown3', font=('Arial',
									16,'bold'),
			bd=4,command=added_value.squared
			).grid(row=1, column= 2, pady = 1)

btnAdd = Button(calFrame, text="+",width=6, height=2,
				bg='antiquewhite3',
				font=('Arial',16,'bold'),
				bd=4,command=lambda:added_value.operation("add")
				).grid(row=1, column= 3, pady = 1)

btnSub = Button(calFrame, text="-",width=6,
				height=2,bg='rosybrown3',
				font=('Arial',16,'bold'),
				bd=4,command=lambda:added_value.operation("sub")
				).grid(row=2, column= 3, pady = 1)

btnMul = Button(calFrame, text="x",width=6,
				height=2,bg='antiquewhite3',
				font=('Arial',16,'bold'),
				bd=4,command=lambda:added_value.operation("multi")
				).grid(row=3, column= 3, pady = 1)

btnDiv = Button(calFrame, text="/",width=6,
				height=2,bg='rosybrown3',
				font=('Arial',16,'bold'),
				bd=4,command=lambda:added_value.operation("divide")
				).grid(row=4, column= 3, pady = 1)

btnZero = Button(calFrame, text="0",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=lambda:added_value.numberEnter(0)
				).grid(row=5, column= 0, pady = 1)

btnDot = Button(calFrame, text=".",width=6,
				height=2,bg='antiquewhite3',
				font=('Arial',16,'bold'),
				bd=4,command=lambda:added_value.numberEnter(".")
				).grid(row=5, column= 1, pady = 1)

btnPM = Button(calFrame, text=chr(177),width=6,
			height=2,bg='rosybrown3', font=('Arial',16,'bold'),
			bd=4,command=added_value.mathPM
			).grid(row=5, column= 2, pady = 1)

btnEquals = Button(calFrame, text="=",width=6,
				height=2,bg='antiquewhite3',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.sum_of_total
				).grid(row=5, column= 3, pady = 1)
# ROW 1 :
btnPi = Button(calFrame, text="π",width=6,
			height=2,bg='rosybrown3',fg='black',
			font=('Arial',16,'bold'),
			bd=4,command=added_value.pi
			).grid(row=1, column= 4, padx = 5, pady = 1)

btnCos = Button(calFrame, text="cos",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.cos
			).grid(row=1, column= 5, pady = 1)

btntan = Button(calFrame, text="tan",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.tan
			).grid(row=1, column= 6, pady = 1)

btnsin = Button(calFrame, text="sin",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.sin
			).grid(row=1, column= 7, pady = 1)

# ROW 2 :
btn2Pi = Button(calFrame, text="2π",width=6,
				height=2,bg='antiquewhite3',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.tau
			).grid(row=2, column= 4, pady = 1)

btnCosh = Button(calFrame, text="cosh",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.cosh
				).grid(row=2, column= 5, pady = 1)

btntanh = Button(calFrame, text="tanh",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.tanh
				).grid(row=2, column= 6, pady = 1)

btnsinh = Button(calFrame, text="sinh",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.sinh
				).grid(row=2, column= 7, pady = 1)

# ROW 3 :
btnlog = Button(calFrame, text="log",width=6,
				height=2,bg='rosybrown3',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.log
			).grid(row=3, column= 4, pady = 1)

btnExp = Button(calFrame, text="exp",width=6, height=2,
				bg='antiquewhite3',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.exp
			).grid(row=3, column= 5, pady = 1)

btnMod = Button(calFrame, text="mod",width=6,
				height=2,bg='rosybrown3',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=lambda:added_value.operation("mod")
				).grid(row=3, column= 6, pady = 1)

btnE = Button(calFrame, text="e",width=6,
				height=2,bg='antiquewhite3',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.e
			).grid(row=3, column= 7, pady = 1)

# ROW 4 :
btnlog10 = Button(calFrame, text="log10",width=6,
				height=2,bg='antiquewhite3',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.log10
				).grid(row=4, column= 4, pady = 1)

btnlog1p = Button(calFrame, text="log1p",width=6,
				height=2,bg='rosybrown3',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.log1p
				).grid(row=4, column= 5, pady = 1)

btnexpm1 = Button(calFrame, text="expm1",width=6,
				height=2,bg='antiquewhite3',fg='black',
				font=('Arial',16,'bold'),
				bd = 4,command=added_value.expm1
				).grid(row=4, column= 6, pady = 1)

btngamma = Button(calFrame, text="gamma",width=6,
				height=2,bg='rosybrown3',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.lgamma
				).grid(row=4, column= 7, pady = 1)
# ROW 5 :
btnlog2 = Button(calFrame, text="log2",width=6,
				height=2,bg='rosybrown3',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.log2
				).grid(row=5, column= 4, pady = 1)

btndeg = Button(calFrame, text="deg",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.degrees
			).grid(row=5, column= 5, pady = 1)

btnacosh = Button(calFrame, text="acosh",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.acosh
				).grid(row=5, column= 6, pady = 1)

btnasinh = Button(calFrame, text="asinh",width=6,
				height=2,bg='white',fg='black',
				font=('Arial',16,'bold'),
				bd=4,command=added_value.asinh
				).grid(row=5, column= 7, pady = 1)

# buat confirmation exit
def iExit():
    iExit = tkinter.messagebox.askyesno("Kalkulator Cinta <3", "Beneran nih mau keluar? Yaudah deh, semoga yang di sana segera peka ya! Dadah :D")
    if iExit > 0:
        root.destroy()
        return

# buat ke kalkulator scientific
def scientific():
    root.geometry('796x492+460+40')
    root.resizable(width=False, height=False)
    txtResult.delete(0,END)
    txtResult.delete(0,"0")
    # bikin hiasan
    lblDisplay=Label(calFrame,text="I Love You",font=('C39HrP24DhTt',60),padx=9,
                     fg='gray',justify=CENTER)
    lblDisplay.grid(row=0,column=4, columnspan=4)

# buat ke kalkulator standar
def standard():
    root.geometry('400x492+460+40')
    root.resizable(width=False, height=False)
    txtResult.delete(0,END)
    txtResult.delete(0,"0")

# buat ke love calc (side app dari kalkulator ini)
# main aplikasi
def love():
	root = Tk()
	root.title("Love Calculator")
	root.geometry("360x300")
	root.resizable(width=False, height=False)
	root.configure(background='lemonchiffon')
	lblDisplay=Label(root,text="Find Love % Between",font=('Cheri',20),padx=35,pady=10,
						bg="lemonchiffon",fg='hotpink',justify=CENTER)
	lblDisplay.grid(row=0,column=4, columnspan=4)

	# mengatur ukuran font yang digunakan
	font = tkinter.font.Font(size=16)

	# membuat frame baru untuk aplikasi
	frame = LabelFrame(root,padx=45,pady=38, relief=RIDGE)
	frame.place(x=15,y=50)
	calframe = Frame(frame, bd=50, pady=2, relief=RIDGE)
	calframe.grid()

	# membuat judul dan tulisan untuk isi aplikasi
	judul = Label(frame,text="Your name:").grid(row=0,column=0)
	judul2 = Label(frame,text="Partner's name:").grid(row=0,column=3)
	judul3 = Label(frame,text="").grid(row=0,column=2)
	samadengan = Label(frame,text="♥").grid(row=1,column=2)

	# membuat kotak untuk input nama
	a1 = Entry(frame,width=8, font =('arial',12), bg='pink')
	a2 = Entry(frame,width=8, font =('arial',12), bg='pink')
	a1.grid(row=1,column=0)
	a2.grid(row=1,column=3)

	# membuat kotak untuk hasil persentase
	space = Label(frame,text=" ").grid(row=5,column=2)
	result = Label(frame,text="Result:").grid(row=6,column=2)
	a3 = Entry(frame,width=8, font =('arial',12), bg='pink')
	a3.grid(row=7,column=2)
	persen = Label(frame,text="%")
	persen.place(x=150,y=132)

	# membuat tombol untuk menghitung persentase
	space = Label(frame,text=" ").grid(row=3,column=2)
	btn = Button(frame,text="Calculate",command=lambda:rumus("hitung"))
	btn.grid(row=4,column=2)

	# mendefinisikan rumus perhitungan 
	def rumus(rm):
		# menghapus tulisan pada kotak 3 agar autoreset
		a3.delete(0,END)
		# mendapatkan nilai dari kotak
		name1 = str(a1.get())
		name2 = str(a2.get())
		name1 = name1.lower()  
		name2 = name2.lower() 
		# menuliskan rumus hitungan
		# inisiasi variabel kunci   
		score = 0  
		vokal =["a","e","i","o","u","y"]  
		konsonan = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]  
		vowelsInName1 = 0  
		vowelsInName2 = 0  

		# rumus nilai persentase kecocokan
		# berdasarkan jumlah huruf namanya sama
		if len(name1)==len(name2):  
			score+=50
			if name1[0]==name2[0]:
				score+=13
				if name1[1]=='a' or name1[1]=='i' or name1[1]=='u' or name1[1]=='e' or name1[1]=='o':
					score+=30
					if name2[1]=='a' or name2[1]=='i' or name2[1]=='u' or name2[1]=='e' or name2[1]=='o':
						score+=20
				elif name1[-1]==name2[-1]:
					score+= 37
			elif name1[-1]==name2[-1]:
				score+=16
				if name1[1]=='a' or name1[1]=='i' or name1[1]=='u' or name1[1]=='e' or name1[1]=='o':
					score+=30
				elif name2[1]=='a' or name2[1]=='i' or name2[1]=='u' or name2[1]=='e' or name2[1]=='o':
					score+= 20
		# berdasarkan jumlah huruf nama pertama lebih kecil dari nama kedua
		elif len(name1)<len(name2):
			score+=33
			if name1[0]==name2[0]:
				score+=14
				if name1[1]=='a' or name1[1]=='i' or name1[1]=='u' or name1[1]=='e' or name1[1]=='o':
					score+=30
					if name2[1]=='a' or name2[1]=='i' or name2[1]=='u' or name2[1]=='e' or name2[1]=='o':
						score+=20
				elif name1[-1]==name2[-1]:
					score+= 39
			elif name1[-1]==name2[-1]:
				score+=17
		# berdasarkan jumlah huruf nama pertama lebih besar dari nama kedua
		elif len(name1)>len(name2):
			score+=29
			if name1[0]==name2[0]:
				score+=14
				if name1[1]=='a' or name1[1]=='i' or name1[1]=='u' or name1[1]=='e' or name1[1]=='o':
					score+=30
				elif name2[1]=='a' or name2[1]=='i' or name2[1]=='u' or name2[1]=='e' or name2[1]=='o':
					score+=20
					if name1[-1]==name2[-1]:
						score+= 40
			elif name1[1]=='a' or name1[1]=='i' or name1[1]=='u' or name1[1]=='e' or name1[1]=='o':
				score+=30
				if name2[1]=='a' or name2[1]=='i' or name2[1]=='u' or name2[1]=='e' or name2[1]=='o':
					score+=20
			elif name1[-1]==name2[-1]:
				score+=17   
		
		# output hasil akhir
		hasil = score
		a3.insert(0, hasil)

# membuat menu-menu options untuk menuju fitur-fitur yang ada pada kalkulator
menubar = Menu(calFrame)

filemenu= Menu(menubar, tearoff=0)
menubar.add_cascade(label='Options', menu=filemenu)
filemenu.add_command(label='Standard', command=standard)
filemenu.add_separator()
filemenu.add_command(label='Scientific', command=scientific)
filemenu.add_separator()
filemenu.add_command(label='Love', command=love)  
filemenu.add_separator()
filemenu.add_command(label='Exit', command=iExit)

root.config(menu=menubar)

# eksekusi 
root.mainloop()