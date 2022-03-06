USE GOLF;

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
    IN world_rank INT(4)
)
INSERT IGNORE INTO golf.stat
    (id,earnings, drive_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank)
VALUES
    (id,earnings, drive_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank);


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


DROP PROCEDURE IF EXISTS insert_session_type;
CREATE PROCEDURE insert_session_type
(
)
INSERT IGNORE INTO golf.session_type
    (name)
VALUES
    ('round'),('practice');


DROP PROCEDURE IF EXISTS insert_stat_type;
CREATE PROCEDURE insert_stat_type
(
)
INSERT IGNORE INTO golf.stat_type
    (name)
VALUES
    ('driving_distance'),('green_in_regulation'),('total_score'),('putts'),('fairway_hit'),('proximity_to_hole'),('scramble');


DROP PROCEDURE IF EXISTS insert_shot_type;
CREATE PROCEDURE insert_shot_type
(
)
INSERT IGNORE INTO golf.shot_type
    (name)
VALUES
    ('sand'), ('chip'), ('pitch'), ('drive'), ('iron'), ('putt');


DROP PROCEDURE IF EXISTS insert_round;
CREATE PROCEDURE insert_round
(
        IN session_id INT(10),
        IN hole INT(2),
        IN green_reg INT(1),
        IN score INT(3),
        IN putt INT(1), 
        IN fairway INT(1),
        IN proximity_to_hole FLOAT(5), 
        IN scramble INT(1)
)
INSERT IGNORE INTO golf.round
    (session_id, hole, green_reg, score, putt, fairway, proximity_to_hole, scramble)
VALUES
    (session_id, hole, green_reg, score, putt, fairway, proximity_to_hole, scramble);


DROP PROCEDURE IF EXISTS insert_practice;
CREATE PROCEDURE insert_practice
(
        IN session_id INT(10),
        IN shot_type_id INT(3), 
        IN success INT(3),
        IN total INT(3),
        IN distance FLOAT(5),
        IN club_id INT(5)

)
INSERT IGNORE INTO golf.practice
    (session_id, shot_type_id, success, total, distance, club_id)
VALUES
    (session_id, shot_type_id, success, total, distance, club_id);


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

    
DROP PROCEDURE IF EXISTS insert_club;
CREATE PROCEDURE insert_club
(
)
INSERT IGNORE INTO golf.club
    (name)
VALUES
    ('5_iron'), ('6_iron'), ('7_iron'), ('8_iron'), ('9_iron'), ('pitching wedge'), ('52 degree'), ('58 degree'), ('3 hybrid'),('4 hybrid'),('driver'),('putter');