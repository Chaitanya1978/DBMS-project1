### A description of your database

We created the database for the task manager application using sqlite3 database.

Task manager application is using to manage the daily tasks and categories of the users or members. 
The database is designed to be easy to use and allowing users to quickly and easily create, update, and manage tasks and 
categories. We have created the 4 tables in this database and table names are member, membertasks, category and
taskcategory.

member table: This table stores information about the members of the application, 
including their mobile_number, personal email address,full name and password.

The Tasks table stores information about the tasks in the application, including their name, description, due date, 
and completion status.

The Categories table stores information about the categories in the application, including their name and the member who created them(foreign key to member table)

The Task Categories table is used to associate tasks with categories(foreign key relationship with tasks table and
category table), allowing member to organize their tasks by category.

### tables


CREATE TABLE "member" (
"member_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"mobile_number" varchar(12) NOT NULL,
"email" varchar(254) NOT NULL,
"first_name" varchar(50) NOT NULL,
"last_name" varchar(50) NOT NULL,
"password" varchar(18) NOT NULL
);


CREATE TABLE "membertasks" (
"member_task_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(100) NOT NULL, 
"due_date" date NOT NULL, 
"is_task_completed" bool NOT NULL, 
"description" varchar(200) NULL, 
"member_id" integer NOT NULL REFERENCES "member" ("member_id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE "category" (
"category_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(100) NOT NULL, 
"description" varchar(200) NULL,
"created" datetime NOT NULL, 
"member_id" integer NOT NULL REFERENCES "application_code_member" ("member_id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE "taskcategory" (

"task_category_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"created" datetime NOT NULL, 
"category_id" integer NOT NULL REFERENCES "category" ("category_id") DEFERRABLE INITIALLY DEFERRED, 
"member_task_id" integer NOT NULL REFERENCES "membertasks" ("member_task_id") DEFERRABLE INITIALLY DEFERRED
);


### attributes

# member table

member_id (integer, primary key, autoincrement)
mobile_number (varchar(12), not null)
email (varchar(254), not null)
first_name (varchar(50), not null)
last_name (varchar(50), not null)
password (varchar(18), not null)


# Member Tasks table:

member_task_id (integer, primary key, autoincrement)
name (varchar(100), not null)
due_date (date, not null)
is_task_completed (bool, not null)
description (varchar(200), null)
member_id (integer, not null, foreign key referencing member(member_id))

# Category table:

category_id (integer, primary key, autoincrement)
name (varchar(100), not null)
description (varchar(200), null)
created (datetime, not null)
member_id (integer, not null, foreign key referencing member(member_id))

# Task Category table

task_category_id (integer, primary key, autoincrement)
created (datetime, not null)
category_id (integer, not null, foreign key referencing category(category_id))
member_task_id (integer, not null, foreign key referencing member_tasks(member_task_id))

# primary keys

Member table: member_id

Member Tasks table:: member_task_id

Category table: category_id

Task Category table: task_category_id

#  foreign keys

member Tasks table: member_id (foreign key referencing member(member_id))

category table: member_id (foreign key referencing member(member_id))

Task Category table: 

category_id (foreign key referencing category(category_id))
member_task_id (foreign key referencing member_tasks(member_task_id))

## foreign key constraints

above we added the foreign key information, and we added the deferrable initially deferred clause allows 
for the constraints to be deferred until the transaction is committed.

### FDs

# Member table
member_id -> mobile_number, email, first_name, last_name, password

# Member Tasks table:
member_task_id -> name, due_date, is_task_completed, description, member_id

# Category table:
category_id -> name, description, created, member_id


# Task Category table:
task_category_id -> created, category_id, member_task_id


# whether in 3NF

Yes, all above tables are in 3NF form.



### one or two rows of sample data for each table.

member_id	mobile_number	email	              first_name	last_name	password
1	         1234567890	   john.doe@example.com	    John	       Doe	      abc123
2	          0987654321	jane.doe@example.com	Jane	        Doe	       123xyz



member_task_id	name	     due_date	  is_task_completed	     description	               member_id
   1	         Grocery shop	 2023-04-24	         0	           Buy groceries for next week	      1
   2	         Pay rent	     2022-05-05	         0	            Pay rent for apartment	          2


category_id	     name	           description	                  created	         member_id
1	          Personal	       Personal tasks and to-dos	    2023-04-23 10:00:00     	1
2	            Work	      Tasks related to work or career	2023-04-23 10:30:00      	2


task_category_id	created	            category_id	    member_task_id
  1	             2022-04-30 11:00:00	    1	            1
  2	             2022-04-30 11:30:00	    2	            2