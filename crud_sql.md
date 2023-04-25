SELECT * FROM member;
SELECT * FROM member WHERE member_id = 1;
INSERT INTO member (mobile_number, email, first_name, last_name, password) 
VALUES ('1234567890', 'test@example.com', 'John', 'Doe', 'password');
UPDATE member SET email = 'new_email@example.com' WHERE member_id = 1;
DELETE FROM member WHERE member_id = 1;
SELECT * FROM member WHERE first_name = 'John';
SELECT * FROM member WHERE mobile_number LIKE '123%';


SELECT * FROM membertasks;
SELECT * FROM membertasks WHERE member_task_id = 1;
INSERT INTO membertasks (name, due_date, is_task_completed, description, member_id) 
VALUES ('Task 1', '2022-05-01', 0, 'Description for task 1', 1);
UPDATE membertasks SET name = 'New task name' WHERE member_task_id = 1;
DELETE FROM membertasks WHERE member_task_id = 1;
SELECT * FROM membertasks WHERE member_id = 1 AND is_task_completed = 1;


INSERT INTO category (name, description, created, member_id) 
VALUES ('Category 1', 'Description for category 1', '2022-05-01 09:00:00', 1);
SELECT * FROM category WHERE category_id = 1;
SELECT * FROM category;
SELECT * FROM category WHERE category_id = 1;
UPDATE category SET name = 'New category name' WHERE category_id = 1;
DELETE FROM category WHERE category_id = 1;



SELECT * FROM taskcategory;
SELECT * FROM taskcategory WHERE task_category_id = 1;
INSERT INTO taskcategory (created, category_id, member_task_id)
VALUES ('2022-05-06 16:30:00', 3, 6);
DELETE FROM taskcategory WHERE task_category_id = 1;
UPDATE taskcategory SET created = '2022-05-01 09:00:00' WHERE task_category_id = 1;

