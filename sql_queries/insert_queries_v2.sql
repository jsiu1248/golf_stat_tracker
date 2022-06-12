USE GOLF;

-- Currently, I am dropping the procedure everytime that it is being run again.
-- But, I tried to find another function that would not drop it every time such as IF EXISTS.

-- This procedure inserts data to the stat table.
DROP PROCEDURE IF EXISTS insert_stat;
CREATE PROCEDURE insert_stat
(
    IN id CHAR(255),
    IN earnings FLOAT(13),
    IN drive_avg FLOAT(6),
    IN gir_pct FLOAT(4),
    IN putt_avg FLOAT(4),
    IN sand_saves_pct FLOAT(4),
    IN birdies_per_round FLOAT(4),
    IN hole_proximity_avg VARCHAR(255),
    IN scrambling_pct FLOAT(4),
    IN world_rank INT(4),
    IN scoring_avg FLOAT(5)

)
INSERT IGNORE INTO golf.stat
    (id,earnings, drive_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank, scoring_avg)
VALUES
    (id,earnings, drive_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank, scoring_avg);

-- This inserts data to the pga_player table.
DROP PROCEDURE IF EXISTS insert_pga_player;
CREATE PROCEDURE insert_pga_player
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
INSERT IGNORE INTO golf.pga_player
    (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
VALUES
    (id, first_name, last_name, height, birthday, country, residence, birth_place, college);

-- This inserts data for the lgpa_player table. But, it is only biodemo data for them.
DROP PROCEDURE IF EXISTS insert_lpga_player;
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
INSERT IGNORE INTO golf.lpga_player
    (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
VALUES
    (id, first_name, last_name, height, birthday, country, residence, birth_place, college);

-- This inserts data to the golf_course whenever there is a new course
DROP PROCEDURE IF EXISTS insert_golf_course;
CREATE PROCEDURE insert_golf_course
(
        IN course_name VARCHAR(255),
        IN hole INT(2)
)
INSERT IGNORE INTO golf.golf_course
    (course_name, hole)
VALUES
    (course_name, hole);

-- Creating a lookup table that has the session_types "round" and "practice."
DROP PROCEDURE IF EXISTS insert_session_type;
CREATE PROCEDURE insert_session_type
(
)
INSERT IGNORE INTO golf.session_type
    (name)
VALUES
    ('round'),('practice');

-- Lookup table for stat_type.
DROP PROCEDURE IF EXISTS insert_stat_type;
CREATE PROCEDURE insert_stat_type
(
)
INSERT IGNORE INTO golf.stat_type
    (name)
VALUES
    ('driving_distance'),('green_in_regulation'),('total_score'),('putts'),('fairway_hit'),('proximity_to_hole'),('scramble');

-- Lookup table for shot_type
DROP PROCEDURE IF EXISTS insert_shot_type;
CREATE PROCEDURE insert_shot_type
(
)
INSERT IGNORE INTO golf.shot_type
    (name)
VALUES
    ('sand'), ('chip'), ('pitch'), ('drive'), ('iron'), ('putt');

-- Insert round data
DROP PROCEDURE IF EXISTS insert_round;
CREATE PROCEDURE insert_round
(
        IN player_id VARCHAR(255),
        IN session_id INT(10),
        IN hole INT(2),
        IN green_reg INT(1),
        IN score INT(3),
        IN putt INT(1),
        IN fairway INT(1),
        IN proximity_to_hole FLOAT(5),
        IN scramble INT(1),
        IN sand_success INT(1),
        IN sand_total INT(1)
)
INSERT IGNORE INTO golf.round
    (player_id, session_id, hole, green_reg, score, putt, fairway, proximity_to_hole, scramble, sand_success, sand_total)
VALUES
    (player_id, session_id, hole, green_reg, score, putt, fairway, proximity_to_hole, scramble, sand_success, sand_total);

-- Insert practice data
DROP PROCEDURE IF EXISTS insert_practice;
CREATE PROCEDURE insert_practice
(
        IN player_id VARCHAR(255),
        IN session_id INT(10),
        IN shot_type_id INT(3),
        IN success INT(3),
        IN total INT(3),
        IN distance FLOAT(5),
        IN club_id INT(5)

)
INSERT IGNORE INTO golf.practice
    (player_id, session_id, shot_type_id, success, total, distance, club_id)
VALUES
    (player_id, session_id, shot_type_id, success, total, distance, club_id);

-- Insert session data.
DROP PROCEDURE IF EXISTS insert_session;
CREATE PROCEDURE insert_session
(
            IN session_type_id INT(2),
            IN course_id INT(10),
            IN date DATE,
            IN notes LONGTEXT,
            IN goals LONGTEXT
)
INSERT IGNORE INTO golf.self_session
    ( session_type_id, course_id, date, notes, goals)
VALUES
    ( session_type_id, course_id, date, notes, goals);

-- Insert distance tracking for each club
DROP PROCEDURE IF EXISTS insert_distance_tracking;
CREATE PROCEDURE insert_distance_tracking
(
        IN date DATE,
        IN club_id INT(5),
        IN distance FLOAT(5)
)
INSERT IGNORE INTO golf.distance_tracking
    (date, club_id, distance)
VALUES
    (date, club_id, distance);

-- Insert the name of clubs
DROP PROCEDURE IF EXISTS insert_club;
CREATE PROCEDURE insert_club
(
)
INSERT IGNORE INTO golf.club
    (name)
VALUES
    ('5_iron'), ('6_iron'), ('7_iron'), ('8_iron'), ('9_iron'), ('pitching wedge'), ('52 degree'), ('58 degree'), ('3 hybrid'),('4 hybrid'),('driver'),('putter');


-- Insert holes and pars for new golf courses
DROP PROCEDURE IF EXISTS insert_hole;
CREATE PROCEDURE insert_hole
(
        IN golf_course_id INT(5),
        IN hole_num INT(2),
        IN par INT(1)
)
INSERT IGNORE INTO golf.hole
    (golf_course_id, hole_num, par)
VALUES
    (golf_course_id, hole_num, par);




    -- have to change safe mode for a bit

SET SQL_SAFE_UPDATES = 0;

-- Manually setting personal player_id
UPDATE golf.round
SET player_id='00000000-0000-0000-0000-000000000001';

-- Manually setting personal player_id
UPDATE golf.practice
SET player_id='00000000-0000-0000-0000-000000000001';

SET SQL_SAFE_UPDATES = 1;

-- Please add your own data for the insert below.

INSERT IGNORE INTO pga_player
(id, first_name, last_name, height, birthday, country, residence, birth_place, college)
VALUES
('00000000-0000-0000-0000-000000000001', 'Jonathan','Siu',64, '1992-01-24 00:00:00', 'UNITED STATES','Mountain View, CA, USA', 'San Francisco, CA, USA', 'Case Western Reserve University')

-- inserting player_id into stat
INSERT IGNORE INTO GOLF.STAT
(id)
VALUES
('00000000-0000-0000-0000-000000000001')

-- inserting world_rank into stat for player
UPDATE golf.stat
SET world_rank=0
WHERE id='00000000-0000-0000-0000-000000000001';


-- Creating personal stats
DROP PROCEDURE IF EXISTS personal_stat;
CREATE PROCEDURE personal_stat
(
        IN GIR_PCT FLOAT(4),
        IN PUTT_AVG FLOAT(4),
        IN DRIVE_AVG FLOAT(6),
        IN SCRAMBLING_PCT FLOAT(4),
        IN score_avg FLOAT(5)
)

UPDATE golf.stat
SET gir_pct=(SELECT green_reg_avg FROM GOLF.round_data_dim),
putt_avg=(SELECT putt_avg FROM GOLF.round_data_dim),
drive_avg=(SELECT AVG(DISTANCE) AVG_DRIVE FROM golf.practice_data WHERE SHOT_TYPE_NAME='drive'),
scrambling_pct=(SELECT scramble_avg FROM GOLF.round_data_dim),
scoring_avg=(SELECT AVG(TOTAL_SCORE) FROM GOLF.round_data_summary),
sand_saves_pct=(SELECT SAND_SAVES_PCT FROM GOLF.round_data_dim)

WHERE ID='00000000-0000-0000-0000-000000000001';

-- Set player_type to non_pga
UPDATE golf.stat
SET player_type='non-pga'
WHERE id='00000000-0000-0000-0000-000000000001';

-- Setting pga_players to pga so that it is easier for visualizations later
UPDATE golf.stat
SET player_type='pga'
WHERE id <> '00000000-0000-0000-0000-000000000001';

-- Setting player earning to 0
UPDATE golf.stat
SET earnings=0
WHERE id = '00000000-0000-0000-0000-000000000001';

