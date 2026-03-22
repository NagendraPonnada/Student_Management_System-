-- MySQL Commands for Adding Student Data
-- Connect to MySQL first: mysql -u root -p

USE student_management_system;

-- Method 1: Insert single student
INSERT INTO testapp_student
(enrollment_number, first_name, last_name, email, phone, date_of_birth,
 gender, address, city, state, zipcode, joining_date, is_active, created_at, updated_at)
VALUES
('23J21A0001', 'Rahul', 'Sharma', 'rahul.sharma@example.com', '9876543216',
 '2002-01-15', 'M', '101 MG Road', 'Mumbai', 'Maharashtra', '400001',
 CURDATE(), 1, NOW(), NOW());

-- Method 2: Insert multiple students at once
INSERT INTO testapp_student
(enrollment_number, first_name, last_name, email, phone, date_of_birth,
 gender, address, city, state, zipcode, joining_date, is_active, created_at, updated_at)
VALUES
('23J21A0002', 'Priya', 'Patel', 'priya.patel@example.com', '9876543217',
 '2002-04-20', 'F', '202 Brigade Road', 'Bangalore', 'Karnataka', '560002',
 CURDATE(), 1, NOW(), NOW()),
('23J21A0003', 'Amit', 'Singh', 'amit.singh@example.com', '9876543218',
 '2001-09-10', 'M', '303 Park Street', 'Kolkata', 'West Bengal', '700003',
 CURDATE(), 1, NOW(), NOW()),
('23J21A0004', 'Sneha', 'Reddy', 'sneha.reddy@example.com', '9876543219',
 '2002-06-25', 'F', '404 Connaught Place', 'Delhi', 'Delhi', '110004',
 CURDATE(), 1, NOW(), NOW());

-- Verify the data was added
SELECT enrollment_number, first_name, last_name, email, city
FROM testapp_student
ORDER BY created_at DESC
LIMIT 5;

-- Check total count
SELECT COUNT(*) as total_students FROM testapp_student;

-- View all data
SELECT * FROM testapp_student;