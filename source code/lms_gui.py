from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import os

def reset(x):
    for child in x.winfo_children():
        child.destroy()
def home():
	tmsg.showinfo("Home","Thanx for using this software ....\nwe are working on home function.When we are done we will let you know.....")
def about():
	tmsg.showinfo("About","This Software is designed by\nShivshanker Singh")
def help1():
	tmsg.showinfo('Help','Please let us know about your problem we will respond as soon as possible\nemail us at...\nshiv71290@gmail.com')
def logt():
	a=tmsg.askquestion("Log Out","Press Yes to Log Out and close the program")
	if a=="yes":
		exit()
def menubar():
	mymenu=Menu(root)

	mymenu.add_command(label='Home',command=home)
	mymenu.add_command(label='About',command=about)
	mymenu.add_command(label='Help!',command=help1)
	mymenu.add_command(label='Log Out',command=logt)
	root.config(menu=mymenu)

def search_book():
	tmsg.showinfo("Home","Thanx for using this software ....\nwe are working on this function.When we are done we will let you know.....")
def book_list():
	tmsg.showinfo("Home","Thanx for using this software ....\nwe are working on this function.When we are done we will let you know.....")
def profile():
	tmsg.showinfo("Home","Thanx for using this software ....\nwe are working on this function.When we are done we will let you know.....")
def admin_profile():
	reset(root)
	menubar()
	Label(text="Admin Profile",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
	Label(text="Name    :").place(x=320,y=200)
	Label(text="Roll No :").place(x=320,y=240)
	Label(text="Branch  :").place(x=320,y=280)
	Label(text="Mobile  :").place(x=320,y=320)
	Label(text="Email   :").place(x=320,y=360)
	Label(text="Section :").place(x=320,y=400)
	Label(text="Semester:").place(x=320,y=440)
	Label(text="College :").place(x=320,y=480)

	Label(text="Shivshanker Singh Solanki").place(x=400,y=200)
	Label(text="1811010051").place(x=400,y=240)
	Label(text="Computer Science & Engineering").place(x=400,y=280)
	Label(text="+91 80*****33, +91 82******00").place(x=400,y=320)
	Label(text="shiv71290@gmail.com").place(x=400,y=360)
	Label(text="A2").place(x=400,y=400)
	Label(text="3").place(x=400,y=440)
	Label(text="Institute of Enggineering & Rural Technology, Prayagraj").place(x=400,y=480)

	Button(text="Back",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_menu).place(x=320,y=520)
	Button(text="Exit",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=575,y=520)

def admin_delete_student():
	reset(root)
	menubar()

	def back():
		admin_manage_student()

	def delete():
		f=open("student_data.DAT")
		f2=open("temp.DAT",'a+')
		while 1:
			content=f.readline()
			if content=='':
				break
			content=eval(content)
			if content['roll_no']!=roll_no1.get():
				f2.write(str(content))
				f2.write("\n")
		f.close()
		f2.close()
		os.remove("student_data.DAT")
		os.rename(r"temp.DAT",r"student_data.DAT")
		tmsg.showinfo("Delete Student","Student Data Deleted Successfully")
		admin_manage_student()
	def view_profile(std):
		reset(root)
		menubar()
		Label(text="Student Profile",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
		Label(text="Name     :").place(x=340,y=200)
		Label(text="Roll No  :").place(x=340,y=240)
		Label(text="Branch   :").place(x=340,y=280)
		Label(text="Semester:").place(x=340,y=320)
		Label(text="Admission Year:").place(x=300,y=360)
		Label(text="Mobile  :").place(x=348,y=400)
		Label(text="Email  :").place(x=348,y=440)

		Label(text=std['name']).place(x=430,y=200)
		Label(text=std['roll_no']).place(x=430,y=240)
		Label(text=std['branch']).place(x=430,y=280)
		Label(text=std['sem']).place(x=430,y=320)
		Label(text=std['session']).place(x=430,y=360)
		Label(text=std['mobile']).place(x=430,y=400)
		Label(text=std['email']).place(x=430,y=440)
		Button(text="Cancel",width=15,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=340,y=500)
		Button(text="Delete",width=15,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=delete).place(x=560,y=500)


	def profile():
		f=open("student_data.DAT")
		while 1:
			content=f.readline()
			if content=='':
				break
			content=eval(content)
			if content['roll_no']==roll_no1.get():
				f.close()
				view_profile(content)
		f.close()
		tmsg.showinfo("No Data Found","This Roll number is not available in database please check the roll number and try again")



	roll_no1=StringVar()
	Label(root,text="Delete Student",font=("lucida",20,"bold"),bg="yellow",fg="blue",relief=RAISED,borderwidth=5).place(x=530,y=50)
	Label(root,text="Enter Roll Number:").place(x=550,y=230)
	Entry(root,textvariable=roll_no1).place(x=550,y=250)
	Button(text="Delete",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=profile).place(x=650,y=300)
	Button(text="Back",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=540,y=300)


def admin_add_book():
	reset(root)
	menubar()
	def add_book_data():
		book['title']=title1.get()
		book['author']=author1.get()
		book['publisher']=publisher1.get()
		book['isbn']=isbn1.get()
		book['catagory']=catagory1.get()
		book['pub_year']=pub_year1.get()
		book['total_copies']=book['avl_copies']=total_copies1.get()
		flag=0
		try:
			f=open("book_data.DAT")
			while 1:
				content=f.readline()
				if content=='':
					break
				content=eval(content)
				if content['isbn']==book['isbn']:
					tmsg.showinfo("Existing ISBN Number","This book ISBN already exists please enter again")
					f.close()
					flag+=1
					break
		except FileNotFoundError:
			flag=0
		if flag==0:
			f1=open("book_data.DAT",'a+')
			f1.write(str(book))
			f1.write("\n")
			f1.close()
			a=tmsg.askquestion("Add Book","Book data saved successfully\nWant to add another Book")
			if a=="yes":
				admin_add_book()
			else:
				admin_manage_books()
	book={'title':'','author':'','publisher':'','isbn':'','catagory':'','pub_year':'','avl_copies':'','total_copies':''}

	Label(root,text="Add Book",font=("lucida",20,"bold")).place(x=530,y=50)
	Label(root,text="Title:").place(x=475,y=150)
	Label(root,text="Author:").place(x=470,y=200)
	Label(root,text="Publisher:").place(x=465,y=250)
	Label(root,text="ISBN:").place(x=465,y=300)
	Label(root,text="Catagory:").place(x=450,y=350)
	Label(root,text="Publication Year:").place(x=425,y=400)
	Label(root,text="Total Copies:").place(x=450,y=450)
	list0=["Computer Science & Engineering",
			"Electronics",
			"Mechanical",
			"Civil",
			"Electrical",
			"IP",
			"IC",
			"Other"
			]
	title1=StringVar()
	author1=StringVar()
	publisher1=StringVar()
	isbn1=StringVar()
	catagory1=StringVar()
	pub_year1=StringVar()
	catagory1.set("Select Department")
	total_copies1=StringVar()
	Entry(root,textvariable=title1).place(x=540,y=150)
	Entry(root,textvariable=author1).place(x=540,y=200)
	Entry(root,textvariable=publisher1).place(x=540,y=250)
	Entry(root,textvariable=isbn1).place(x=540,y=300)
	OptionMenu(root,catagory1,*list0).place(x=540,y=350)
	Entry(root,textvariable=pub_year1).place(x=540,y=400)
	Entry(root,textvariable=total_copies1).place(x=540,y=450)

	Button(text="Back",width=8,bg="blue",fg="yellow",borderwidth=5,font=("lucida",13,"bold"),command=admin_manage_books).place(x=450,y=500)
	Button(text="Submit",width=8,bg="blue",borderwidth=5,fg="yellow",font=("lucida",13,"bold"),command=add_book_data).place(x=640,y=500)


def admin_search_book():
	reset(root)
	menubar()

	def back():
		admin_manage_books()
	def view_profile(book):
		reset(root)
		menubar()
		Label(text="Search Book",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
		Label(text="Title:").place(x=465,y=200)
		Label(text="Author:").place(x=460,y=240)
		Label(text="Publisher:").place(x=450,y=280)
		Label(text="ISBN:").place(x=465,y=320)
		Label(text="Publication Year:").place(x=400,y=360)
		Label(text="Available Copies:").place(x=400,y=400)
		Label(text="Total Copies:").place(x=420,y=440)

		Label(text=book['title']).place(x=530,y=200)
		Label(text=book['author']).place(x=530,y=240)
		Label(text=book['publisher']).place(x=530,y=280)
		Label(text=book['isbn']).place(x=530,y=320)
		Label(text=book['pub_year']).place(x=530,y=360)
		Label(text=book['avl_copies']).place(x=530,y=400)
		Label(text=book['total_copies']).place(x=530,y=440)
		Button(text="Back",width=15,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=520,y=470)

	def profile():
		f=open("book_data.DAT")
		flag=0
		while 1:
			content=f.readline()
			if content=='':
				break
			content=eval(content)
			if content['isbn']==isbn1.get():
				f.close()
				view_profile(content)
				flag+=1
				break
		if flag==0:
			f.close()
			tmsg.showinfo("No Data Found","This ISBN number is not available in database please check the ISBN number and try again")

	isbn1=StringVar()
	Label(root,text="Search Book",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
	Label(root,text="Enter ISBN Number:").place(x=540,y=210)
	Entry(root,textvariable=isbn1).place(x=540,y=230)
	Button(text="Search",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=profile).place(x=630,y=300)
	Button(text="Back",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=520,y=300)

	
def admin_manage_books():
	#tmsg.showinfo("Home","Thanx for using this software ....\nwe are working on this function.When we are done we will let you know.....")
	reset(root)
	menubar()
	Label(root,text="Manage Books",width=15,font=("lucida",20,"bold")).place(x=530,y=50)
	Button(text="Add Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_add_book).place(x=400,y=200)
	Button(text="Edit Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=400,y=250)
	Button(text="Remove Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=400,y=300)
	Button(text="Search Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_search_book).place(x=400,y=350)
	Button(text="Book List",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=400,y=400)

	Button(text="Issue Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=750,y=200)
	Button(text="Submit Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=750,y=250)
	Button(text="Issued Books",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=750,y=300)
	Button(text="Submitted Books",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=750,y=350)
	Button(text="Back",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_menu).place(x=750,y=400)
	Button(text="Exit",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=575,y=470)


def librarian_search_book():
	reset(root)
	menubar()

	def back():
		librarian_manage_books()
	def view_profile(book):
		reset(root)
		menubar()
		Label(text="Search Book",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
		Label(text="Title:").place(x=465,y=200)
		Label(text="Author:").place(x=460,y=240)
		Label(text="Publisher:").place(x=450,y=280)
		Label(text="ISBN:").place(x=465,y=320)
		Label(text="Publication Year:").place(x=400,y=360)
		Label(text="Available Copies:").place(x=400,y=400)
		Label(text="Total Copies:").place(x=420,y=440)

		Label(text=book['title']).place(x=530,y=200)
		Label(text=book['author']).place(x=530,y=240)
		Label(text=book['publisher']).place(x=530,y=280)
		Label(text=book['isbn']).place(x=530,y=320)
		Label(text=book['pub_year']).place(x=530,y=360)
		Label(text=book['avl_copies']).place(x=530,y=400)
		Label(text=book['total_copies']).place(x=530,y=440)
		Button(text="Back",width=15,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=520,y=470)

	def profile():
		f=open("book_data.DAT")
		flag=0
		while 1:
			content=f.readline()
			if content=='':
				break
			content=eval(content)
			if content['isbn']==isbn1.get():
				f.close()
				view_profile(content)
				flag+=1
				break
		if flag==0:
			f.close()
			tmsg.showinfo("No Data Found","This ISBN number is not available in database please check the ISBN number and try again")

	isbn1=StringVar()
	Label(root,text="Search Book",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
	Label(root,text="Enter ISBN Number:").place(x=540,y=210)
	Entry(root,textvariable=isbn1).place(x=540,y=230)
	Button(text="Search",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=profile).place(x=630,y=300)
	Button(text="Back",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=520,y=300)


def librarian_add_book():
	reset(root)
	menubar()
	def add_book_data():
		book['title']=title1.get()
		book['author']=author1.get()
		book['publisher']=publisher1.get()
		book['isbn']=isbn1.get()
		book['catagory']=catagory1.get()
		book['pub_year']=pub_year1.get()
		book['total_copies']=book['avl_copies']=total_copies1.get()
		flag=0
		try:
			f=open("book_data.DAT")
			while 1:
				content=f.readline()
				if content=='':
					break
				content=eval(content)
				if content['isbn']==book['isbn']:
					tmsg.showinfo("Existing ISBN Number","This book ISBN already exists please enter again")
					f.close()
					flag+=1
					break
		except FileNotFoundError:
			flag=0
		if flag==0:
			f1=open("book_data.DAT",'a+')
			f1.write(str(book))
			f1.write("\n")
			f1.close()
			a=tmsg.askquestion("Add Book","Book data saved successfully\nWant to add another Book")
			if a=="yes":
				librarian_add_book()
			else:
				librarian_manage_books()
	book={'title':'','author':'','publisher':'','isbn':'','catagory':'','pub_year':'','avl_copies':'','total_copies':''}

	Label(root,text="Add Book",font=("lucida",20,"bold")).place(x=530,y=50)
	Label(root,text="Title:").place(x=475,y=150)
	Label(root,text="Author:").place(x=470,y=200)
	Label(root,text="Publisher:").place(x=465,y=250)
	Label(root,text="ISBN:").place(x=465,y=300)
	Label(root,text="Catagory:").place(x=450,y=350)
	Label(root,text="Publication Year:").place(x=425,y=400)
	Label(root,text="Total Copies:").place(x=450,y=450)
	list0=["Computer Science & Engineering",
			"Electronics",
			"Mechanical",
			"Civil",
			"Electrical",
			"IP",
			"IC",
			"Other"
			]
	title1=StringVar()
	author1=StringVar()
	publisher1=StringVar()
	isbn1=StringVar()
	catagory1=StringVar()
	pub_year1=StringVar()
	catagory1.set("Select Department")
	total_copies1=StringVar()
	Entry(root,textvariable=title1).place(x=540,y=150)
	Entry(root,textvariable=author1).place(x=540,y=200)
	Entry(root,textvariable=publisher1).place(x=540,y=250)
	Entry(root,textvariable=isbn1).place(x=540,y=300)
	OptionMenu(root,catagory1,*list0).place(x=540,y=350)
	Entry(root,textvariable=pub_year1).place(x=540,y=400)
	Entry(root,textvariable=total_copies1).place(x=540,y=450)

	Button(text="Back",width=8,bg="blue",fg="yellow",borderwidth=5,font=("lucida",13,"bold"),command=librarian_manage_books).place(x=450,y=500)
	Button(text="Submit",width=8,bg="blue",borderwidth=5,fg="yellow",font=("lucida",13,"bold"),command=add_book_data).place(x=640,y=500)



def librarian_manage_books():
	#tmsg.showinfo("Home","Thanx for using this software ....\nwe are working on this function.When we are done we will let you know.....")
	reset(root)
	menubar()
	Label(root,text="Manage Books",width=15,font=("lucida",20,"bold")).place(x=530,y=50)
	Button(text="Add Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=librarian_add_book).place(x=400,y=200)
	Button(text="Edit Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=400,y=250)
	Button(text="Remove Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=400,y=300)
	Button(text="Search Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=librarian_search_book).place(x=400,y=350)
	Button(text="Book List",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=400,y=400)

	Button(text="Issue Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=750,y=200)
	Button(text="Submit Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=750,y=250)
	Button(text="Issued Books",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=750,y=300)
	Button(text="Submitted Books",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=750,y=350)
	Button(text="Back",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=librarian_menu).place(x=750,y=400)
	Button(text="Exit",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=575,y=470)

def librarian_add_student():
	reset(root)
	menubar()

	def add_student_data():
		student['name']=name1.get()
		student['roll_no']=roll_no1.get()
		student['mobile']=mobile1.get()
		student['email']=email1.get()
		student['branch']=branch1.get()
		student['sem']=sem1.get()
		student['session']=session1.get()
		student['password']=student['name'][:4]+student['mobile'][:4]

		flag=0
		try:
			f=open("student_data.DAT")
			while 1:
				content=f.readline()
				if content=='':
					break
				content=eval(content)
				if content['roll_no']==student['roll_no']:
					tmsg.showinfo("Existing Roll Number","This roll number already exists please enter again")
					f.close()
					flag+=1
					break
		except FileNotFoundError:
			flag=0
		if flag==0:
			f1=open("student_data.DAT",'a+')
			f1.write(str(student))
			f1.write("\n")
			f1.close()
			a=tmsg.askquestion("Add Student","Student data saved successfully\nWant to add another student")
			if a=="yes":
				admin_add_student()
			else:
				admin_manage_student()
	student={'name':'','roll_no':'','mobile':'','email':'','branch':'','sem':'','session':''}

	Label(root,text="Add Student",font=("lucida",20,"bold")).place(x=530,y=50)
	Label(root,text="       Name:").place(x=450,y=150)
	Label(root,text="     Roll No:").place(x=450,y=200)
	Label(root,text="     Mobile:").place(x=450,y=250)
	Label(root,text="      Email:").place(x=450,y=300)
	Label(root,text="     Branch:").place(x=450,y=350)
	Label(root,text="Semester:").place(x=450,y=400)
	Label(root,text="Admission Year:").place(x=410,y=450)
	list0=["Computer Science & Engineering",
			"Electronics",
			"Mechanical",
			"Civil",
			"Electrical",
			"IP",
			"IC"
			]
	list1=["1","2","3","4","5","6","7","8"]
	name1=StringVar()
	roll_no1=StringVar()
	mobile1=StringVar()
	email1=StringVar()
	branch1=StringVar()
	branch1.set("Select Branch")
	sem1=StringVar()
	sem1.set("select Semester")
	session1=StringVar()
	Entry(root,textvariable=name1).place(x=540,y=150)
	Entry(root,textvariable=roll_no1).place(x=540,y=200)
	Entry(root,textvariable=mobile1).place(x=540,y=250)
	Entry(root,textvariable=email1).place(x=540,y=300)
	OptionMenu(root,branch1,*list0).place(x=540,y=350)
	OptionMenu(root,sem1,*list1).place(x=540,y=400)
	Entry(root,textvariable=session1).place(x=540,y=450)

	Button(text="Back",width=8,bg="blue",fg="yellow",borderwidth=5,font=("lucida",13,"bold"),command=librarian_manage_student).place(x=450,y=500)
	Button(text="Submit",width=8,bg="blue",borderwidth=5,fg="yellow",font=("lucida",13,"bold"),command=add_student_data).place(x=640,y=500)

def librarian_view_student():
	reset(root)
	menubar()

	def back():
		librarian_manage_student()
	def view_profile(std):
		reset(root)
		menubar()
		Label(text="Student Profile",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
		Label(text="Name     :").place(x=440,y=200)
		Label(text="Roll No  :").place(x=440,y=240)
		Label(text="Branch   :").place(x=440,y=280)
		Label(text="Semester:").place(x=440,y=320)
		Label(text="Admission Year:").place(x=400,y=360)
		Label(text="Mobile  :").place(x=448,y=400)
		Label(text="Email  :").place(x=448,y=440)

		Label(text=std['name']).place(x=530,y=200)
		Label(text=std['roll_no']).place(x=530,y=240)
		Label(text=std['branch']).place(x=530,y=280)
		Label(text=std['sem']).place(x=530,y=320)
		Label(text=std['session']).place(x=530,y=360)
		Label(text=std['mobile']).place(x=530,y=400)
		Label(text=std['email']).place(x=530,y=440)
		Button(text="Back",width=15,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=520,y=470)

	def profile():
		f=open("student_data.DAT")
		flag=0
		while 1:
			content=f.readline()
			if content=='':
				break
			content=eval(content)
			if content['roll_no']==roll_no1.get():
				f.close()
				view_profile(content)
				flag+=1
				break
		if flag==0:
			f.close()
			tmsg.showinfo("No Data Found","This Roll number is not available in database please check the roll number and try again")

	roll_no1=StringVar()
	Label(root,text="Student Profile",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
	Label(root,text="Enter Roll Number:").place(x=540,y=210)
	Entry(root,textvariable=roll_no1).place(x=540,y=230)
	Button(text="Search",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=profile).place(x=630,y=300)
	Button(text="Back",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=520,y=300)


def admin_view_student():
	reset(root)
	menubar()

	def back():
		admin_manage_student()
	def view_profile(std):
		reset(root)
		menubar()
		Label(text="Student Profile",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
		Label(text="Name     :").place(x=440,y=200)
		Label(text="Roll No  :").place(x=440,y=240)
		Label(text="Branch   :").place(x=440,y=280)
		Label(text="Semester:").place(x=440,y=320)
		Label(text="Admission Year:").place(x=400,y=360)
		Label(text="Mobile  :").place(x=448,y=400)
		Label(text="Email  :").place(x=448,y=440)

		Label(text=std['name']).place(x=530,y=200)
		Label(text=std['roll_no']).place(x=530,y=240)
		Label(text=std['branch']).place(x=530,y=280)
		Label(text=std['sem']).place(x=530,y=320)
		Label(text=std['session']).place(x=530,y=360)
		Label(text=std['mobile']).place(x=530,y=400)
		Label(text=std['email']).place(x=530,y=440)
		Button(text="Back",width=15,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=520,y=470)


	def profile():
		f=open("student_data.DAT")
		flag=0
		while 1:
			content=f.readline()
			if content=='':
				break
			content=eval(content)
			if content['roll_no']==roll_no1.get():
				f.close()
				view_profile(content)
				flag+=1
				break
		if flag==0:
			f.close()
			tmsg.showinfo("No Data Found","This Roll number is not available in database please check the roll number and try again")
		
	roll_no1=StringVar()
	Label(root,text="Student Profile",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=60)
	Label(root,text="Enter Roll Number:").place(x=540,y=210)
	Entry(root,textvariable=roll_no1).place(x=540,y=230)
	Button(text="Search",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=profile).place(x=630,y=300)
	Button(text="Back",width=5,borderwidth=5,font=("Lucida",13,"bold"),bg='blue',fg='yellow',command=back).place(x=520,y=300)

def admin_add_student():
	reset(root)
	menubar()

	def add_student_data():
		student['name']=name1.get()
		student['roll_no']=roll_no1.get()
		student['mobile']=mobile1.get()
		student['email']=email1.get()
		student['branch']=branch1.get()
		student['sem']=sem1.get()
		student['session']=session1.get()
		student['password']=student['name'][:4]+student['mobile'][:4]
		flag=0
		try:
			f=open("student_data.DAT")
			while 1:
				content=f.readline()
				if content=='':
					break
				content=eval(content)
				if content['roll_no']==student['roll_no']:
					tmsg.showinfo("Existing Roll Number","This roll number already exists please enter again")
					f.close()
					flag+=1
					break
		except FileNotFoundError:
			flag=0
		if flag==0:
			f1=open("student_data.DAT",'a+')
			f1.write(str(student))
			f1.write("\n")
			f1.close()
			a=tmsg.askquestion("Add Student","Student data saved successfully\nWant to add another student")
			if a=="yes":
				admin_add_student()
			else:
				admin_manage_student()
	student={'name':'','roll_no':'','mobile':'','email':'','branch':'','sem':'','session':''}

	Label(root,text="Add Student",font=("lucida",20,"bold")).place(x=530,y=50)
	Label(root,text="       Name:").place(x=450,y=150)
	Label(root,text="     Roll No:").place(x=450,y=200)
	Label(root,text="     Mobile:").place(x=450,y=250)
	Label(root,text="      Email:").place(x=450,y=300)
	Label(root,text="     Branch:").place(x=450,y=350)
	Label(root,text="Semester:").place(x=450,y=400)
	Label(root,text="Admission Year:").place(x=410,y=450)
	list0=["Computer Science & Engineering",
			"Electronics",
			"Mechanical",
			"Civil",
			"Electrical",
			"IP",
			"IC"
			]
	list1=["1","2","3","4","5","6","7","8"]
	name1=StringVar()
	roll_no1=StringVar()
	mobile1=StringVar()
	email1=StringVar()
	branch1=StringVar()
	branch1.set("Select Branch")
	sem1=StringVar()
	sem1.set("select Semester")
	session1=StringVar()
	Entry(root,textvariable=name1).place(x=540,y=150)
	Entry(root,textvariable=roll_no1).place(x=540,y=200)
	Entry(root,textvariable=mobile1).place(x=540,y=250)
	Entry(root,textvariable=email1).place(x=540,y=300)
	OptionMenu(root,branch1,*list0).place(x=540,y=350)
	OptionMenu(root,sem1,*list1).place(x=540,y=400)
	Entry(root,textvariable=session1).place(x=540,y=450)

	Button(text="Back",width=8,bg="blue",fg="yellow",borderwidth=5,font=("lucida",13,"bold"),command=admin_manage_student).place(x=450,y=500)
	Button(text="Submit",width=8,bg="blue",borderwidth=5,fg="yellow",font=("lucida",13,"bold"),command=add_student_data).place(x=640,y=500)

def add_librarian():
	reset(root)
	menubar()
	def add_librarian_data():
		librarian['name']=name1.get()
		librarian['mobile']=mobile1.get()
		librarian['email']=email1.get()
		librarian['password']=librarian['name'][:4]+librarian['mobile'][:4]
		
		f1=open("librarian_data.DAT",'a+')
		f1.write(str(librarian))
		f1.write("\n")
		f1.close()
		a=tmsg.askquestion("Add Librarian","Librarian data saved successfully\nWant to add another student")
		if a=="yes":
			add_librarian()
		else:
			manage_librarian()


	Label(root,text="Add Librarian",font=("lucida",20,"bold")).place(x=530,y=50)
	Label(root,text="Name:").place(x=550,y=150)
	Label(root,text="Mobile:").place(x=550,y=225)
	Label(root,text="Email:").place(x=550,y=300)
	name1=StringVar()
	mobile1=StringVar()
	email1=StringVar()
	Entry(root,textvariable=name1).place(x=550,y=175)
	Entry(root,textvariable=mobile1).place(x=550,y=250)
	Entry(root,textvariable=email1).place(x=550,y=325)

	Button(text="Back",width=8,bg="blue",fg="yellow",borderwidth=5,font=("lucida",13,"bold"),command=manage_librarian).place(x=500,y=400)
	Button(text="Submit",width=8,bg="blue",borderwidth=5,fg="yellow",font=("lucida",13,"bold"),command=add_librarian_data).place(x=650,y=400)


def manage_librarian():
	#tmsg.showinfo("Home","Thanx for using this software ....\nwe are working on this function.When we are done we will let you know.....")
	reset(root)
	menubar()
	Label(root,text="Manage Librarian",width=17,font=("lucida",20,"bold")).place(x=530,y=50)
	Button(text="Add Librarian",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=add_librarian).place(x=575,y=200)
	Button(text="Edit Librarian Details",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=575,y=250)
	Button(text="Remove Librarian",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=575,y=300)
	Button(text="Search Librarian",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=575,y=350)
	Button(text="Librarian List",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=575,y=400)
	Button(text="Back",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_menu).place(x=575,y=450)
	Button(text="Exit",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=575,y=520)

def admin_manage_student():
	#tmsg.showinfo("Home","Thanx for using this software ....\nwe are working on this function.When we are done we will let you know.....")
	reset(root)
	menubar()
	backfunc="manage_student"
	Label(root,text="Manage Student",width=17,font=("lucida",20,"bold")).place(x=530,y=50)
	Button(text="Add Student",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_add_student).place(x=575,y=200)
	Button(text="Edit Student Details",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=575,y=250)
	Button(text="Remove Student",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_delete_student).place(x=575,y=300)
	Button(text="Search Student",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_view_student).place(x=575,y=350)
	Button(text="Student List",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=575,y=400)
	Button(text="Back",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_menu).place(x=575,y=450)
	Button(text="Exit",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=575,y=520)

def librarian_manage_student():
	#tmsg.showinfo("Home","Thanx for using this software ....\nwe are working on this function.When we are done we will let you know.....")
	reset(root)
	menubar()
	Label(root,text="Manage Student",width=17,font=("lucida",20,"bold")).place(x=530,y=50)
	Button(text="Add Student",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=librarian_add_student).place(x=575,y=200)
	Button(text="Edit Student Details",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=575,y=250)
	Button(text="Remove Student",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=575,y=300)
	Button(text="Search Student",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=librarian_view_student).place(x=575,y=350)
	Button(text="Student List",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow').place(x=575,y=400)
	Button(text="Back",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=librarian_menu).place(x=575,y=450)
	Button(text="Exit",width=17,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=575,y=520)

def admin_menu():
	reset(root)
	menubar()
	Label(root,text="Admin Section",font=("lucida",20,"bold")).place(x=530,y=50)
	Button(text="View Profile",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_profile).place(x=550,y=200)
	Button(text="Manage Books",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_manage_books).place(x=550,y=250)
	Button(text="Manage Librarian",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=manage_librarian).place(x=550,y=300)
	Button(text="Manage Student",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_manage_student).place(x=550,y=350)
	Button(text="Change Password",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=search_book).place(x=550,y=400)
	Button(text="Exit",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=550,y=450)
	#Button(text="\tBack\t",borderwidth=5,width=15,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=search_book).place(x=550,y=400)
def librarian_menu():
	reset(root)
	menubar()
	Label(root,text="Librarian Section",font=("lucida",20,"bold")).place(x=530,y=50)
	Button(text="View Profile",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=profile).place(x=550,y=200)
	Button(text="Manage Books",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=librarian_manage_books).place(x=550,y=250)
	Button(text="Manage Student",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=librarian_manage_student).place(x=550,y=300)	
	Button(text="Change Password",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=search_book).place(x=550,y=350)
	Button(text="Exit",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=550,y=450)
def student_menu():
	reset(root)
	menubar()
	Label(root,text="Student Section",font=("lucida",20,"bold")).place(x=530,y=50)
	Button(text="View Profile",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=profile).place(x=550,y=200)
	Button(text="Book List",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=book_list).place(x=550,y=250)
	# Button(text="My Books",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=manage_librarian).place(x=550,y=300)
	Button(text="Search Book",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=search_book).place(x=550,y=300)
	Button(text="Change Password",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=search_book).place(x=550,y=350)
	Button(text="Exit",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=550,y=450)
def admin_login():
	
	def login():
		uid=userid.get()
		paswd=password.get()
		#print(uid,paswd)
		if(uid=="" and paswd==""):
			admin_menu()
		else :
			Label(root,text="*Incorrect Username \nor Password",fg='red').place(x=720,y=200)


	reset(root)
	root.geometry("1366x768")
	menubar()
	Label(root,text="Admin Section",font=("lucida",20,"bold")).place(x=530,y=50)
	#image=Image.open("right.jpeg")
	#photo=ImageTk.PhotoImage(image)
	#Label(root,image=photo).place(x=0,y=0)
	Label(root,text="Enter Login Details",font=("lucida",10,"bold")).place(x=550,y=150)
	Label(root,text="Username:").place(x=550,y=180)
	Label(root,text="Password:").place(x=550,y=250)
	userid=StringVar()
	password=StringVar()

	Entry(root,textvariable=userid).place(x=550,y=200)
	Entry(root,textvariable=password,show="*").place(x=550,y=270)
	Button(root,text="Login",width=10,borderwidth=5,command=login).place(x=550,y=320)

def librarian_login():
	def login():
		uid=userid.get()
		paswd=password.get()
		#print(uid,paswd)
		if(uid=="Shiv" and paswd=="shiv@123"):
			librarian_menu()
		else :
			Label(root,text="*Incorrect Username \nor Password",fg='red').place(x=720,y=200)


	reset(root)
	root.geometry("1366x768")
	menubar()
	Label(root,text="Librarian Section",font=("lucida",20,"bold")).place(x=530,y=50)
	Label(root,text="Enter Login Details",font=("lucida",10,"bold")).place(x=550,y=150)
	Label(root,text="Username:").place(x=550,y=180)
	Label(root,text="Password:").place(x=550,y=250)
	userid=StringVar()
	password=StringVar()

	Entry(root,textvariable=userid).place(x=550,y=200)
	Entry(root,textvariable=password,show="*").place(x=550,y=270)
	Button(root,text="Login",width=10,borderwidth=5,command=login).place(x=550,y=320)

def student_login():
	def login():
		uid=userid.get()
		paswd=password.get()
		#print(uid,paswd)
		if(uid=="Shiv" and paswd=="shiv@123"):
			student_menu()
		else :
			Label(root,text="*Incorrect Username \nor Password",fg='red').place(x=720,y=200)


	reset(root)
	root.geometry("1366x768")
	menubar()
	Label(root,text="Student Section",font=("lucida",20,"bold")).place(x=530,y=50)
	Label(root,text="Enter Login Details",font=("lucida",10,"bold")).place(x=550,y=150)
	Label(root,text="Roll Number:").place(x=550,y=180)
	Label(root,text="Password:").place(x=550,y=250)
	userid=StringVar()
	password=StringVar()

	Entry(root,textvariable=userid).place(x=550,y=200)
	Entry(root,textvariable=password,show="*").place(x=550,y=270)
	Button(root,text="Login",width=10,borderwidth=5,command=login).place(x=550,y=320)


root=Tk()
root.geometry("1366x768")
root.minsize(400,400)
root.title("Library Management System")
menubar()
student={'name':'','roll_no':'','mobile':'','email':'','branch':'','sem':'','session':'','password':''}
librarian={'name':'','mobile':'','email':'','password':''}
image=Image.open("side.jpg")
photo=ImageTk.PhotoImage(image)
Label(root,image=photo).pack()
Label(text="Select One Option",width=15,font=("lucida",15,"bold"),padx=15,pady=10,bg='yellow',fg='blue',bd=3,relief=RAISED).place(x=540,y=190)
Button(text="Admin Login",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=admin_login).place(x=550,y=250)
Button(text="Librarian Login",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=librarian_login).place(x=550,y=300)
Button(text="Student Login",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='blue',fg='yellow',command=student_login).place(x=550,y=350)
Button(text="Exit",width=15,borderwidth=5,font=("lucida",13,"bold"),bg='red',fg='yellow',command=quit).place(x=550,y=450)
root.mainloop()