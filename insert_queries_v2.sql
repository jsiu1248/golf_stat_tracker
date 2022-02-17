
USE GOLF;

DROP insert_stat;
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



INSERT INTO golf.stat
    (id,earnings, drive_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank)
VALUES
    (id,earnings, drive_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank);

DROP insert_pga_player;
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

INSERT INTO golf.pga_player
    (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
VALUES
    (id, first_name, last_name, height, birthday, country, residence, birth_place, college);  

DROP insert_lpga_player;
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
