-- a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
UPDATE users
SET average_score = (SELECT SUM(score * (SELECT weight FROM projects WHERE id = corrections.project_id)) / (SELECT sum(weight) FROM projects) FROM corrections WHERE corrections.user_id = user_id) WHERE id = user_id;
END//
DELIMITER ;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN

DECLARE finished INTEGER DEFAULT 0;
DECLARE user_id INT;

DECLARE curid CURSOR FOR SELECT id FROM users;

DECLARE CONTINUE HANDLER
      FOR NOT FOUND SET finished = 1;

OPEN curid;

getid: LOOP
  FETCH curid INTO user_id;
  IF finished = 1 THEN
  LEAVE getEmail;
  END IF;
CALL ComputeAverageWeightedScoreForUser(user_id);
END LOOP getid;
CLOSE curid;

END//
DELIMITER ;
