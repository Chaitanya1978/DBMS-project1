INSERT INTO member (mobile_number, email, first_name, last_name, password) 
VALUES ('1234567890', 'nsmr@example.com', 'John', 'Doe', 'abc123');

INSERT INTO member (mobile_number, email, first_name, last_name, password) 
VALUES ('0987654321', 'name@example.com', 'Jane', 'Doe', '123xyz');

INSERT INTO member (mobile_number, email, first_name, last_name, password) 
VALUES ('9999999999', 'sample@example.com', 'Jimmy', 'Smith', 'qwerty');

INSERT INTO member (mobile_number, email, first_name, last_name, password) 
VALUES ('1111111111', 'project@example.com', 'Susan', 'Jones', 'mnbvcx');

INSERT INTO member (mobile_number, email, first_name, last_name, password) 
VALUES ('4444444444', 'hello@example.com', 'Brandon', 'Rogers', 'asdfg');

INSERT INTO member (mobile_number, email, first_name, last_name, password) 
VALUES ('7777777777', 'exam@example.com', 'Amanda', 'Jackson', 'zxcvb');



INSERT INTO membertasks (name, due_date, is_task_completed, description, member_id) 
VALUES ('Grocery shop', '2023-05-01', 0, 'Buy groceries for next week', 1);

INSERT INTO membertasks (name, due_date, is_task_completed, description, member_id) 
VALUES ('Pay rent', '2023-05-05', 0, 'Pay rent for apartment', 2);

INSERT INTO membertasks (name, due_date, is_task_completed, description, member_id) 
VALUES ('Walk the dog', '2023-05-01', 1, 'Take the dog for a walk in the park', 3);

INSERT INTO membertasks (name, due_date, is_task_completed, description, member_id) 
VALUES ('Clean the garage', '2023-05-08', 0, 'Organize and clean the garage', 4);

INSERT INTO membertasks (name, due_date, is_task_completed, description, member_id) 
VALUES ('Finish project report', '2023-05-10', 0, 'Complete the project report for work', 5);

INSERT INTO membertasks (name, due_date, is_task_completed, description, member_id) 
VALUES ('Call the dentist', '2023-05-15', 0, 'Schedule a dental check-up', 6);



INSERT INTO category (name, description, created, member_id) 
VALUES ('Personal', 'Personal tasks and to-dos', '2023-04-30 10:00:00', 1);

INSERT INTO category (name, description, created, member_id) 
VALUES ('Work', 'Tasks related to work or career', '2023-04-30 10:30:00', 2);

INSERT INTO category (name, description, created, member_id) 
VALUES ('Health', 'Tasks related to health and fitness', '2023-04-30 11:00:00', 3);

INSERT INTO category (name, description, created, member_id) 
VALUES ('Home', 'Tasks related to home and household', '2023-04



INSERT INTO taskcategory (created, category_id, member_task_id)
VALUES ('2023-05-01 09:00:00', 1, 1);

INSERT INTO taskcategory (created, category_id, member_task_id)
VALUES ('2023-05-02 10:30:00', 2, 2);

INSERT INTO taskcategory (created, category_id, member_task_id)
VALUES ('2023-05-03 14:15:00', 3, 3);

INSERT INTO taskcategory (created, category_id, member_task_id)
VALUES ('2023-05-04 11:45:00', 2, 4);

INSERT INTO taskcategory (created, category_id, member_task_id)
VALUES ('2023-05-05 13:00:00', 1, 5);

INSERT INTO taskcategory (created, category_id, member_task_id)
VALUES ('2023-05-06 16:30:00', 3, 6);



