import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd=" ",database="project")
cursor=con.cursor()
L=[]
M=[]
bookname,autname,pubname,cost,isbn,btype,date_entry,total_copies,available_no,book_id,lent_
copy,ret_copy,fine,borrow="","","",0,0,"","",0,0,"",0,0,0,""
status=""
borrowpendret=""
dateborrow=""
dateret=""
query="select * from book"
cursor.execute(query)
data=cursor.fetchall()
for i in data:
 L.append(i[0])
query="select * from STUDENT"
cursor.execute(query)
data=cursor.fetchall()
for i in data:
 M.append(i[0])
def Admin_Login(n):
 c=int(input("Choose desired acƟon. \n1.Adding Books \n2.UpdaƟng Books \n3.DeleƟng Books
\n4.Add User \n5.Book Details \n6.UpdaƟng fine of a user \n7.Search a Book Available \n8.User 
Details \n9.Add a New Password \n10.Delete a user \n11.Update a pending status"))
 if c==1:
 Add_Books()
 elif c==2:
 Update_Books()
 elif c==3:
 Delete_Books()
 elif c==4:
 Add_User()
 elif c==5:
 Book_Details()
 elif c==6:
 Fine()
 elif c==7:
 Search_Books()
 elif c==8:
 User_Details("Admin",n)
 elif c==9:
 addpassword()
 elif c==10:
 Delete_User()
 elif c==11:
 Pending()
 else:
 print("Not a valid input")
 ch2=input("Do you want to perform more admin acƟons? Press Y for Yes")
 if ch2=="Y" or ch2=="y":
 Admin_Login(n)
 else:
 return
 
def User_Login(n):
 c=int(input("Choose desired acƟon. \n1.Searching Books currently available \n2.Book Details 
\n3.Seeing your own details"))
 if c==1:
 Search_Books()
 elif c==2:
 Book_Details()
 elif c==3:
 User_Details("User",n)
 else:
 print("Invalid input")
 ch2=input("Do you want to perform more user acƟons? Press Y for Yes")
 if ch2=="Y" or ch2=="y":
 User_Login(n)
 else:
 return
def Add_Books():
 bookname=input("Enter book name")
 autname=input("Enter author name")
 pubname=input("Enter publisher name")
 cost=int(input("Enter cost"))
 isbn=int(input("Enter isbn"))
 btype=input("Enter book type")
 date_entry=input("Enter date of entry")
 total_copies=int(input("Enter number of copies taken"))
 book_id=input("Enter book id")
 available_no=total_copies
 query="Insert into Book 
values('{}','{}','{}',{},{},'{}','{}',{},{},{},{},'{}')".format(bookname,autname,pubname,cost,isbn,btype,dat
e_entry,total_copies,available_no,lent_copy,ret_copy,book_id)
 cursor.execute(query)
 con.commit()
 print("Data inserted successfully")
 ch=input("Do you want to enter more books? Enter Y for yes, press any other key for No")
 if (ch=="Y" or ch=="y"):
 Add_Books()
def Add_User():
 st_name=input("Enter student name")
 cl=int(input("Enter class"))
 secƟon=(input("Enter secƟon"))
 roll_no=int(input("Enter roll"))
 st_id=input("Enter student id") 
 query="Insert into Student 
values('{}',{},'{}',{},'{}','{}','{}',{},'{}','{}')".format(st_name,cl,secƟon,roll_no,st_id,borrowpendret,statu
s,fine,dateborrow,dateret)
 cursor.execute(query)
 con.commit()
 print("Data inserted successfully")
 ch=input("Do you want to enter more users? Enter Y for yes, press any other key for No")
 if (ch=="Y" or ch=="y"):
 Add_User()
def Update_Books():
 
 bname=input("Enter a single book name for reference")
 
 if bname not in L:
 print("Book not available")
 else:
 s="select available_no,lent_copy,ret_copy from book where 
bookname='{}'".format(bname)
 cursor.execute(s)
 data=cursor.fetchone()
 available_no=data[0]
 lent_copy=data[1]
 ret_copy=data[2]
 print("Enter the corresponding numbers to update accordingly. ")
 print("1.Change Author Name \n2.Change publisher name \n3.Change cost \n4.Change 
isbn \n5.Change book type \n6.Change date of entry \n7.change book id \n8.update number of 
books lent \n9.update number of books received from borrowers") 
 i=int(input("Enter choice "))
 
 if i==1:
 autname=input("Enter new author name")
 query="update Book set autname='{}' where bookname='{}' 
".format(autname,bname)
 cursor.execute(query)
 con.commit()
 elif i==2:
 pubname=input("Enter new publisher name")
 query="update Book set pubname='{}' where 
bookname='{}'".format(pubname,bname)
 cursor.execute(query)
 con.commit()
 elif i==3:
 cost=int(input("Enter new cost"))
 query="update Book set cost={} where bookname='{}'".format(cost,bname)
 cursor.execute(query)
 con.commit()
 elif i==4:
 isbn=int(input("Enter new isbn"))
 query="update Book set isbn={} where bookname='{}'".format(isbn,bname)
 cursor.execute(query)
 con.commit()
 elif i==5:
 btype=input("Enter new book type")
 query="update Book set btype='{}' where bookname='{}' ".format(btype,bname)
 cursor.execute(query)
 con.commit()
 elif i==6:
 date_entry=input("Enter new date of entry")
 query="update Book set date_entry='{}' where bookname='{}' 
".format(date_entry,bname)
 cursor.execute(query)
 con.commit()
 elif i==7:
 book_id=input("Enter new book id")
 query="update Book set book_id={} where bookname='{}'".format(book_id,bname)
 cursor.execute(query)
 con.commit()
 elif i==8:
 if available_no > 0:
 print(available_no,"book(s) available for lending")
 lent_copy=int(input("Enter number of copies for lending"))
 db=input("Enter today's date")
 for i in range(0,lent_copy):
 sname=input("Enter the student name borrowing the book")
 
 
 query="Update Student set borrowpendret='{}' where 
st_name='{}'".format(bname,sname)
 cursor.execute(query)
 query="Update Student set dateborrow='{}' where 
st_name='{}'".format(db,sname)
 cursor.execute(query)
 
 query="update Student set status='{}' where 
st_name='{}'".format("Borrowed",sname)
 cursor.execute(query)
 con.commit() 
 else:
 print("Book not available for lending")
 query="update Book set available_no={} where 
bookname='{}'".format(available_no-lent_copy,bname)
 cursor.execute(query)
 query="update Book set lent_copy={} where 
bookname='{}'".format(lent_copy,bname)
 cursor.execute(query)
 con.commit()
 elif i==9:
 ret_copy=int(input("Enter number of copies returned"))
 
 query="update Book set available_no={} where 
bookname='{}'".format(available_no+ret_copy,bname)
 cursor.execute(query)
 query="update Book set ret_copy={} where bookname='{}'".format(ret_copy,bname)
 cursor.execute(query)
 con.commit()
 dr=input("Enter todays date")
 for i in range(0,ret_copy):
 name=input(("Enter the name of the student who returned the book"))
 query="update Student set status='{}' where 
st_name='{}'".format("Returned",name)
 cursor.execute(query)
 query="Update Student set dateret='{}' where st_name='{}'".format(dr,sname)
 cursor.execute(query)
 con.commit()
 else:
 print("Invalid input")
 ch2=input("Do you want to update more books? Press y for yes")
 if(ch2=="Y" or ch2=="y"):
 Update_Books()
 else:
 return
def Book_Details():
 print("Welcome to Book Details corner.")
 print("Search with: \n1.Book name \n2.Author name \n3.Publisher name \n4.Cost \n5.Isbn 
\n6.Book Type \n7.Date of entry\n8.Book id")
 while True:
 inp=int (input("Enter number . press 0 to exit. If input info not found, nothing will be 
printed."))
 
 if inp==0:
 break
 elif inp==1:
 d=input("Enter book name")
 query="select * from Book where bookname='{}' ".format(d)
 elif inp==2:
 d=input("Enter author name")
 query="select * from Book where autname='{}' ".format(d)
 elif inp==3:
 d=input("Enter publisher name")
 query="select * from Book where pubname='{}' ".format(d)
 elif inp==4:
 d=int(input("Enter cost"))
 query="select * from Book where cost={} ".format(d)
 elif inp==5:
 d=int(input("Enter isbn"))
 query="select * from Book where isbn={} ".format(d)
 elif inp==6:
 d=input("Enter book type")
 query="select * from Book where btype='{}' ".format(d)
 elif inp==7:
 d=input("Enter date of entry")
 query="select * from Book where date_entry='{}' ".format(d)
 elif inp==8:
 d=input("Enter book_id")
 query="select * from Book where book_id='{}' ".format(d)
 else:
 print("Invalid input")
 cursor.execute(query)
 data=cursor.fetchall()
 for i in data:
 print("Bookname",i[0])
 print("Author name",i[1])
 print("Publisher",i[2])
 print("Cost",i[3])
 print("Isbn",i[4])
 print("Book type",i[5])
 print("Date of entry",i[6])
 print("Total copies",i[7])
 print("Available",i[8])
 print("Lent (last entry)",i[9])
 print("Returned (last entry)",i[10])
 print("Book-id",i[11])
 print("*"*100)
 
def User_Details(t,n):
 
 print("Welcome to the user details dashboard.")
 if t=="User":
 query="Select * from Student where st_name='{}'".format(n)
 cursor.execute(query)
 i=cursor.fetchone()
 
 print("Student name",i[0])
 print("Class",i[1])
 print("SecƟon",i[2])
 print("Roll no.",i[3])
 print("Student ID",i[4])
 
 print("Book associated",i[5])
 print ("Date borrowed",i[8])
 print("Status",i[6])
 print("Date returned",i[9])
 
 print("Fine Pending",i[7])
 print("*"*100)
 
 elif t=="Admin":
 print("Search with:\n1. Student name \n2. Class \n3. SecƟon \n4. Roll no. \n5. Student ID 
\n6.Book Borrowed \7.Status")
 while True:
 keywd=int(input('''Enter number according to menu. Press 0 to exit. If user not 
found,nothing will be printed.'''))
 if keywd==0:
 break
 elif keywd==1:
 sname=input("Enter student name:")
 query="SELECT* FROM student WHERE st_name='{}'".format(sname)
 elif keywd==2:
 sclass=int(input("Enter student's class:"))
 query="SELECT* FROM student WHERE cl={}".format(sclass)
 elif keywd==3:
 ssec=input("Enter student's secƟon:")
 query="SELECT* FROM student WHERE secƟon='{}'".format(ssec)
 elif keywd==4:
 sroll=int(input("Enter student's roll no.:"))
 query="SELECT* FROM student WHERE roll_no={}".format(sroll)
 elif keywd==5:
 sid=input("Enter student id:")
 query="SELECT* FROM student WHERE st_id='{}'".format(sid)
 elif keywd==6:
 borr=input("Enter the book associated")
 query="SELECT* FROM student WHERE borrowpendret='{}'".format(borr)
 elif keywd==7:
 stat=input("Enter the status")
 query="SELECT* FROM student WHERE status='{}'".format(stat)
 else:
 print("Query not valid...Try Again")
 cursor.execute(query)
 data=cursor.fetchall()
 for i in data:
 print("Student name",i[0])
 print("Class",i[1])
 print("SecƟon",i[2])
 print("Roll no.",i[3])
 print("Student ID",i[4])
 print("Book associated",i[5])
 print("Dte borrowed",i[8])
 print("Status",i[6])
 print("Date returned",i[9])
 print("Fine Pending",i[7])
 print("*"*100)
 
def Delete_Books():
 bname=input("Enter the book name which you want to delete:")
 if bname not in L:
 print("Book not available")
 else:
 query="DELETE FROM Book WHERE bookname='{}'".format(bname)
 cursor.execute(query)
 con.commit()
 print("Book deleted successfully")
 ans=input("Do you want to delete more books? Press Y for yes")
 if ans in ("yY"):
 Delete_Books()
 else:
 return
def Delete_User():
 sname=input("Enter the student name which you want to delete:")
 if sname not in M:
 print("Student not available")
 else:
 query="DELETE FROM Student WHERE st_name='{}'".format(sname)
 cursor.execute(query)
 con.commit()
 query="DELETE FROM Password WHERE name='{}' and type='{}'".format(sname,"User")
 cursor.execute(query)
 con.commit()
 print("Student deleted successfully")
 ans=input("Do you want to delete more student data? Press Y for yes")
 if ans in ("yY"):
 Delete_User()
 else:
 return
def Fine():
 while True:
 f=int(input("Enter the number of days"))
 st_name=input("Enter the student name ")
 query="Update Student set fine={} where st_name='{}'".format(f*2,st_name)
 cursor.execute(query)
 con.commit()
 print("Fine updated")
 c=input("Do you want to update more fine amounts? Press Y for Yes")
 if c not in "Yy":
 break
 
def Search_Books():
 query="select bookname from book where available_no>0 order by bookname "
 cursor.execute(query)
 data=cursor.fetchall()
 for i in data:
 print(i[0])
def password(p,t,n):
 query="Select * from Password where name='{}' and type='{}'".format(n,t)
 cursor.execute(query)
 data=cursor.fetchone()
 if data==None:
 return
 elif data[2]==p:
 return True
def addpassword():
 while True:
 t=input("Enter type")
 n=input("Enter name")
 p=input("Enter password")
 query="Insert into password values('{}','{}','{}')".format(t,n,p)
 cursor.execute(query)
 con.commit()
 print("Data inserted successfully")
 c=input("Enter more? Y for Yes")
 if c not in "Yy":
 break
def Pending():
 while True:
 st_name=input("Enter name of student whose book is pending")
 query="Update Student set Status='{}' where st_name='{}'".format("Pending",st_name)
 cursor.execute(query)
 con.commit()
 c=input("More entries ? y for yes")
 if c in "Yy":
 Pending()
 else:
 break
global n
print("HI! WELCOME TO LIBRARY MANAGEMENT SYSTEM!")
print("*"*100)
ch=int(input("Enter 1 for Admin Login or 2 for User Login"))
if ch==1:
 
 n=input("Enter name")
 p=input("Enter password")
 if (password(p,"Admin",n)==True):
 print("WELCOME",n)
 print("*"*100)
 Admin_Login(n)
 else:
 print("You are invalid admin")
if ch==2:
 
 n=input("Enter name")
 p=input("Enter password")
 if (password(p,"User",n)==True):
 print("WELCOME",n)
 print("*"*100)
 print("LIBRARY RULES AND REGULATIONS")
 print("*"*100)
 print("1.Library will be closed on Saturday and Sunday. Visitors will not be allowed.")
 print("2.A fine will be charged @Rs.2/day aŌer a fortnight of issue of book if not 
returned.")
 print("3.You cannot issue a book more than once consecuƟvely.")
 print("4.Maintain complete peace in the library for others.")
 print("5.Bags and electronic devices are not permitetd within the premises of the 
library.")
 print("*"*100)
 User_Login(n)
 else:
 print("You are invalid user")
print("Thank you! Visit Again! ")
print("*"*100)
