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