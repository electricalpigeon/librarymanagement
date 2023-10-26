## Library Management Project
_Made as a part of AISSCE 12 course-work in CS_

## Note:

1) If admin has to nullify fine, he/she has to enter 0 as number of days.

2) The syntax requires a manual input to database at the very beginning for a admin and  his/her password before others.

3) Admin and Students will be required to enter a password to authenticate their access to the database. 

4) System is easy to use with proper values. If proper values are not inserted it may result into a  collapse.

5) Only one book can be borrowed at a time for 14 days. Renew option is not available.


## AIM:
To formulate and implement an error-free and successfully-working library 
management system using Python-Mysql connectivity. Python -the 
programming language is at the front end, while Mysql- the database is at the 
back end.

## PURPOSE:
An attempt to develop real-life computerised library management system for 
faster and easier transaction and manipulation of available data and records 
understandable to librarian and students alike.

## ADVANTAGES OF LIBRARY MANAGEMENT SYSTEM:

• Managing of Books in an electronic manner that saves human time, 
efforts and paper.

• It is more reliable and secure.

• Well organized, easy to search for books and maintain records.


## DISADVANTAGES OF LIBRARY MANAGEMENT SYSTEM:

• Could have added more functions to make it more realistic.

• No human interaction in an electronic version.

• Interactive interface is missing

## COMMANDS FOR MySQL-Database: CREATION OF TABLE BOOK.

create table Book(bookname varchar(500) not null primary key,

autname varchar(500) not null,

pubname varchar (500),

cost integer,

isbn integer unique,

btype varchar(50),

date_entry varchar(20),

total_copies integer not null check(total_copies >=0),

available_no integer not null check(available_no >=0 ),

lent_copy integer not null check(lent_copy >=0 ),

ret_copy integer not null check(ret_copy >=0 ),

book_id integer not null unique,

check (available_no<= total_copies and lent_copy<=available_no and ret_copy<=total_copies) )

## COMMANDS FOR MySQL-Database: CREATION OF TABLE STUDENT.

create table Student(st_name varchar(20) not null,

cl integer,

section varchar(5),

roll_no integer,

st_id varchar(15) primary key,

borrowpendret varchar(100),

status varchar(15),

fine integer,

dateborrow varchar(15),

dateret varchar(15));


## COMMANDS FOR MySQL-Database: CREATION OF TABLE PASSWORD.


create table Password(type varchar(10),

name varchar(100) not null,

password varchar (15) primary key);
