-- a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
UPDATE users
SET average_score = (SELECT SUM(score * (SELECT weight FROM projects WHERE id = corrections.project_id)) / (SELECT sum(weight) FROM projects) FROM corrections WHERE corrections.user_id = user_id) WHERE id = user_id;
END//
DELIMITER ;
