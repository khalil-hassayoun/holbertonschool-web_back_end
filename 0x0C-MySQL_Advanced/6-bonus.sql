-- a SQL script that creates a stored procedure AddBonus that
-- adds a new correction for a student.
DELIMITER //

CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
IF
EXISTS(SELECT * from projects WHERE name = project_name LIMIT 1)
THEN
SET @project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
ELSE
INSERT INTO projects (name) VALUES (project_name);
SET @project_id = LAST_INSERT_ID();
END IF;
INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, @project_id, score);
END//
DELIMITER ;
