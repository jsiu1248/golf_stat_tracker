
BEGIN;
IF NOT EXISTS (SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.ROUTINES WHERE
        ROUTINE_TYPE='PROCEDURE' 
AND ROUTINE_SCHEMA='golf'
AND ROUTINE_NAME = 'insert_lpga_player'

    ) > 0
THEN BEGIN
    CREATE PROCEDURE insert_lpga_player
(
        IN id VARCHAR(255),
        IN first_name VARCHAR(255),
        IN last_name VARCHAR(255), 
        IN height INT (3),
        IN birthday DATETIME,
        IN country VARCHAR(255),
        IN residence VARCHAR(255), 
        IN birth_place VARCHAR(255),
        IN college VARCHAR(255)
)
  

INSERT INTO golf.lpga_player
    (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
VALUES
    (id, first_name, last_name, height, birthday, country, residence, birth_place, college);
    END;
    END IF

-- USE GOLF;

-- DELIMITER $$
--     CREATE PROCEDURE insert_lpga_player
-- (
--         IN id VARCHAR(255),
--         IN first_name VARCHAR(255),
--         IN last_name VARCHAR(255), 
--         IN height INT (3),
--         IN birthday DATETIME,
--         IN country VARCHAR(255),
--         IN residence VARCHAR(255), 
--         IN birth_place VARCHAR(255),
--         IN college VARCHAR(255)
-- )
--     IF (SELECT COUNT(*)
--         FROM INFORMATION_SCHEMA.ROUTINES WHERE
--         ROUTINE_TYPE='PROCEDURE' 
-- AND ROUTINE_SCHEMA='golf'
-- AND ROUTINE_NAME = 'insert_lpga_player'

--     ) = 0
-- THEN BEGIN

-- INSERT INTO golf.lpga_player
--     (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
-- VALUES
--     (id, first_name, last_name, height, birthday, country, residence, birth_place, college);
--     END;
--     END IF
-- $$
                 
-- SELECT count(*) > 0
-- into @myvar 
-- FROM INFORMATION_SCHEMA.ROUTINES 
-- WHERE 
--        ROUTINE_TYPE='PROCEDURE' 
--    AND ROUTINE_SCHEMA='golf'
--    AND ROUTINE_NAME = 'insert_lpga_player'

-- CREATE PROCEDURE insert_lpga_player
-- (
--         IN id VARCHAR(255),
--         IN first_name VARCHAR(255),
--         IN last_name VARCHAR(255), 
--         IN height INT (3),
--         IN birthday DATETIME,
--         IN country VARCHAR(255),
--         IN residence VARCHAR(255), 
--         IN birth_place VARCHAR(255),
--         IN college VARCHAR(255)
-- )

-- INSERT INTO golf.lpga_player
--     (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
-- VALUES
--     (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
--     
--     WHERE NOT EXISTS ();
-- END$$