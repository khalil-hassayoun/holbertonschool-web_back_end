DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DROP VIEW IF EXISTS users_stats;
    CREATE VIEW users_stats AS
    SELECT cor.user_id, (SUM(cor.score * pro.weight) / SUM(pro.weight)) as arg 
    FROM corrections AS cor
    JOIN projects AS pro ON pro.id = cor.project_id
    GROUP BY cor.user_id;

    UPDATE users AS usr
    SET average_score = (
        SELECT arg FROM users_stats WHERE usr.id = user_id
    );
    DROP VIEW IF EXISTS users_stats;
END$$
DELIMITER ;
