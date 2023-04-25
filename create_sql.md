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