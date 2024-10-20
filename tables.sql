USE iit_indore_db;

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_code VARCHAR(10) NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
    semester INT NOT NULL
);

-- Insert sample courses for BTech, CSE@IIT Indore
INSERT INTO courses (course_code, course_name, credits, semester)
VALUES 
('CS101', 'Introduction to Computer Science', 4, 1),
('CS102', 'Data Structures and Algorithms', 4, 2),
('CS201', 'Operating Systems', 4, 3),
('CS202', 'Computer Networks', 4, 4),
('CS301', 'Machine Learning', 4, 5),
('CS302', 'Artificial Intelligence', 4, 6),
('CS401', 'Blockchain Technologies', 4, 7),
('CS402', 'Cloud Computing', 4, 8);
