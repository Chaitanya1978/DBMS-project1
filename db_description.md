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
